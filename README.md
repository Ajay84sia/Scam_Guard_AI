🛡️ ScamGuard AI

AI-powered scam detection using Google Gemini, Python, and Streamlit.

Detect scams, identify intent, and explain why a message is suspicious.

<p align="center">
  <a href="https://scamdetect.streamlit.app/" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/🚀%20Live%20Demo-Streamlit-FF4B4B?logo=streamlit&logoColor=white" alt="Live Demo">
  </a>
  <a href="https://github.com/Ajay84sia/Scam_Guard_AI" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/💻%20GitHub-Repository-181717?logo=github&logoColor=white" alt="GitHub">
  </a>
</p>

🚨 Problem

Scammers use urgency, impersonation, phishing links, OTP requests, fake rewards, and other social-engineering techniques. Simple keyword-based systems often fail when the wording changes.

ScamGuard AI uses an LLM to understand the context and intent of a message instead of relying only on keywords.

✨ Features

🚨 Scam / Not Scam / Uncertain classification

🎯 Intent detection

⚠️ Risk factor identification

🧠 Explainable reasoning

📊 CSV batch analysis

📈 Dataset evaluation

🧠 How It Works

User Message
     ↓
Prompt Builder
     ↓
Google Gemini
     ↓
Output Parser
     ↓
Structured Result
     ↓
Streamlit UI

Output:

Label
Intent
Reasoning
Risk Factors

🛠️ Tech Stack

Python 3.11+

Google Gemini / GenAI

Streamlit

Pandas

Pydantic

python-dotenv

## 📁 Project Structure

```text
Scam_Guard_AI/
│
├── llm/
│   └── client.py
│
├── pipeline/
│   └── scam_detector/
│       ├── builder.py
│       ├── detector.py
│       ├── executor.py
│       └── parser.py
│
├── streamlit/
│   └── app.py
│
├── config.py
├── evaluate.py
├── main.py
├── requirements.txt
└── README.md
```

🚀 Run Locally

git clone https://github.com/Ajay84sia/Scam_Guard_AI.git
cd Scam_Guard_AI

python -m venv venv
source venv/Scripts/activate

pip install -r requirements.txt

Create .env:

GEMINI_API_KEY=your_api_key
GEMINI_MODEL=your_model

Run:

streamlit run streamlit/app.py


🔮 Future Improvements

Multi-language detection

URL/domain reputation analysis

Image/screenshot scam detection

Browser extension

REST API

Confidence scoring

<p align="center">
  🛡️ <strong>ScamGuard AI — Detect smarter. Stay safer.</strong>
</p>
