# 🕷️ AI Web Scraper

An AI-powered web scraping application that extracts and intelligently parses website content using **local LLMs**. Built with Python, Selenium, BeautifulSoup, Streamlit, and Ollama for completely **free, offline processing**.

## ✨ Features

- **🌐 Web Scraping**: Scrape any website URL using Selenium
- **🧹 Content Cleaning**: Automatically remove scripts, styles, and clean HTML
- **🤖 AI-Powered Parsing**: Use Ollama LLMs to extract specific information from scraped content
- **📝 DOM Content Viewer**: View and inspect extracted DOM content
- **💻 Web Interface**: Simple and intuitive Streamlit UI
- **🔓 100% Free**: No API keys, no paid services - runs completely locally

## 🛠️ Tech Stack

- **Python 3.14+**
- **Selenium** - Web automation & scraping
- **BeautifulSoup** - HTML parsing and cleaning
- **Streamlit** - Web interface
- **LangChain** - LLM integration
- **Ollama** - Local LLM inference (Qwen 2.5 3B model)

## 📋 Prerequisites

- Python 3.10+
- Google Chrome (for Selenium)
- Ollama installed locally ([download here](https://ollama.ai))
- 4GB+ RAM for running the Qwen 2.5 3B model

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/Saket-code40/Web_Scrapper_ai.git
cd Web_Scrapper_ai
```

### Step 2: Set Up Python Virtual Environment

```bash
# Create virtual environment
python -m venv aiweb

# Activate virtual environment
# On Linux/Mac:
source aiweb/bin/activate
# On Windows:
aiweb\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Install and Set Up Ollama

1. **Download Ollama** from [ollama.ai](https://ollama.ai)
2. **Install** following the official guide for your OS
3. **Download the Qwen 2.5 3B model**:
   ```bash
   ollama pull qwen2.5:3b
   ```

### Step 5: Create Environment File

```bash
# Copy the example
cp .env.example .env

# .env is already configured for local Ollama
# No API keys needed!
```

## 🎯 Usage

### Step 1: Start Ollama Server

Open a terminal and keep it running:

```bash
ollama serve
```

This starts the Ollama server on `http://localhost:11434`

### Step 2: Start the Web App

In another terminal:

```bash
cd /path/to/Web_Scrapper_ai
source aiweb/bin/activate
streamlit run main.py
```

The app will open at `http://localhost:8501`

### Step 3: Use the App

1. **Enter a URL** - Paste the website you want to scrape
2. **Enter parse description** - Describe what information you want to extract
3. **Click "Scrape"** - The app will:
   - Scrape the website using Selenium
   - Extract the body content
   - Clean HTML tags and scripts
   - Split content into chunks
   - Use Qwen 2.5 to extract the requested information

## 📁 Project Structure

```
Web_Scrapper_ai/
├── main.py                 # Streamlit app entrypoint
├── scrape.py              # Scraping functions using Selenium
├── parse.py               # LLM parsing with Ollama
├── requirements.txt       # Python dependencies
├── .env.example          # Example environment variables
├── .gitignore            # Git ignore file
├── README.md             # This file
├── chromedriver          # Selenium Chrome driver
└── aiweb/                # Python virtual environment
```

## 🔧 Configuration

### Model Selection

To use a different Ollama model, edit [parse.py](parse.py):

```python
model = OllamaLLM(
    model="your-model-here",  # Change this
    temperature=0
)
```

Available models: `qwen2.5:3b`, `mistral`, `llama2`, etc.

Run `ollama list` to see installed models or `ollama pull <model-name>` to download new ones.

### Selenium Configuration

Edit [scrape.py](scrape.py) to change Chrome options:

```python
options.binary_location = "/usr/bin/google-chrome"  # Path to Chrome
```

## 📊 How It Works

```
User Input (URL + Description)
        ↓
Selenium scrapes website
        ↓
BeautifulSoup extracts body content
        ↓
Cleans HTML, removes scripts/styles
        ↓
Split into 1000-char chunks
        ↓
Ollama processes each chunk with Qwen 2.5
        ↓
Results displayed in Streamlit UI
```

## ⚡ Performance

- **First run**: ~5-10 seconds (model loads into memory)
- **Subsequent requests**: ~2-5 seconds per chunk
- **Memory usage**: ~3-4 GB RAM for Qwen 2.5 3B model

## 📚 Requirements

Full dependency list in [requirements.txt](requirements.txt):

- streamlit
- selenium
- beautifulsoup4
- langchain
- langchain-ollama
- langchain-text-splitters
- python-dotenv

## 🚨 Troubleshooting

### "Model not found" Error
- Make sure Ollama is running: `ollama serve`
- Verify model is installed: `ollama list`
- Pull model if needed: `ollama pull qwen2.5:3b`

### Slow Performance
- Close other applications to free up RAM
- Use a lighter model: `ollama pull phi`
- Reduce chunk size in [parse.py](parse.py)

### Connection Refused
- Ensure Ollama server is running (`ollama serve`)
- Check if running on correct port (default: 11434)

### Chrome Driver Issues
- Update chromedriver to match your Chrome version
- Or remove chromedriver and let Selenium handle it automatically

## 🔮 Future Improvements

- [ ] CSV/Excel export functionality
- [ ] Multi-page crawling and following links
- [ ] RAG-based website chatbot
- [ ] Caching for faster repeated queries
- [ ] Deployment templates (Docker, Streamlit Cloud)
- [ ] Support for more LLM providers
- [ ] Advanced scraping options (JavaScript rendering, authentication)

## 📝 License

MIT License - feel free to use this project for personal and commercial purposes

## 👨‍💻 Author

**Saket Sharma**
- GitHub: [@Saket-code40](https://github.com/Saket-code40)
- Project: [Web_Scrapper_ai](https://github.com/Saket-code40/Web_Scrapper_ai)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs via GitHub Issues
- Submit pull requests with improvements
- Suggest new features

## 💡 Tips

- Start with simple URLs for testing (e.g., news articles)
- Be specific in your parse description for better results
- Test with different Ollama models for different use cases
- Monitor Ollama memory usage for large scraping jobs

