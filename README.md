
# APIS Project

A Python-based API aggregator providing insights from various domains including news, space, weather, tech trends, chaos index, and more. It also includes sentiment analysis and a fortune generator for fun interactions.

## 🌐 Overview

This project combines multiple APIs and core utilities to deliver a cohesive information service. It's designed to be modular, extensible, and easy to deploy.

### 📁 Structure

```
APIS/
├── main.py                  # Entry point for running the application
├── .env                     # Environment variables (API keys, secrets)
├── requirements.txt         # Python dependencies
├── apis/                    # Contains API-specific modules
│   ├── chaos_index.py
│   ├── nasa.py
│   ├── news.py
│   └── tech_trends.py
├── core/                    # Core utilities and logic
│   ├── fortune_generator.py
│   └── sentiment.py
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd APIS
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables

Create a `.env` file in the root directory with the necessary API keys. Example:

```
NEWS_API_KEY=your_key
NASA_API_KEY=your_key
```

### 4. Run the Application

```bash
python main.py
```

---

## 📦 Features

- 📰 News aggregator (`news.py`)
- 🚀 NASA data fetcher (`nasa.py`)
- 📊 Chaos index visualization (`chaos_index.py`)
- 💻 Tech trends insights (`tech_trends.py`)
- 💬 Sentiment analysis (`sentiment.py`)
- 🔮 Fortune generator (`fortune_generator.py`)

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 🛡 License

This project is licensed under the MIT License.
