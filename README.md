# AI Business Plan Generator

Create a complete, investor‑ready business plan in minutes. This Streamlit app uses Google Gemini (2.5 Flash) to turn your inputs into a professional plan you can review online and download as a PDF.

## 🚀 Features
- **Guided, 5‑step flow**: Company Overview → Marketing → Competitors → Financials → Generate
- **Built for non‑technical users**: Clear labels, examples in every field, helpful validation
- **Gemini API key input (BYOK)**: Enter your key securely in the sidebar (session‑only)
- **AI‑generated plan**: Structured, comprehensive output using proven plan sections
- **PDF download**: One‑click export to a clean, readable PDF (Markdown fallback on error)
- **Fast and private**: No server storage; data stays in your session

## 📋 Sections Collected
1. Company name, description, mission, target market
2. Marketing strategy, acquisition methods, channels, budget notes
3. Competitor overview, advantages, positioning, unique value
4. Expected costs, financial strategy, projected sales, revenue model, funding needs

## 🛠️ Setup (Local)
### Prerequisites
- Python 3.9+
- A Google Gemini API key (get one at Google AI Studio: https://makersuite.google.com/app/apikey)

### Install
```bash
git clone https://github.com/yourusername/AI-Business-Plan-Generator.git
cd AI-Business-Plan-Generator
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
# source venv/bin/activate
pip install -r requirements.txt
```

### Run
```bash
streamlit run app.py
```
Open http://localhost:8501.

### Enter your API key
- In the app sidebar, paste your Gemini API key (kept only for this session).

## 🔧 Configuration
You can optionally create a `.env` file for local defaults (the app still supports runtime key via sidebar):
```env
GEMINI_API_KEY=your_gemini_api_key_here
MAX_RETRIES=3
REQUEST_TIMEOUT=60
```
Example template: `env_example.txt`.

## 📦 Dependencies
Ensure these are present in `requirements.txt` (used by Streamlit Cloud to build the app):
```txt
streamlit>=1.28.0
google-generativeai>=0.3.0
python-dotenv>=1.0.0
pydantic>=2.0.0
requests>=2.31.0
reportlab>=4.0.0
```
- `reportlab` is required for PDF generation. Missing it will cause import errors during deploy.

## 🖥️ Deployment (Streamlit Community Cloud)
1. Push this repo to GitHub
2. Create a new Streamlit app from the repo and select `app.py`
3. Ensure `requirements.txt` contains all dependencies (including `reportlab`)
4. Configure secrets if desired (optional, since the app accepts the key in the UI)
5. Deploy. The app should build and run without OS‑level binaries

## 🧑‍💻 Usage
1. Complete each step using the examples as guidance
2. Enter your Gemini API key in the sidebar
3. Click “Generate Business Plan”
4. Review the output
5. Click “Download Business Plan (PDF)” to export

## 🧱 Project Structure
```
AI-Business-Plan-Generator/
├── app.py                         # Streamlit app (UI flow, validation, generation)
├── config.py                      # App and prompt configuration
├── requirements.txt               # Python dependencies (used by deploy)
├── env_example.txt                # Optional .env template
├── utils/
│   ├── __init__.py
│   ├── api_client.py              # Gemini client with runtime key support
│   ├── form_validation.py         # Required field checks and messages
│   ├── business_plan_formatter.py # On-screen render + download buttons
│   └── pdf_generator.py           # ReportLab PDF generation
└── README.md
```

## ⚙️ Technical Notes
- **Model**: `gemini-2.0-flash-exp` (configured in `config.py`)
- **Runtime key**: Read from sidebar; `.env` optional
- **Retries**: Exponential backoff on generation
- **PDF**: Generated with ReportLab (no external binaries required)
- **Security**: No DB; content lives in the user session. Do not paste secrets into form fields

## 🧪 Testing Guide
- Try minimal and long inputs; confirm validation and clean PDF output
- Generate with a valid key; ensure output sections are structured and readable
- Verify PDF download on Windows/macOS/iOS/Android
- Test in Chrome, Edge, Safari, Firefox; confirm mobile responsiveness

## 🆘 Troubleshooting
- Import error for `reportlab` during deploy:
  - Ensure `reportlab` is listed in `requirements.txt` and redeploy
- Generation fails:
  - Verify Gemini API key validity/quota; check network
- UI won’t proceed to next step:
  - Fill in all required fields marked with “*”

## 📄 License
MIT (see `LICENSE`).

## 🙋 Support
Open an issue on GitHub or contact the site owner.
