import os
from slack_bolt import App
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Slack App
app = App(token=os.getenv("SLACK_BOT_TOKEN"), signing_secret=os.getenv("SLACK_SIGNING_SECRET"))

# Gemini setup
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

@app.event("app_mention")
def handle_mention(event, say):
    user_input = event["text"]
    response = model.generate_content(user_input)
    reply = response.text
    say(reply)

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
