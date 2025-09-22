import google.generativeai as genai
import requests
import sqlite3
from datetime import datetime
import re
from dotenv import load_dotenv
import os

DB_FILE = "plans.db"

# --- Initialize Database ---
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT,
            plan TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()



load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


# --- Configure Gemini ---
genai.configure(api_key=GEMINI_API_KEY)

# --- Helper: Extract city from user input ---
def extract_city(text):
    match = re.search(r'\bto\s+([A-Z][a-zA-Z\s]+)', text)
    if match:
        return match.group(1).strip()
    match = re.search(r'\bin\s+([A-Z][a-zA-Z\s]+)', text)
    if match:
        return match.group(1).strip()
    capitals = re.findall(r'\b[A-Z][a-zA-Z]{2,}\b', text)
    if capitals:
        return capitals[0]
    return None

# --- Weather Fetch ---
def get_weather(city):
    if not city:
        return "Temperature unavailable, Conditions unavailable"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    try:
        resp = requests.get(url).json()
        if resp.get("main") and resp.get("weather"):
            temp = round(resp['main']['temp'])
            condition = resp['weather'][0]['description'].capitalize()
            return f"Temperature: {temp}°C, Conditions: {condition}"
    except:
        pass
    return "Temperature unavailable, Conditions unavailable"

# --- Google Custom Search Description ---
def get_place_description(place_name):
    try:
        url = f"https://www.googleapis.com/customsearch/v1"
        params = {
            "key": GOOGLE_API_KEY,
            "cx": SEARCH_ENGINE_ID,
            "q": place_name,
            "num": 1
        }
        resp = requests.get(url, params=params).json()
        if "items" in resp and len(resp["items"]) > 0:
            snippet = resp["items"][0]["snippet"].replace("\n", " ").strip()
            return snippet
    except Exception as e:
        print("Error fetching description:", e)
    return "Description not available"

# --- Generate Trip Plan ---
def generate_plan(query):
    city = extract_city(query)
    weather = get_weather(city)

    prompt = f"""
You are a professional travel planner.
Create a structured day-by-day itinerary for: {query}.
Include Morning, Afternoon, Evening activities with times.
Add actual forecasted weather for each day: "{weather}".
Keep natural readable formatting with line breaks and bullet points.
Do not use markdown symbols like *, ###, or ---.
Make steps actionable and easy to follow.
"""
    model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")
    response = model.generate_content(prompt)
    plan_text = response.text.strip()

    # Enrich with descriptions for each location
    enriched_lines = []
    for line in plan_text.split("\n"):
        enriched_lines.append(line)
        # naive detection: capitalized proper nouns following 'at', 'to', or 'in'
        match = re.search(r"\b(?:at|to|in)\s+([A-Z][a-zA-Z\s]+)", line)
        if match:
            place = match.group(1).strip()
            desc = get_place_description(place)
            enriched_lines.append(f"  -> {desc}")
    enriched_plan = "\n".join(enriched_lines)

    save_plan(query, enriched_plan)
    return enriched_plan

# --- Database ---
def save_plan(query, plan):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO plans (query, plan, timestamp) VALUES (?, ?, ?)",
              (query, plan, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT query, plan, timestamp FROM plans ORDER BY id DESC LIMIT 5")
    rows = c.fetchall()
    conn.close()
    return rows
