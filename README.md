# Finance Agent 📈

An AI-powered investment analyst agent specialized in Indian stock market analysis. Built with the [Agno framework](https://github.com/agno-labs/agno), this intelligent assistant provides comprehensive stock research, fundamental analysis, and automated trading capabilities through Zerodha Kite integration.

## 🌟 Features

- **Stock Market Analysis**: Real-time stock prices, technical indicators, and financial ratios using YFinance
- **Fundamental Analysis**: Deep dive into company financials, income statements, and analyst recommendations
- **AI-Powered Insights**: Leverages Google's Gemini Flash model with extended reasoning capabilities
- **Knowledge Base**: RAG (Retrieval Augmented Generation) system with investment lessons from MIT courses and Warren Buffett
- **Trading Integration**: Place orders on Zerodha Kite platform via MCP (Model Context Protocol)
- **Conversational Interface**: Natural language interaction with persistent memory
- **Indian Market Focus**: Specialized for NSE/BSE stocks with proper ticker format handling

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   Finance Agent                          │
├─────────────────────────────────────────────────────────┤
│  FastAPI Web Application (main.py)                      │
│  ├── Gemini Flash AI Model (8,285 token thinking)       │
│  ├── Reasoning Tools (Analysis & Critical Thinking)     │
│  ├── YFinance Tools (Market Data & Indicators)          │
│  ├── Web Tools (Research & Information Gathering)       │
│  ├── MCP Tools (Zerodha Kite Trading Integration)       │
│  └── Knowledge System (Vector DB with Investment Lessons)│
├─────────────────────────────────────────────────────────┤
│  Data Layer                                              │
│  ├── PostgreSQL + PgVector (Knowledge Embeddings)       │
│  ├── SQLite (Conversation History)                      │
│  └── File Cache (YFinance API Responses)                │
└─────────────────────────────────────────────────────────┘
```

## 📋 Prerequisites

- Python 3.8 or higher
- PostgreSQL with PgVector extension
- Google AI API key ([Get it here](https://aistudio.google.com/app/apikey))
- (Optional) Zerodha Kite account for trading features

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kamaravichow/finance-agent.git
   cd finance-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up PostgreSQL with PgVector**
   ```bash
   # Install PostgreSQL (if not already installed)
   # For Ubuntu/Debian:
   sudo apt-get install postgresql postgresql-contrib
   
   # Install PgVector extension
   # Follow instructions at: https://github.com/pgvector/pgvector
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your credentials:
   # - GOOGLE_API_KEY: Your Google AI API key
   # - DATABASE_URL: PostgreSQL connection string
   ```

5. **Sync knowledge base** (One-time setup)
   ```bash
   python sync.py
   ```
   This will process all markdown files in the `knowledge/` directory and store their embeddings in PostgreSQL.

## 🎯 Usage

### Starting the Agent

```bash
python main.py
```

The FastAPI application will start on `http://localhost:8000` with hot-reload enabled.

### Interacting with the Agent

Access the web interface or API endpoints to interact with your personal investment analyst:

**Example Queries:**
- "What is the current price of TCS (Tata Consultancy Services)?"
- "Perform a fundamental analysis of Reliance Industries (RELIANCE.NS)"
- "Show me the analyst recommendations for Infosys"
- "What are the key financial ratios for HDFC Bank?"
- "Place a buy order for 10 shares of TCS on NSE"

### Indian Stock Ticker Format

The agent is configured for Indian markets (NSE/BSE). Use the following ticker formats:
- **NSE**: `SYMBOL.NS` (e.g., `TCS.NS`, `RELIANCE.NS`, `INFY.NS`)
- **BSE**: `SYMBOL.BO` (e.g., `TCS.BO`)

## 📁 Project Structure

```
finance-agent/
├── main.py                 # Main application entry point
├── sync.py                 # Knowledge base synchronization script
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore rules
├── knowledge/             # Investment lessons and strategies (markdown)
│   ├── 1.md
│   ├── mit1.md
│   ├── mit2.md
│   ├── mit3.md
│   └── warren-buffet-lessons.md
└── yfinance_cache/        # Cached API responses (git-ignored)
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Google AI API key for Gemini model | Yes |
| `DATABASE_URL` | PostgreSQL connection string with PgVector | Yes |

### Agent Instructions

The agent is pre-configured with specialized instructions for Indian stock market analysis. You can modify these in `main.py` under the `instructions` parameter.

## 🛡️ Security Notes

- **Never commit `.env` files** to version control
- Database credentials are loaded from environment variables
- The `.gitignore` is configured to exclude sensitive files
- Review the `.env.example` for required configuration

## 📚 Knowledge Base

The agent comes with pre-loaded investment knowledge from:
- MIT OpenCourseWare on quantitative trading
- Warren Buffett investment lessons and principles
- Technical analysis fundamentals

To add more knowledge:
1. Place markdown files in the `knowledge/` directory
2. Run `python sync.py` to update the vector database

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on:
- Code style guidelines
- Development workflow
- Submitting pull requests
- Reporting issues

## 📝 License

This project is provided as-is for educational and research purposes. Please ensure compliance with:
- Google AI API Terms of Service
- YFinance data usage policies
- Zerodha Kite API terms (if using trading features)
- Securities and exchange regulations in your jurisdiction

## ⚠️ Disclaimer

**This agent is for educational and research purposes only. It does NOT provide financial advice.**

- All investment decisions should be made after consulting with qualified financial advisors
- Past performance does not guarantee future results
- Trading stocks involves risk of loss
- The creators and contributors are not responsible for any financial losses

## 🔗 Resources

- [Agno Framework Documentation](https://docs.agno.dev/)
- [Google AI Studio](https://aistudio.google.com/)
- [YFinance Documentation](https://pypi.org/project/yfinance/)
- [PgVector GitHub](https://github.com/pgvector/pgvector)
- [Zerodha Kite API](https://kite.trade/)

## 💬 Support

For issues, questions, or contributions:
- Open an issue on [GitHub Issues](https://github.com/kamaravichow/finance-agent/issues)
- Check existing documentation and README first
- Provide detailed information when reporting bugs

---

**Built with ❤️ using Agno and Google Gemini**
