import requests
import json
import google.generativeai as genai
from bs4 import BeautifulSoup
from flask import current_app
def configure_gemini():
    api_key = current_app.config['GEMINI_API_KEY']
    genai.configure(api_key=api_key)
def get_text_from_url(url:str)->str|None:
    try:
        headers={
            'User-Agent':'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response=requests.get(url,headers=headers,timeout=10)
        response.raise_for_status()  
        soup=BeautifulSoup(response.content,'html.parser')
        paragraphs=soup.find_all('p')
        article_text=' '.join([p.get_text() for p in paragraphs])
        return article_text
    except requests.exceptions.RequestException as e:
        current_app.logger.error(f"Error fetching URL {url}: {e}")
        return None
def analyze_text_with_gemini(article_text:str)->dict:
    configure_gemini()
    model=genai.GenerativeModel('gemini-1.5-flash-latest')
    prompt=f"""
    You are an expert market analyst. Your task is to extract product-centric sales trends from the following article.
    
    From the text provided, perform these actions:
    1.  **Identify Products**: List all specific product names or product categories mentioned.
    2.  **Extract Sales Trend**: For each product, describe its sales trend (e.g., "increasing sales", "declining demand", "strong market entry", "facing competition").
    3.  **Summarize**: Provide a single, concise summary of the overall market trends described in the article.

    Format your entire output as a single JSON object with two main keys: "summary" and "products".
    The "products" key should contain a list of JSON objects, where each object has two keys: "product_name" and "trend".

    Here is the article text:
    ---
    {article_text}
    ---
    """
    try:
        response = model.generate_content(prompt)
        cleaned_response = response.text.strip().replace('```json', '').replace('```', '').strip()
        return json.loads(cleaned_response)
    except Exception as e:
        current_app.logger.error(f"Error during Gemini API call: {e}")
        return {"error": "Failed to analyze text with Gemini API."}
