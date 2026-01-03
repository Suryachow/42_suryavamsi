# 🌐 Enterprise Network AI Assistant

<div align="center">

![Platform](https://img.shields.io/badge/Platform-Web-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0+-red?style=for-the-badge&logo=flask)
![AI](https://img.shields.io/badge/AI-Powered-purple?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**A modern, enterprise-grade telecom customer support platform powered by AI and RAG**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Documentation](#-documentation)

</div>

---

## 📖 About

Enterprise Network AI Assistant is an intelligent customer support system designed for telecom and network service providers. It combines **Retrieval-Augmented Generation (RAG)** with **Perplexity AI** to deliver accurate, context-aware responses from historical support data.

### 🎯 Key Highlights

- 🎨 **Modern UI** - Airtel-inspired enterprise portal with clean, professional design
- 🤖 **AI-Powered** - RAG-based knowledge retrieval with intelligent response generation
- 📊 **Smart Citations** - Source attribution with numbered references
- 🚀 **Auto Escalation** - Seamlessly hands off complex queries to human agents
- 💬 **Live Chat Widget** - Floating chat interface with real-time messaging
- 📱 **Responsive Design** - Works beautifully on all devices

---

## ✨ Features

### 🎨 Enterprise-Grade UI
- Clean, light-themed portal design
- Step-based form progression with visual indicators
- Glassmorphism effects and smooth animations
- Professional navigation and breadcrumbs
- Mobile-responsive layout

### 🤖 Intelligent Support
- **RAG-Based Retrieval**: Searches historical support logs for relevant context
- **AI Response Generation**: Uses Perplexity AI for professional, empathetic answers
- **Smart Citations**: References source documents with `[1]`, `[2]` notation
- **Auto Escalation**: Detects when human intervention is needed
- **Multi-Format Support**: Processes CSV and JSON data files

### 💬 Chat Experience
- Floating chat launcher button
- Real-time messaging interface
- Quick action chips for common queries
- Typing indicators and status updates
- Markdown rendering for rich text responses

---

## 🚀 Demo

### UI Preview
The application features a modern, step-based interface inspired by leading telecom portals:

**Main Portal**
- Clean navigation with category tabs (Individual, Business, Investors)
- Hero section with gradient background
- Progressive step cards for user onboarding
- Professional color scheme and typography

**Chat Widget**
- Floating red launcher button (bottom-right)
- Expandable chat interface
- AI-powered responses with source citations
- Escalation button for human support

---

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Perplexity API key ([Get one here](https://www.perplexity.ai/))

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/Suryachow/42_suryavamsi.git
cd 42_suryavamsi
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**

Create a `.env` file in the project root:
```env
PERPLEXITY_API_KEY=your_api_key_here
```

4. **Add your data**

Place support data files (CSV or JSON) in the `data/` folder:
```
data/
├── support_tickets.csv
├── customer_conversations.json
└── ... (your data files)
```

5. **Run the application**
```bash
python app.py
```

6. **Open your browser**
```
http://localhost:5000
```

---

## 📚 Usage

### Starting the Server
```bash
python app.py
```

The application will:
- ✅ Build/load the TF-IDF index from your data
- ✅ Start Flask server on port 5000
- ✅ Display "Server starting at http://localhost:5000"

### Using the Chat Widget

1. Click the **floating red chat button** (bottom-right corner)
2. Type your query or select a **quick action chip**
3. Receive AI-generated responses with **source citations** `[1]`, `[2]`
4. Click **"Talk to Human"** if you need to escalate

### API Integration

**POST /query**
```json
{
    "query": "Internet is slow, how to fix?",
    "api_key": "optional_override_key"
}
```

**Response**
```json
{
    "answer": "To resolve slow internet issues [1], try these steps: 1. Restart your router...",
    "context": "Retrieved context from knowledge base",
    "sources": [...],
    "escalation": false
}
```

---

## 📁 Project Structure

```
42_suryavamsi/
│
├── app.py                      # Flask application entry point
├── rag_service.py              # RAG service with TF-IDF retrieval
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (not in repo)
├── .gitignore                  # Git ignore rules
├── README.md                   # This file
├── PROJECT_README.md           # Detailed documentation
│
├── data/                       # Your support data (CSV/JSON)
│   └── tfidf_index.pkl        # Cached index (auto-generated)
│
├── templates/
│   └── index.html             # Main HTML template
│
└── static/
    ├── css/
    │   ├── style.css          # Main stylesheet
    │   ├── enhancements.css   # UI animations
    │   └── escalation.css     # Modal styles
    └── js/
        └── script.js          # Frontend JavaScript
```

---

## ⚙️ Configuration

### RAG Settings
Edit `rag_service.py`:
```python
TOP_K_RETRIEVE = 10        # Documents to retrieve
FINAL_K = 5                # Documents sent to AI
SIMILARITY_THRESHOLD = 0.1 # Minimum similarity score
MAX_CONTEXT_CHARS = 6000   # Maximum context length
```

### UI Customization
Edit `static/css/style.css`:
```css
:root {
    --primary: #e60000;           /* Brand color */
    --bg-light: #f5f7fa;          /* Background */
    --text-dark: #1a1a1a;         /* Text color */
}
```

---

## 🔧 Tech Stack

### Backend
- **Flask** - Web framework
- **scikit-learn** - TF-IDF vectorization & similarity
- **Pandas** - Data processing
- **NumPy** - Numerical operations
- **Perplexity API** - LLM for response generation

### Frontend
- **HTML5** - Structure
- **CSS3** - Modern styling with variables
- **JavaScript** - Interactivity
- **FontAwesome** - Icons
- **Marked.js** - Markdown rendering

### AI/ML
- **TF-IDF** - Document retrieval (current)
- **Perplexity Sonar** - Response generation
- **FAISS** (planned) - Semantic vector search

---

## 🎨 Design Philosophy

### Visual Principles
- ✅ **Clean & Minimal** - Ample whitespace, clear hierarchy
- ✅ **Enterprise-Grade** - Professional color palette
- ✅ **Trustworthy** - Subtle animations, polished interactions
- ✅ **Accessible** - High contrast, readable typography

### UX Patterns
- 📈 **Progressive Disclosure** - Step-by-step forms
- 👁️ **Visual Feedback** - Hover states, focus rings
- ✔️ **Status Indicators** - Completion checkmarks, pulse animations
- 🎯 **Clear Actions** - Prominent CTAs, intuitive navigation

---

## 🚨 Troubleshooting

### Common Issues

**"Perplexity API Key is missing"**
- Create `.env` file with `PERPLEXITY_API_KEY=your_key`

**Index not found or outdated**
- Delete `data/tfidf_index.pkl` and restart the app

**No documents indexed**
- Ensure data files are in `data/` folder
- Files must have text columns (conversation, text, description, etc.)

**Port 5000 already in use**
- Change port in `app.py`: `app.run(port=5001)`

---

## 🔮 Roadmap

### ✅ Completed
- [x] Enterprise UI with Airtel-style design
- [x] RAG-based document retrieval
- [x] Perplexity AI integration
- [x] Smart citation system
- [x] Auto escalation logic
- [x] Floating chat widget

### 🎯 Coming Soon
- [ ] **FAISS Integration** - Semantic vector search
- [ ] **Sentence Transformers** - Better embeddings
- [ ] **Multi-language Support** - i18n
- [ ] **Analytics Dashboard** - Usage metrics
- [ ] **User Authentication** - Secure login
- [ ] **Conversation History** - Persistent chat logs
- [ ] **Admin Panel** - Data management UI

---

## 📝 Citation System

The AI uses numbered citations `[1]`, `[2]` to reference source documents:
- ✅ Citations appear inline for factual statements
- ✅ Strict rules prevent overuse
- ✅ Never used for greetings or general advice
- ✅ No filename exposure to users

---

\
---

## 🙏 Acknowledgments

- Inspired by modern telecom portals (Airtel, AWS, Cloudflare)
- UI design principles from enterprise SaaS applications
- Powered by [Perplexity AI](https://www.perplexity.ai/) for intelligent responses

---

## 📞 Support

For questions or issues:
- 📧 Open an issue on GitHub
- 💬 Check the [PROJECT_README.md](PROJECT_README.md) for detailed documentation
- 🐛 Report bugs with detailed reproduction steps

---

<div align="center">

**Built with ❤️ for enterprise telecom support**

⭐ **Star this repo** if you find it helpful!

[![GitHub stars](https://img.shields.io/github/stars/Suryachow/42_suryavamsi?style=social)](https://github.com/Suryachow/42_suryavamsi/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Suryachow/42_suryavamsi?style=social)](https://github.com/Suryachow/42_suryavamsi/network/members)

</div>
