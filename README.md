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
git clone [<YOUR_REPOSITORY_URL>](https://github.com/sagarcmgowda/research_agent.git)
cd research_agent
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
