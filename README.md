# 📚 LearnMate AI

**LearnMate AI** is an intelligent, Streamlit-powered educational assistant designed to help users interact with PDFs, summarize content, ask questions, and more. Built with Cohere and Streamlit, this app offers a sleek interface and multiple AI-driven features for engaging with educational material in an intuitive way.

🌐 **Live App**: [learnmate-ai-1.onrender.com](https://learnmate-ai-1.onrender.com)

---

## ✨ Features

* 🧠 **AI Chat** – Engage in natural conversation using Cohere-powered responses.
* 📄 **PDF Q\&A** – Upload PDF files and ask questions about their content.
* 📝 **Summarization** – Automatically generate summaries of text using AI.
* 🎨 **Interactive UI** – Clean design with smooth animations and dynamic user experience.
* 🔒 **API Key security** – Environment variables and Streamlit secrets used for managing keys securely.

---

## 🚀 Technologies Used

* [Streamlit](https://streamlit.io/) – Frontend UI
* [Cohere](https://cohere.com/) – NLP and language processing
* [PyPDF2](https://pypi.org/project/PyPDF2/) – PDF text extraction
* [Python Dotenv](https://pypi.org/project/python-dotenv/) – Environment variable management
* [Render](https://render.com/) – Deployment platform

---

## 📂 Project Structure

```bash
├── app.py               # Main Streamlit app
├── requirements.txt     # All Python dependencies
├── .streamlit/
│   └── config.toml      # Optional Streamlit config
└── README.md            # Project documentation (this file)
```

---

## ⚙️ Installation (Local)

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/learnmate-ai.git
   cd learnmate-ai
   ```

2. **Set up environment**:

   Create a `.env` file and add your Cohere API key:

   ```
   COHERE_API_KEY=your-cohere-api-key
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**:

   ```bash
   streamlit run app.py
   ```

---

## 🛠 Deployment (Render)

**Start Command (Render settings)**:

```bash
streamlit run app.py --server.port $PORT --server.enableCORS false
```

Make sure to add your `COHERE_API_KEY` in Render under **Environment → Secret Files** or **Environment Variables**.

---

## 📎 Example Use Cases

* Students summarizing textbook chapters.
* Researchers analyzing PDF reports.
* Anyone exploring AI-powered learning.

---

## 🙌 Acknowledgements

Special thanks to:

* [Cohere](https://cohere.com/) for their amazing NLP API.
* [Streamlit](https://streamlit.io/) for making UI creation so accessible.

---

## 📫 Contact

Have feedback or suggestions?
📧 Email: [lorrieym@gmail.com](mailto:your-email@example.com)


