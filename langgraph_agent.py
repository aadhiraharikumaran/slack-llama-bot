from langchain.llms import HuggingFaceHub
from langgraph.graph import StateGraph, END

def run_llama_agent(message):
    llm = HuggingFaceHub(repo_id="meta-llama/Llama-2-7b-chat-hf", model_kwargs={"temperature":0.5})
    return llm(message)

# Graph node
def start(state):
    message = state["message"]
    response = run_llama_agent(message)
    return {"message": response}

# Set up LangGraph
def get_graph():
    workflow = StateGraph(input_schema={"message": str})
    workflow.add_node("start", start)
    workflow.set_entry_point("start")
    workflow.set_finish_point("start")
    return workflow.compile()
