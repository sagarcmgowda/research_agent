# main.py
from agent import ResearchAgent
import os
import sys

def run_project():
    # Check for GOOGLE_API_KEY as the Gemini SDK prefers it, but checking for
    # the requested GEMINI_API_KEY is also a good practice.
    if not os.environ.get("GOOGLE_API_KEY") and not os.environ.get("GEMINI_API_KEY"):
        print("ERROR: Please set the GOOGLE_API_KEY or GEMINI_API_KEY environment variable.")
        print("Run: set GOOGLE_API_KEY=YOUR_API_KEY (Windows cmd) or export GOOGLE_API_KEY=YOUR_API_KEY (Linux/Mac)")
        # Exit the program gracefully if the key is missing
        sys.exit(1)

    # Check for Tavily Key
    if not os.environ.get("TAVILY_API_KEY"):
        print("ERROR: Please set the TAVILY_API_KEY environment variable.")
        print("Run: set TAVILY_API_KEY=YOUR_API_KEY (Windows cmd) or export TAVILY_API_KEY=YOUR_API_KEY (Linux/Mac)")
        # Exit the program gracefully if the key is missing
        sys.exit(1)

    try:
        # Initialize the Agent
        agent = ResearchAgent()
    except EnvironmentError as e:
        print(f"Initialization Failed: {e}")
        return

    # --- START OF CHANGE ---
    print("\n" + "=" * 50)
    print("WELCOME TO THE AI RESEARCH AGENT")
    print("=" * 50)
    
    # PROMPT THE USER FOR THE RESEARCH QUESTION
    complex_question = input("Enter your research question: ")
    
    # Check if the user entered anything
    if not complex_question.strip():
        print("-" * 50)
        print("No research question entered. Exiting.")
        print("-" * 50)
        return
        
    print("-" * 50)
    print(f"**Research Question:** {complex_question}")
    print("-" * 50)
    # --- END OF CHANGE ---

    # Run the research
    final_report = agent.run_research(complex_question)

    print("\n" + "=" * 50)
    print("**FINAL STRUCTURED RESEARCH REPORT**")
    print("=" * 50)
    print(final_report)
    print("=" * 50)


if __name__ == "__main__":
    run_project()