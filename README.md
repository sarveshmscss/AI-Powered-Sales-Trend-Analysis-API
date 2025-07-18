# AI-Powered Sales Trend Analysis API

A Python-based web API that automates product-centric market research by extracting and summarizing sales trends from online articles using the Google Gemini API.

---

## Overview

This project enables users to submit a public article URL and receive structured insights on product sales trends. It:

* Scrapes article content from the web.
* Uses the **Google Gemini API** for AI-based analysis.
* Extracts product-specific sales trends.
* Generates a high-level summary of the article’s content.

Ideal for businesses, analysts, and researchers seeking fast, AI-powered insights from unstructured news sources.

---

## Core Functionality

* **URL-Based Input**: Accepts a URL via a simple `POST` request.
* **Smart Web Scraping**: Extracts clean article text using BeautifulSoup.
* **AI Trend Extraction**: Uses the Google Gemini API to analyze and detect product-centric sales trends.
* **Structured Output**: Returns a JSON summary with product names and their respective trends.
* **Automated Summary**: Includes a concise summary of the market narrative.
* **Modular Design**: Flask-based structure for easy maintenance and scalability.

---

## Technology Stack

| Component                | Technology                  |
| ------------------------ | --------------------------- |
| Backend Framework        | Flask                       |
| AI/NLP                   | Google Gemini API           |
| Web Scraping             | requests, BeautifulSoup4    |
| Configuration Management | python-dotenv               |
| Web Server               | Flask Dev Server / Gunicorn |

---

## API Endpoint

### Analyze Article

Analyzes a public article and extracts product sales trends.

* **Endpoint**: `/analyze`
* **Method**: `POST`
* **Content-Type**: `application/json`

#### Request Body

```json
{
  "url": "https://www.example.com/news/article-about-tech-sales"
}
```

#### Success Response (200 OK)

```json
{
  "products": [
    {
      "product_name": "Aero-Drone X1",
      "trend": "Significant 40% increase in shipments due to a new marketing campaign."
    },
    {
      "product_name": "Sky-Hopper 2",
      "trend": "Sharp decline in sales as consumers shift to newer technology."
    }
  ],
  "summary": "The company is experiencing strong growth for its new drone models while older products are being phased out. Competitive pressure is noted as a potential future risk."
}
```

#### Error Response (4xx/5xx)

```json
{
  "error": "Descriptive error message here."
}
```

---

## Local Setup and Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

### 2. Create and Activate a Virtual Environment

**Windows**

```bash
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file in the project root and add your Gemini API key:

```
GEMINI_API_KEY="your_api_key_here"
```

### 5. Run the Application

```bash
python run.py
```

Visit `http://127.0.0.1:5001` in your browser or API client.

---

## Testing the API

Use a tool like Postman or `curl` to test:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"url": "https://www.cnbc.com/2024/05/01/apple-aapl-earnings-q2-2024.html"}' \
http://127.0.0.1:5001/analyze
```
---

## Author

**Sarvesh K**
[LinkedIn](https://www.linkedin.com/in/sarveshkmscss)

---

