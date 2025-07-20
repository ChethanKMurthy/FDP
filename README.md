<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# rewrite the markdown file with the repo link and create a seperate requirements.txt file to upload https://github.com/ChethanKMurthy/FDP

```markdown
# 📘 Faculty Text Analyzer

A user-friendly, interactive web app that empowers **non-CSE faculty** to explore essential Natural Language Processing (NLP) tasks including research paper summarization, named entity recognition (NER), lemmatization, tokenization, part-of-speech (POS) tagging, and PDF text extraction.

Built for Faculty Development Programmes (FDPs), this project makes NLP powerful, accessible, and interactive via a no-code, single-click interface using **Streamlit** and modern NLP libraries.

**GitHub Repository:**  
[https://github.com/ChethanKMurthy/FDP](https://github.com/ChethanKMurthy/FDP)

---

## 🚀 Features

- 📄 **PDF Upload:** Analyze research papers and academic documents as PDFs
- 🧠 **NLP Analysis:** Tokenization, Lemmatization, POS Tagging, Named Entity Recognition (NER)
- 🔍 **AI Summarization:** Generate concise summaries with transformer models
- 🕹️ **Interactive UI:** Built with Streamlit for ease of use
- 🔐 **Offline-Ready:** Run locally with no internet required after setup

---

## 🧰 Technologies Used

| Tool         | Purpose                         |
|--------------|---------------------------------|
| Python       | Programming Language            |
| Streamlit    | Web App Framework               |
| spaCy        | Tokenization, POS, NER          |
| nltk         | Tokenization support            |
| transformers | Summarization engine (BART)     |
| PyPDF2       | PDF Text Extraction             |

---

## 🖥️ Setup Instructions

Follow these steps to run the Faculty Text Analyzer in a **virtual environment**.

### 1. Clone the Repository

```

git clone https://github.com/ChethanKMurthy/FDP.git
cd FDP

```

### 2. Create and Activate a Virtual Environment

**On Windows:**
```

python -m venv venv
venv\Scripts\activate

```

**On macOS/Linux:**
```

python3 -m venv venv
source venv/bin/activate

```

### 3. Install Dependencies

Install required Python packages using the included `requirements.txt`:
```

pip install -r requirements.txt

```

If you want to install them manually, see the end of this README for the full list.

### 4. Run the Application

After activating your environment and installing dependencies:
```

streamlit run app.py

```

The app will open in your default browser at `http://localhost:8501`.

---

## 🚦 Usage Instructions

1. **Upload a PDF file**—upload a research paper or academic document.
2. **Or paste text** into the provided text box.
3. Click **"Run NLP Analysis"**.
4. Explore tokenization, lemmatization, POS tagging, NER, and AI-powered summarization inside expandable sections.

---

## 📂 Project Structure

```

FDP/
│
├── app.py                \# Main Streamlit app
├── requirements.txt      \# Python dependencies
├── README.md             \# Project guide \& info
└── (other files)

```

---

## ✅ Future Enhancements

- [ ] Sentiment Analysis
- [ ] Multilingual Support
- [ ] Download analysis results as PDF/CSV
- [ ] Keyword Extraction

---

## 📚 Example NLP Tasks Explained

| Task                 | Description                                  | Educational Use                      |
|----------------------|----------------------------------------------|--------------------------------------|
| Lemmatization        | Finds root word forms                        | Text simplification                  |
| POS Tagging          | Labels word types (noun, verb, etc.)         | Grammar/linguistics insights         |
| NER                  | Detects names, organizations, locations, etc.| Research, document mining            |
| Summarization        | AI creates short, readable summaries         | Research, feedback, lesson prep      |

---

## 🙋 For FDP Use

This tool is suitable for faculty in any field—sciences, commerce, humanities—supporting:

- Curriculum design
- Feedback analysis
- Research summary
- Content simplification

---

## 📝 License

For educational, academic, and personal use only.

---

## 🤝 Contributing

Feedback and pull requests are encouraged to further improve the application!

---

## ☎️ Support

For help or suggestions, please contact [Your Name/Institution/Email].

---

# requirements.txt

Below is a standard requirements file suitable for uploading to the repository:

```

streamlit
spacy
nltk
transformers
torch
sumy
PyPDF2

```

**Post-installation instructions:**
After running `pip install -r requirements.txt`, run the following commands to install required models:

```

python -m nltk.downloader punkt
python -m spacy download en_core_web_sm

```
```

<div style="text-align: center">⁂</div>

[^1]: https://github.com/ChethanKMurthy/FDP

