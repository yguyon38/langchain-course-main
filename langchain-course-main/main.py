from dotenv import load_dotenv
import os

load_dotenv()  # Loads environment variables from .env
print("DEBUG - TAVILY_API_KEY:", os.getenv("TAVILY_API_KEY"))
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_tavily import TavilySearch
from langchain_openai import ChatOpenAI

# Initialize Tavily tool using the environment variable
tavily_tool = TavilySearch(
    tavily_api_key=os.getenv("TAVILY_API_KEY")
)

tools = [tavily_tool]

# Initialize LLM
llm = ChatOpenAI(model="gpt-4")

# Load ReAct prompt
react_prompt = hub.pull("hwchase17/react")


# Create the agent
agent = create_react_agent(llm=llm, tools=tools, prompt=react_prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

def main():
    print("Agent running...")
    result = executor.invoke({"input": "What is LangChain and who created it?"})
    print(result["output"])

if __name__ == "__main__":
    main()
