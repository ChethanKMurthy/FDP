import streamlit as st
import spacy
import nltk
import PyPDF2
from transformers import pipeline

# Download required resources
nlp_spacy = spacy.load("en_core_web_sm")
nltk.download('punkt')

# Load HuggingFace summarizer
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# UI title
st.set_page_config(page_title="Faculty Text Analyzer", layout="wide")
st.title("📘 Faculty Text Analyzer - NLP Toolkit for Educators")
st.markdown("Upload a **research paper (PDF)** or paste any text below to analyze it using core NLP tasks.")

# PDF Upload
uploaded_file = st.file_uploader("📄 Upload Research Paper (PDF)", type="pdf")
text_input = ""

# Extract from PDF
if uploaded_file is not None:
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text_list = [page.extract_text() for page in pdf_reader.pages]
        text_input = "\n".join(text_list)
        st.success("✅ Text extracted from PDF successfully!")
    except Exception as e:
        st.error(f"❌ Error reading PDF: {e}")
else:
    # Manual text input fallback
    text_input = st.text_area("📋 Or paste your own text below:", height=250)

# Run Analysis
if st.button("🔍 Run NLP Analysis"):
    if not text_input.strip():
        st.warning("Please upload a PDF or enter some text to analyze.")
    else:
        doc = nlp_spacy(text_input)

        with st.expander("🧩 Tokenization"):
            tokens = [token.text for token in doc]
            st.write(tokens)

        with st.expander("🧠 Lemmatization"):
            lemmas = [(token.text, token.lemma_) for token in doc]
            st.write(lemmas)

        with st.expander("🖋️ Part-of-Speech (POS) Tagging"):
            pos_tags = [(token.text, token.pos_, token.tag_) for token in doc]
            st.write(pos_tags)

        with st.expander("🧾 Named Entity Recognition (NER)"):
            if doc.ents:
                entities = [(ent.text, ent.label_) for ent in doc.ents]
                st.write(entities)
            else:
                st.info("No named entities detected in the text.")

        with st.expander("📌 Text Summarization"):
            if len(text_input.split()) > 50:
                try:
                    summary = summarizer(text_input, max_length=150, min_length=30, do_sample=False)
                    st.success("Summary:")
                    st.write(summary[0]["summary_text"])
                except Exception as e:
                    st.warning(f"❌ Summarization failed: {e}")
            else:
                st.info("The text is too short for summarization (minimum ~50 words).")

        # Optional future enhancement:
        # with st.expander("💬 Sentiment Analysis"):
        #   sentiment_pipeline = pipeline("sentiment-analysis")
        #   result = sentiment_pipeline(text_input[:512])  # Limit tokens
        #   st.json(result)

        st.success("✅ NLP analysis completed!")
