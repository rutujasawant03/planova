🌍 Planova – AI-Powered Smart Planner 

AI-powered trip & task planner that turns natural language goals into structured, actionable plans.  
It integrates **Google Custom Search** for real-world info, **OpenWeather API** for live weather, and stores plans in a **SQLite database** with a simple **Flask web app** frontend.  

---

🚀 Features  
- Accepts natural language goals (e.g., “Plan a 2-day trip to Goa with beaches & nightlife”).  
- Breaks them into clear **day-by-day itineraries**.  
- Enriches results with:  
  - 🌍 **Google Search** → key place descriptions  
  - 🌦️ **Weather API** → real-time forecasts  
- Saves all generated plans in **SQLite** for later access.  
- Clean web interface to:  
  - Enter new goals  
  - View generated plan  
  - Browse history of past plans  

---

🖼️ Workflow Diagram  

```mermaid
flowchart TD
    A[User enters goal in Web UI] --> B[Flask App]
    B --> C[Planner Agent Gemini LLM]
    C --> D[Google Custom Search API]
    C --> E[OpenWeather API]
    D --> C
    E --> C
    C --> F[Day-by-Day Structured Plan]
    F --> G[SQLite Database]
    G --> H[Web UI - Show Plan + History]


⚙️ Setup Instructions

### 1️⃣ Clone Repo

```bash
git clone https://github.com/rutujasawant03/planova.git
cd wonderplan-ai
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 4️⃣ Add API Keys

Create a `.env` file in the project root:

```bash
# Gemini / OpenAI API key
GEMINI_API_KEY=your_gemini_api_key_here

# Google Custom Search API key
GOOGLE_API_KEY=your_google_api_key_here
SEARCH_ENGINE_ID=your_search_engine_id_here

# OpenWeatherMap API key
WEATHER_API_KEY=your_openweather_key_here
```

### 5️⃣ Run the App

```bash
python app.py
```

Then open: [http://localhost:5000]

---

📖 Example Goals

### Example 1:

**Input** → `Plan a 2-day vegetarian food tour in Hyderabad`
**Output** →

Here is a structured 2-day vegetarian food tour itinerary for Hyderabad, designed for a professional travel planner:

---

**2-Day Vegetarian Food Tour in Hyderabad**
> Hyderabad District is a city-district in the state of Telangana ,It is the smallest in terms of area, among all the districts in the state, but has the highest ...

This itinerary focuses on showcasing the diverse and rich vegetarian culinary landscape of Hyderabad, from traditional South Indian flavors to local Hyderabadi specialties, with a touch of modern twists.

---

**Day 1: Traditional Breakfast, Thali Feast & Street Delights**
**Day 1 Weather:**
Temperature: 24°C, Conditions: Thunderstorm with light rain

**Morning (8:00 AM - 12:30 PM): Arrival and Classic South Indian Breakfast**

* **8:00 AM:** Arrive in Hyderabad. Check into your pre-booked accommodation.

> Hyderabad district was formed initially in the year 1948 followed by Police Action by merging the Atraf-a-Balda District and Baghat Districts. In the year 1978, ...

* **9:30 AM:** Head to a renowned South Indian restaurant such as Chutneys or a popular local tiffin center.

* **Activity:** Indulge in a quintessential Hyderabadi breakfast experience. Savor crispy Masala Dosa, fluffy Idli, spicy Vada, and delicate Upma, all served with an assortment of fresh chutneys and sambar. Conclude with a piping hot cup of filter coffee.

* **11:00 AM:** Take a gentle stroll around the vibrant streets of Banjara Hills or Jubilee Hills, enjoying the morning atmosphere and light exercise.

* **12:00 PM:** Return to your hotel for a brief rest and to freshen up.

**Afternoon (1:00 PM - 5:30 PM): Grand Vegetarian Thali and Iconic Desserts**

* **1:00 PM:** Experience an authentic Andhra/Telangana style vegetarian thali for lunch. Visit a restaurant like Subbayya Gari Hotel (or similar traditional meal providers).

* **Activity:** Enjoy a lavish, unlimited spread featuring rice, various regional curries (pappu, koora), tangy sambar, spicy rasam, a variety of pickles, chutneys, and a sweet dish. This is a true culinary immersion into local flavors.

* **3:00 PM:** Visit a legendary Hyderabadi bakery or sweet shop, such as Karachi Bakery or Pista House (known for their sweets selection).

* **Activity:** Sample traditional Hyderabadi vegetarian desserts. Try Double ka Meetha (bread pudding), Khubani ka Meetha (apricot dessert), and pick up some world-famous Osmania Biscuits to enjoy with tea.

* **4:30 PM:** Find a cozy Irani Cafe in areas like Charminar or Himayatnagar.

* **Activity:** Immerse yourself in Hyderabad's unique Irani Chai culture. Enjoy a rich, sweet cup of Irani Chai paired with your Osmania Biscuits, soaking in the local ambiance.

> Hyderabad District is a city-district in the state of Telangana ,It is the smallest in terms of area, among all the districts in the state, but has the highest ...

**Evening (6:00 PM - 9:30 PM): Street Food Exploration & Diverse Dinner**

* **6:00 PM:** Explore the lively street food scene. Head to an area known for its diverse vegetarian snacks. While Charminar area is popular, specific vegetarian street food clusters can be found near Koti or Begum Bazaar.

* **Activity:** Taste local vegetarian street delights like Mirchi Bajji (chilli fritters), Punugulu (fried rice-flour dumplings), and a variety of Indian chaat (savory snacks).

* **7:30 PM:** Dinner at a popular multi-cuisine vegetarian restaurant known for its extensive menu and quality. Look for establishments offering a blend of North and South Indian vegetarian dishes.

* **Activity:** Indulge in a comprehensive dinner. Options could include a rich Paneer dish, a wholesome vegetarian Pulao, or a specially prepared vegetarian version of Hyderabadi Biryani (note: traditional Hyderabadi Biryani is meat-based, but vegetarian adaptations are widely available and popular).

* **9:00 PM:** Return to your hotel to relax after a day of culinary adventures.

---

**Day 2: Regional Specialties, Spice Markets & Farewell Feast**
**Day 2 Weather:**
Temperature: 26°C, Conditions: Cloudy with scattered showers

**Morning (8:30 AM - 12:30 PM): Unique Breakfast & Sensory Spice Market**

* **8:30 AM:** Enjoy breakfast at a different local establishment, perhaps one specializing in regional Andhra vegetarian dishes.

* **Activity:** Try specialties like Pesarattu (green gram dosa served with ginger chutney) or Dibba Roti (thick, crispy pan-fried dosa), showcasing another facet of South Indian breakfast.

* **10:00 AM:** Visit the bustling Begum Bazaar or Laad Bazaar (near Charminar).

* **Activity:** Immerse yourself in the vibrant colors and aromas of a traditional Indian spice market. Observe a vast array of spices, pulses, and local ingredients that form the backbone of Hyderabadi cuisine. It’s an excellent opportunity for sensory learning and perhaps purchasing authentic spices.

* **12:00 PM:** Start making your way back or towards your next culinary destination.

**Afternoon (1:00 PM - 5:30 PM): Modern Vegetarian Cuisine & Culinary Insights**

* **1:00 PM:** Lunch at a contemporary vegetarian cafe or a restaurant offering fusion Indian cuisine. Explore options in areas like Jubilee Hills or Kavuri Hills.

* **Activity:** Experience a modern take on vegetarian dining. Savor innovative dishes, fresh salads, or creatively presented Indian meals, offering a refreshing contrast to traditional fare.

* **3:00 PM:** Participate in a culinary demonstration or a mini-workshop (if pre-arranged with a local chef or cooking school).

* **Activity:** Learn to prepare a simple Hyderabadi vegetarian snack or a traditional South Indian dish. Gain insights into local cooking techniques and the use of specific ingredients. If a workshop isn't available, a visit to a gourmet food store can offer similar insights.

* **4:30 PM:** Enjoy a final leisurely Irani Chai break, perhaps trying a different bakery item or a fresh fruit juice.

**Evening (6:30 PM - 9:30 PM): Grand Farewell Dinner & Departure**

* **6:30 PM:** Indulge in a grand farewell dinner at a highly-rated vegetarian fine dining restaurant. Choose a place known for its elegant ambiance and exquisite Indian vegetarian fare, offering a memorable closing to your tour.

* **Activity:** Enjoy a sophisticated multi-course vegetarian meal, reflecting on the rich and diverse flavors experienced throughout your Hyderabad culinary journey.

* **8:30 PM:** Head to the airport or train station for your departure, or return to your hotel for an overnight stay if departing the next day.

---

### Example 2:

**Input** → `“Organise a 5‑step daily study routine for learning Python.”`
**Output** →

Welcome to your personalized 5-day Python Study Expedition!

This itinerary is designed to build a strong foundation in Python through consistent, structured learning. Each day follows a dynamic 5-step routine to ensure comprehensive understanding and practical application.

> Jun 30, 2025 ... Need variable descriptions in a consistent format? Just show the LLM ... For each, suggest columns to analyze and Python methods.” The ...

Your 5-Step Daily Python Study Routine:

1. Review & Warm-up: Revisit yesterday's concepts and tackle quick challenges.

2. Learn New Concept: Dive into new topics with tutorials, documentation, and theory.

3. Hands-on Practice & Exercises: Apply what you've learned through coding along and solving problems.

4. Apply & Build (Mini-Project): Integrate multiple concepts by working on a small, focused project.

5. Reflect & Plan: Consolidate learning, identify areas for improvement, and prepare for tomorrow.

Let's embark on your Python journey!

---

## 🤝 AI Assistance Disclosure

Parts of this project (prompting, database setup, workflow diagram, and README drafting) were built with help from **ChatGPT (OpenAI GPT-5)**.

---

## 📌 Next Steps (Future Work)

* Add support for **multi-city trips**
* Export itineraries to **PDF/ICS calendar format**
* User login for personalized history




