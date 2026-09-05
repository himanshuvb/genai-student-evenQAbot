# GenAI Student Event Q&A Bot

A Python-based Generative AI application that uses Google's Gemini API to answer student questions related to an event.

## 🛠️ Tech Stack

- Python
- Google Gemini API
- `google-genai` Python SDK
- Environment Variables
- Git / GitHub

## 📁 Project Structure

```text
assignment1/
├── utils/
│   └── config.py
├── main.py
├── prompt.txt
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## ⚙️ Prerequisites

Make sure you have:

- Python 3.9+
- pip
- Git
- Google Gemini API Key

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/himanshuvb/genai-student-evenQAbot.git
cd genai-student-evenQAbot
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Configuration

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Do not commit the `.env` file to GitHub.

Make sure `.env` is included in `.gitignore`.

## ▶️ Running the Application

Run:

```bash
python main.py
```

The application will accept a student question and use the Gemini API to generate a response.

## 🧠 Prompt

The application uses `prompt.txt` to define the instructions provided to the Gemini model.

You can modify `prompt.txt` to change the bot's behavior, response style, and context.

## 🔄 Application Flow

```text
User Question
      │
      ▼
   main.py
      │
      ▼
Load Configuration
      │
      ▼
Load System Prompt
      │
      ▼
Gemini API
      │
      ▼
Generated Response
      │
      ▼
    User
```

## 🔐 Security

API keys and other sensitive configuration values should never be committed to GitHub.

Use environment variables or a `.env` file to store secrets.

## 📦 Dependencies

Project dependencies are maintained in `requirements.txt`.

Install them using:

```bash
pip install -r requirements.txt
```

## 👨‍💻 Author

**Himanshu Bendale**

GitHub: https://github.com/himanshuvb

## 📄 License

This project is created for educational purposes.
