# agent.py
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool

# --- Tool Definitions ---

# Tavily web search tool
tavily_search_tool = TavilySearch(max_results=3)

@tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers and returns the result."""
    return a * b

# List of tools the agent can use
TOOLS = [tavily_search_tool, multiply]


class ResearchAgent:
    """
    A LangChain Agent dedicated to research, initialized with the necessary LLM,
    tools, and prompt to execute complex queries.
    """
    def __init__(self):
        # --- 1. Initialize LLM ---
        # NOTE: The GOOGLE_API_KEY environment variable is automatically detected by the SDK
        try:
            self.llm = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash", 
                temperature=0
            )
        except Exception as e:
            print(f"Error initializing LLM: {e}")
            raise EnvironmentError("Please ensure your GOOGLE_API_KEY is set as an environment variable.") from e

        # --- 2. Define the Agent Prompt ---
        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "You are a helpful and extremely powerful AI assistant. You must use the available tools to answer factual questions. If a math calculation is needed, use the multiply tool. Structure your final answer into clear sections."),
                ("human", "{input}"),
                ("placeholder", "{agent_scratchpad}"),
            ]
        )

        # --- 3. Create the Agent and Executor ---
        self.agent = create_tool_calling_agent(self.llm, TOOLS, self.prompt)
        self.agent_executor = AgentExecutor(
            agent=self.agent, 
            tools=TOOLS, 
            verbose=True # Set to True to see the agent's internal Thought/Action loop
        )

    def run_research(self, query: str) -> str:
        """Invokes the agent executor with a given query."""
        try:
            # The agent_executor takes a dictionary with an 'input' key
            result = self.agent_executor.invoke({"input": query})
            return result["output"]
        except Exception as e:
            print(f"An error occurred during agent execution: {e}")
            return f"Agent execution failed: {e}"

# --- Test Cases (Optional, now inside a dedicated block) ---
def run_test_cases():
    """Runs the original test cases for the ResearchAgent."""
    try:
        agent_tester = ResearchAgent()

        queries = [
            "What is the current capital of Australia and what is the biggest country by area?",
            "What is the result of 150 times 45?",
            "Hello! How can you help me today?"
        ]
        
        for query in queries:
            print(f"\n>>> Running Agent Test for: '{query}'")
            print("-" * 30)
            result = agent_tester.run_research(query)
            print("--- Final Answer ---")
            print(result)
            print("---------------------\n")
            
    except EnvironmentError as e:
        print(f"Skipping test cases due to missing environment key: {e}")


if __name__ == "__main__":
    # If you want to run the test cases from this file, uncomment the line below:
    # run_test_cases()
    print("Agent class defined successfully. Run main.py to execute the research project.")