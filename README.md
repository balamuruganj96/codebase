# 🤖 Azure OpenAI Streamlit Chatbot

This repository contains a **Streamlit-based chatbot application** powered by **Azure OpenAI** and **LangChain**.
The app supports conversational chat, maintains session history, and displays **token usage statistics** for each response.

---

## 🚀 Features

* 💬 Interactive chat UI using Streamlit
* 🔐 Secure configuration using `.env`
* 🧠 Azure OpenAI integration via LangChain
* 🗂️ Persistent chat history (session-based)
* 🧮 Token usage tracking (prompt, completion, total)
* 📊 Token usage summary panel

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Azure OpenAI**
* **LangChain**
* **python-dotenv**


## 🔐 Environment Variables

Create a `.env` file in the project root and add your Azure OpenAI credentials:

```env
AZURE_OPENAI_API_KEY=your_azure_openai_api_key
```

> ⚠️ **Do not commit `.env` to GitHub**

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/azure-openai-streamlit-chatbot.git
cd azure-openai-streamlit-chatbot
```

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Streamlit app using:

```bash
streamlit run additional_streamlit.py
```

Once running, open the browser at:

```
http://localhost:8501
```

---

## ⚙️ Azure OpenAI Configuration

The application is configured with Azure OPEN AI.
Ensure:

* The deployment name exists in your Azure OpenAI resource
* The API version matches your Azure configuration
* Your API key is valid and active

---

## 🧮 Token Usage Tracking

Each assistant response displays:

* **Prompt tokens**
* **Completion tokens**
* **Total tokens**

A cumulative summary is available under:

> 📊 **Token Usage Summary** (Expandable panel)

---

## 🧠 Session Behavior

* Chat history is preserved **within the same browser session**
* Refreshing the page will reset the conversation
* System prompt initializes the assistant as:

  > *"You are a helpful AI assistant."*

---

## 📌 Notes & Limitations

* This app is intended for **POC / demo use**
* Not optimized for high concurrency
* Token tracking depends on Azure OpenAI metadata availability

---

## 📜 License

This project is licensed under the **MIT License**.
Feel free to use, modify, and distribute.

---

## 🙌 Acknowledgements

* [Streamlit](https://streamlit.io/)
* [LangChain](https://www.langchain.com/)
* [Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/)

