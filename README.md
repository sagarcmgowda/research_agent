# 🤖 Autonomous Research Agent

An **AI-powered research agent** built in Python to generate structured, factual, and up-to-date reports on complex topics by leveraging the power of **Google's Gemini models** and the **Tavily Search API**.

---

## ✨ Features
- **Dynamic Research**: Accepts a research question as a command-line input for maximum flexibility.  
- **Real-Time Data**: Gathers the most recent and relevant information using the Tavily Search API.  
- **Advanced Generation**: Utilizes the Gemini API for high-quality, structured analysis and report writing.  
- **Dependency Check**: Automatically validates required API keys (`GOOGLE_API_KEY` or `GEMINI_API_KEY`, and `TAVILY_API_KEY`).  
- **Structured Output**: Generates a clean, formatted research report directly in your terminal.  

---

## 🚀 Installation & Setup

### ✅ Prerequisites
- Python **3.10+**
- API keys from:
  - [Google AI Studio / Google Cloud](https://aistudio.google.com/) (Gemini API key)
  - [Tavily AI](https://tavily.com/) (Tavily API key)

---

### Step 1: Clone the Repository
```bash
git clone https://github.com/sagarcmgowda/research_agent.git
cd research_agent
```
---

### Step 2: Create a Virtual Environment
It's best practice to use a virtual environment to manage dependencies.

```bash
# Create the environment
python -m venv .venv

# Activate (Linux/macOS)
source .venv/bin/activate

# Activate (Windows CMD)
.\.venv\Scripts\activate.bat

# Activate (Windows PowerShell)
.\.venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies
Make sure your requirements.txt includes packages such as:
google-genai, langchain-community, pydantic, tavily-python, python-dotenv
```bash
pip install -r requirements.txt
```
### tep 4: Set API Keys
The agent requires two API keys. You can set them as environment variables:

Windows (Command Prompt):
```bash
set GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```
```bash
set TAVILY_API_KEY=YOUR_TAVILY_API_KEY
```

### 🛠️ Usage

Run the agent via main.py.
```bash
python main.py
```

## Example Run

(.venv) C:\path\to\research_agent>python main.py
```bash
==================================================
WELCOME TO THE AI RESEARCH AGENT
==================================================
Enter your research question: Analyze the current regulatory landscape (e.g., EU's AI Act, US executive orders) governing the deployment of Generative AI models and detail the primary compliance challenges faced by large technology companies.
--------------------------------------------------
**Research Question:** Analyze the current regulatory landscape (e.g., EU's AI Act, US executive orders) governing the deployment of Generative AI models and detail the primary compliance challenges faced by large technology companies.
--------------------------------------------------
... (Agent performs research, search, and generation) ...

==================================================
**FINAL STRUCTURED RESEARCH REPORT**
==================================================
... (The detailed report output will appear here) ...
==================================================
```
