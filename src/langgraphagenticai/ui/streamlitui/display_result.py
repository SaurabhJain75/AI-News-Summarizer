import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json

class DisplayResultStreamlit:
    def __init__(self, graph, user_message):
        self.graph= graph
        self.user_message= user_message
    
    def display_result_on_ui(self):
        # graph= self.graph
        # user_message=self.user_message
        print(self.user_message)
        frequency= self.user_message
        with st.spinner("Fetching and summarizing news... ⌛"):
            result= self.graph.invoke({"messages":frequency})
            try:
                #Read the markdown file
                AI_NEWS_PATH= f"./ai_news/{frequency.lower()}_summary.md"
                with open(AI_NEWS_PATH, "r") as file:
                    markdown_content= file.read()
                    
                #Display the markdown content in streamlit
                st.markdown(markdown_content, unsafe_allow_html=True)
            except FileNotFoundError:
                st.error(f"News Not Generated or File not found: {AI_NEWS_PATH}")
            except Exception as e:
                st.error(f"An error occured: {str(e)}")
        