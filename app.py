from flask import Flask, render_template, request
from datetime import datetime
import pytz

app = Flask(__name__)

# ---------------- Helper: IST Time ----------------
def get_ist_time():
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist)
    return current_time.strftime("%Y-%m-%d %H:%M:%S")

# ---------------- Dummy Weather ----------------
def get_weather(city="Lucknow"):
    # Dummy response for demo
    return f"☀ Weather in {city}: Clear sky, 28°C (Checked at {get_ist_time()})"

# ---------------- Dummy Train ----------------
def get_train_info(train_name="Rajdhani"):
    # Dummy response for demo
    return f"🚆 Train {train_name} Express (12309) runs from New Delhi to Mumbai Central."

# ---------------- Dummy Bus ----------------
def get_bus_info(city="Lucknow"):
    # Dummy response for demo
    return f"🚌 Next bus in {city}: Route 101 at 5:30 PM (IST)"

# ---------------- Chatbot Logic ----------------
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "bus" in user_input:
        return get_bus_info("Lucknow")
    if "train" in user_input:
        return get_train_info("Rajdhani")
    if "weather" in user_input:
        return get_weather("Lucknow")
    if "time" in user_input:
        return f"🕒 Current IST Time: {get_ist_time()}"

    return "🤖 Sorry, I didn’t understand. Try asking about bus, train, weather, or time."

# ---------------- Flask Routes ----------------
@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_text = request.form["msg"]
    return chatbot_response(user_text)

if __name__ == "__main__":
    app.run(debug=True)