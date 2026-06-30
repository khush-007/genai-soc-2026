# 🚀 PromptForge

PromptForge is a Multi-Persona AI Assistant built using Gradio and Groq API. The application allows users to interact with different AI personalities, receive real-time streaming responses, perform structured code reviews, and manage multiple chat sessions with conversation memory.

---

# ✨ Features

## 🎭 Multiple AI Personas

PromptForge includes the following AI personas:

* 🔬 Technical Explainer
* 💻 DSA Mentor
* 🗣️ Debate Coach
* ✍️ Creative Writer
* 🔍 Code Reviewer

Each persona uses a dedicated system prompt and few-shot examples to generate specialized responses.

---

## ⚡ Real-Time Streaming

Responses are streamed token-by-token, providing a smooth ChatGPT-like user experience.

---

## 🧠 Conversation Memory

The assistant remembers previous messages and maintains context throughout the conversation.

---

## 💬 Multi-Chat History

Users can:

* Create multiple chat sessions
* Switch between conversations
* Maintain separate chat histories
* Continue previous discussions anytime

---

## 🔍 Structured Code Review

The Code Reviewer persona provides:

* Summary
* Issues Found
* Suggestions
* Severity Analysis
* Complexity Insights

using structured JSON parsing and markdown formatting.

---

## 🎛️ Custom Controls

* Persona Selection
* Temperature Adjustment
* Active System Prompt Viewer
* Chat Management

---

# 🛠️ Tech Stack

* Python
* Gradio
* Groq API
* Llama Models
* JSON Parsing
* Prompt Engineering

---

# 📂 Project Structure

```text
week1-promptforge/

├── app.py
├── personas.py
├── llm.py
├── utils.py
├── formatter.py
├── config.py
├── requirements.txt
├── .env.example
├── README.md

└── screenshots/
    ├── technical_explainer.png
    ├── dsa_mentor.png
    ├── debate_coach.png
    ├── creative_writer.png
    ├── code_reviewer.png
    └── multichat.png
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone <your-github-repository-url>
cd week1-promptforge
```

## Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama-3.3-70b-versatile
```

---

# ▶️ Run Project

```bash
python app.py
```

The Gradio application will start locally in your browser.

---

# 📸 Screenshots

## 🔬 Technical Explainer

![Technical Explainer](screenshots/technical_explainer.png)

---

## 💻 DSA Mentor

![DSA Mentor](screenshots/dsa_mentor.png)

---

## 🗣️ Debate Coach

![Debate Coach](screenshots/debate_coach.png)

---

## ✍️ Creative Writer

![Creative Writer](screenshots/creative_writer.png)

---

## 🔍 Code Reviewer

![Code Reviewer](screenshots/code_reviewer.png)

---

## 💬 Multi Chat History

![Multi Chat History](screenshots/multichat.png)

---

# 🔮 Future Improvements

* Export Chat
* Rename Chat Sessions
* Delete Chat Sessions
* Persistent Chat Storage
* File Upload Support
* Theme Switching
* Hugging Face Deployment
* Voice Input Support

---

# 👨‍💻 Author

**Khush Hingrajiya**

Built as a Prompt Engineering and Generative AI project using Gradio and Groq API.

---

# ⭐ Acknowledgements

* Gradio
* Groq
* Llama Models
* Open Source AI Community
