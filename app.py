from flask import Flask, render_template, request
from planner_agent import generate_plan, get_history

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    plan = None
    if request.method == "POST":
        query = request.form.get("query")
        if query:
            plan = generate_plan(query)
    history = get_history()
    return render_template("index.html", plan=plan, history=history)

if __name__ == "__main__":
    app.run(debug=True)
