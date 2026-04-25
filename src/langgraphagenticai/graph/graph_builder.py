from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.ai_news_node import AI_News_Node


class GraphBuilder:
    def __init__(self, model):
        self.llm= model
        self.graph_buider = StateGraph(State)

    def ai_news_builder_graph(self):
        
        ai_news_node= AI_News_Node(self.llm)
        # Added the nodes
        self.graph_buider.add_node("fetch_news",ai_news_node.fetch_news)
        self.graph_buider.add_node("summarize_news",ai_news_node.summarize_news)
        self.graph_buider.add_node("save_results",ai_news_node.save_results)
        # Added the edges
        self.graph_buider.set_entry_point("fetch_news")
        self.graph_buider.add_edge("fetch_news","summarize_news")
        self.graph_buider.add_edge("summarize_news","save_results")
        self.graph_buider.add_edge("save_results", END)
        
    def setup_graph(self):
        self.ai_news_builder_graph()
        return self.graph_buider.compile()
