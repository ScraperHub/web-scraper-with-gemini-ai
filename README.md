# 🤖 Gemini AI Web Scraper with Python

This repository shows how to build a **Gemini-powered web scraper** using Python and LLMs to extract structured data from complex web pages — without writing custom parsing logic.

📖 Read the full tutorial → [How to Leverage Gemini AI for Web Scraping](https://crawlbase.com/blog/how-to-leverage-gemini-ai-for-web-scraping/)

## ✨ What It Does

- Fetches HTML from any public webpage
- Converts HTML to Markdown using markdownify
- Sends it to Gemini AI with a natural language prompt
- Extracts structured data in JSON format

## 🧰 Tech Stack

- `google-generativeai` – Gemini API for LLM-powered parsing
- `requests` – For basic HTTP requests (if not using a proxy)
- `beautifulsoup4` – For basic HTML parsing (optional)
- `markdownify` – Converts HTML into cleaner Markdown
- `python-dotenv` – For managing API keys and environment variables

## 📦 Installation

1. Clone this repo:

```bash
git clone https://github.com/yourusername/gemini-ai-web-scraper.git
cd gemini-ai-web-scraper
```

2. Install dependencies:

```bash
pip install google-generativeai python-dotenv requests beautifulsoup4 markdownify
```

3. Add your Gemini API Key in the script or as environment variable.

## 🚀 Scale Scraping with Crawlbase Smart Proxy

Web scraping with Gemini AI can hit blocks, CAPTCHAs, and anti-bot systems. Crawlbase Smart Proxy solves that.

### ✅ Why Use It?

- Avoid IP blocks with automatic rotation
- Bypass CAPTCHAs seamlessly
- Skip proxy management
- Get clean, parsed HTML for better AI input

### 🔧 Example Usage

```python
import requests
import time

proxy_url = "http://_USER_TOKEN_@smartproxy.crawlbase.com:8012"
proxies = {"http": proxy_url, "https": proxy_url}
url = "https://example.com/protected-page"

time.sleep(2)  # Mimic human behavior
response = requests.get(url, proxies=proxies, verify=False)
print(response.text)
```

Replace `_USER_TOKEN_` with your Crawlbase Smart Proxy token. Get one after signup on [Crawlbase](https://www.crawlbase.com/signup).
