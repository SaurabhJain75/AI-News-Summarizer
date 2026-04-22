from tavily imort TavilyClient
from langchain_core.prompts import ChatPromptTemplate

class AI_News_Node:
    def __init__(self, llm):
        """
        Initialize the AI News Node with API keys for Tavily and Groq
        """
        self.llm = llm
        self.tavily= TavilyClient()
        # this is used to capture various steps in the file so that later can be use for steps shown
        self.state= {}
        
    def fetch_news(self, state: dict) -> dict:
        """
        Fetch AI news based on the specified frequency.
        
        Args:
            state (dict): The state dictionary containing the frequency.
            
        Returns:
            dict: Updated state with 'news_data' key containing the fetched news.
        """
        
        
    def summarize_news(self, state: dict) -> dict:
        """
        Summarize the fetched news using an llm.
        
        Args:
            state (dict): The state dictionary containing 'news_data'.
            
        Returns:
            dict: Updated state with 'summary' key containing the summarized news.
        """
        
        news_items= self.state["news_data"]
        
        prompt_template= ChatPromptTemplate.from_messages([
            ("system", """Summarize AI news articles into markdown format. For each item include:
             - Date in **YYYY-MM-DD** format in the IST timezone
             - Concise sentences summary form the latest news
             - Source news by date wise (latest first)
             Use format:
             ### [Date]
             - [Summary](URL)"""),
            ("user", "Articles:\n{articles}")
        ])
        
        articles_str= "\n\n".join([
            f"Content: {item.get('content', '')}\nURL: {item.get('url', '')}\nDate: {item.get('published_date', '')}" 
            for item in news_items
        ])
        
        response= self.llm(prompt_template.format(articles=articles_str))
        state["summary"]= response.content
        self.state["summary"]= state["summary"]
        return self.state
    
    def save_results(self, state: dict) -> dict:
        frequency= self.state["frequency"]
        summary= self.state["summary"]
        filename= f"ai_news/{frequency}_summary.md"
        with open(filename, "w") as f:
            f.write(f"# {frequency.capitalize()} AI News Summary\n\n")
            f.write(summary)
        self.state["filename"]= filename
        return self.state