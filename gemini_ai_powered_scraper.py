import requests
from bs4 import BeautifulSoup
from markdownify import markdownify
import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

# Load Gemini API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Step 1: Send the HTTP request
url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
response = requests.get(url)

if response.status_code != 200:
    raise Exception("Failed to fetch the page.")

# Step 2: Extract specific section using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
main_section = soup.select_one("article.product_page")
main_html = str(main_section)

# Step 3: Convert HTML to Markdown
main_markdown = markdownify(main_html)

# Step 4: Use Gemini to extract structured data
model = genai.GenerativeModel("gemini-2.0-flash")
prompt = f"""
Extract the book title, price, and availability from the following content:

{main_markdown}

Respond in JSON format.
"""

response = model.generate_content(prompt)
extracted_data = response.text

# Step 5: Export the result in JSON format
try:
    data = json.loads(extracted_data)
    with open("book_data.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Data saved to book_data.json")
except json.JSONDecodeError:
    print("Failed to parse response from Gemini:")
    print(extracted_data)