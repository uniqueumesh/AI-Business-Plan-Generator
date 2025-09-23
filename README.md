# AI Business Plan Generator

An intelligent business plan generator powered by Google's Gemini AI that helps entrepreneurs and business owners create comprehensive, professional business plans through a simple, step-by-step interface.

## 🚀 Features

- **Step-by-Step Form**: Easy-to-use multi-step form interface
- **AI-Powered Generation**: Uses Google Gemini 2.5 Flash for intelligent business plan creation
- **Comprehensive Sections**: Covers all essential business plan components
- **User-Friendly Design**: Built for non-technical users
- **Download Functionality**: Export your business plan as a Markdown file
- **Real-time Validation**: Form validation with helpful error messages

## 📋 Business Plan Sections

1. **Company Overview**: Company name, business description, mission, and target market
2. **Marketing Details**: Marketing strategy, customer acquisition, and channels
3. **Competitor Information**: Competitive analysis and unique value proposition
4. **Financial Overview**: Costs, financial strategy, and sales projections
5. **AI Generation**: Automated business plan creation with professional formatting

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key (get one at [Google AI Studio](https://makersuite.google.com/app/apikey))

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/AI-Business-Plan-Generator.git
   cd AI-Business-Plan-Generator
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Copy the example environment file
   cp env_example.txt .env
   
   # Edit .env and add your Gemini API key
   GEMINI_API_KEY=your_actual_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:8501` to use the application.

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# Required
GEMINI_API_KEY=your_gemini_api_key_here

# Optional
MAX_RETRIES=3
REQUEST_TIMEOUT=60
```

### API Key Setup

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key and add it to your `.env` file

## 📖 Usage

### Step 1: Company Overview
- Enter your company name
- Describe your business or product
- Write your mission statement
- Define your target market

### Step 2: Marketing Details
- Outline your marketing strategy
- Describe customer acquisition methods
- List marketing channels
- Add budget considerations

### Step 3: Competitor Information
- Analyze your competitors
- Highlight competitive advantages
- Define market positioning
- Explain your unique value proposition

### Step 4: Financial Overview
- Estimate expected costs
- Describe your financial strategy
- Project sales for the first year
- Outline your revenue model
- Add funding requirements if needed

### Step 5: Generate Plan
- Review your information
- Click "Generate Business Plan"
- Download your professional business plan

## 🏗️ Project Structure

```
AI-Business-Plan-Generator/
├── app.py                      # Main Streamlit application
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
├── env_example.txt            # Environment variables template
├── utils/
│   ├── __init__.py
│   ├── api_client.py          # Gemini API client
│   ├── form_validation.py     # Form validation logic
│   └── business_plan_formatter.py # Output formatting
├── README.md                  # This file
└── DEVELOPMENT_PLAN.md        # Development planning document
```

## 🔧 Technical Details

### Dependencies

- **Streamlit**: Web application framework
- **Google Generative AI**: Gemini API client
- **Python-dotenv**: Environment variable management
- **Pydantic**: Data validation

### API Configuration

- **Model**: Gemini 2.0 Flash Experimental
- **Temperature**: 0.7 (balanced creativity)
- **Max Tokens**: 4000
- **Retry Logic**: 3 attempts with exponential backoff

## 🚨 Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure your `GEMINI_API_KEY` is correctly set in the `.env` file
   - Verify the API key is valid and has proper permissions

2. **Import Errors**
   - Make sure all dependencies are installed: `pip install -r requirements.txt`
   - Check that you're using the correct Python version

3. **Form Validation Errors**
   - Complete all required fields marked with asterisks (*)
   - Ensure text areas have sufficient content

4. **Generation Errors**
   - Check your internet connection
   - Verify API key has sufficient quota
   - Try reducing the amount of text in form fields

### Getting Help

- Check the [Issues](https://github.com/yourusername/AI-Business-Plan-Generator/issues) page
- Review the development plan in `DEVELOPMENT_PLAN.md`
- Ensure all dependencies are properly installed

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Gemini AI for providing the language model
- Streamlit team for the excellent web framework
- The open-source community for inspiration and tools

## 📞 Support

For support, email support@yourcompany.com or create an issue in the GitHub repository.

---

**Made with ❤️ for entrepreneurs and business owners**
Generate comprehensive business plan with AI in simple steps.
