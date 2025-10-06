from typing import List, TypedDict
from langchain_ollama import ChatOllama
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.graph import StateGraph, END
from dotenv import load_dotenv

load_dotenv()
search_tool = DuckDuckGoSearchRun()
llm = ChatOllama(model="llama3", temperature=0)

class GraphState(TypedDict):
    topic: str
    plan: str
    search_results: List[str]
    report: str
    critique_decision: str

def planner_node(state: GraphState): # ... (same as before)
    print("--- 📝 Generating Plan ---")
    prompt = f"Create a concise, step-by-step research plan for the topic: {state['topic']}"
    response = llm.invoke(prompt)
    return {"plan": response.content}
def search_node(state: GraphState): # ... (same as before)
    print(f"--- 🔍 Searching for: {state['plan']} ---")
    search_result = search_tool.run(state['plan'])
    return {"search_results": [search_result]}
def critique_node(state: GraphState): # ... (same as before)
    print("--- 🤔 Critiquing Search Results ---")
    prompt = f"Is this search result sufficient to write a report on {state['topic']}? Result: {state['search_results']}. Answer 'yes' or 'no'."
    response = llm.invoke(prompt)
    decision = response.content.strip().lower()
    return {"critique_decision": decision}
def writer_node(state: GraphState): # ... (same as before)
    print("--- ✍️ Writing Final Report ---")
    prompt = f"Synthesize a comprehensive report on {state['topic']} using the following data: {state['search_results']}"
    response = llm.invoke(prompt)
    return {"report": response.content}
def should_continue(state: GraphState): # ... (same as before)
    return "write" if state["critique_decision"] == "yes" else "end"

workflow = StateGraph(GraphState)
workflow.add_node("planner", planner_node)
workflow.add_node("search", search_node)
workflow.add_node("critique", critique_node)
workflow.add_node("writer", writer_node)
workflow.set_entry_point("planner")
workflow.add_edge("planner", "search")
workflow.add_edge("search", "critique")
workflow.add_conditional_edges("critique", should_continue, {"write": "writer", "end": END})
workflow.add_edge("writer", END)
app = workflow.compile()