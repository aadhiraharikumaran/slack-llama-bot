import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
from langgraph_agent import get_graph

load_dotenv()

# Slack credentials
app = App(token=os.environ["SLACK_BOT_TOKEN"])
graph = get_graph()

@app.message("")
def handle_message_events(message, say):
    user_input = message['text']
    result = graph.invoke({"message": user_input})
    say(result["message"])

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
