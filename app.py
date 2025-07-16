import streamlit as st
from streamlit_chat import message
import cohere
from PyPDF2 import PdfReader
import os
import tempfile
import speech_recognition as sr
from pydub import AudioSegment
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# Initialize Cohere client
co = cohere.Client(COHERE_API_KEY)

# App title
st.set_page_config(page_title="LearnMate AI", layout="wide")
st.title("🤖 LearnMate AI")

# Navigation menu
page = st.sidebar.radio("Navigation", ["Chat", "Voice Input", "Summarization", "PDF Q&A"])

# --------------------- Chat ---------------------
if page == "Chat":
    st.header("💬 Chat with AI")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("You:", key="chat_input")
    if user_input:
        st.session_state.chat_history.append({"role": "USER", "message": user_input})
        try:
            response = co.chat(
                message=user_input,
                chat_history=st.session_state.chat_history[:-1],  # history except current
                temperature=0.7,
            )
            bot_message = response.text
            st.session_state.chat_history.append({"role": "CHATBOT", "message": bot_message})
        except Exception as e:
            bot_message = f"Error: {str(e)}"
            st.session_state.chat_history.append({"role": "CHATBOT", "message": bot_message})

    for msg in st.session_state.chat_history:
        message(msg["message"], is_user=(msg["role"] == "USER"))

# --------------------- Voice Input ---------------------
elif page == "Voice Input":
    st.header("🎙️ Voice Input")

    audio_file = st.file_uploader("Upload a WAV audio file", type=["wav"])
    if audio_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            tmp_file.write(audio_file.read())
            tmp_filename = tmp_file.name

        recognizer = sr.Recognizer()
        with sr.AudioFile(tmp_filename) as source:
            audio = recognizer.record(source)

        try:
            transcription = recognizer.recognize_google(audio)
            st.success(f"Transcription: {transcription}")
            response = co.chat(message=transcription)
            st.write("AI Response:", response.text)
        except sr.UnknownValueError:
            st.error("Could not understand the audio.")
        except sr.RequestError as e:
            st.error(f"Speech recognition error: {e}")

# --------------------- Summarization ---------------------
elif page == "Summarization":
    st.header("📝 Summarize Text")
    long_text = st.text_area("Paste long text here:", height=300)
    if st.button("Summarize"):
        if len(long_text.strip()) < 250:
            st.warning("Text must be at least 250 characters.")
        else:
            try:
                response = co.summarize(text=long_text)
                st.subheader("Summary:")
                st.write(response.summary)
            except Exception as e:
                st.error(f"Summarization Error: {e}")

# --------------------- PDF Q&A ---------------------
elif page == "PDF Q&A":
    st.header("📄 PDF Q&A")

    uploaded_pdf = st.file_uploader("Upload a PDF file", type="pdf")
    question = st.text_input("Ask a question about the PDF content:")

    def extract_pdf_text(file):
        reader = PdfReader(file)
        return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())

    def pdf_qa(text, question):
        # Chunk or trim long PDFs if needed (e.g. 2000 tokens max)
        prompt = f"{text[:3000]}\n\nQuestion: {question}"
        response = co.chat(message=prompt)
        return response.text

    if uploaded_pdf:
        pdf_text = extract_pdf_text(uploaded_pdf)
        st.subheader("Extracted Text")
        st.text_area("PDF Content", pdf_text[:2000], height=300)

        if st.button("Get Answer"):
            if question:
                try:
                    answer = pdf_qa(pdf_text, question)
                    st.subheader("Answer:")
                    st.write(answer)
                except Exception as e:
                    st.error(f"Error while getting answer: {e}")
            else:
                st.warning("Please enter a question.")
