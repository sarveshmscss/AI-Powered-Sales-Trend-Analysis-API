AI-Powered Sales Trend Analysis APIOverviewThis project is a Python-based web API designed to automate the process of market research by extracting and summarizing product-centric sales trends from online articles. The application accepts a URL to a news article or report, scrapes its content, and leverages the power of the Google Gemini API to perform a detailed analysis. The result is a clean, structured JSON object that identifies key products, their sales trends, and a high-level summary of the article's content, providing actionable insights at a glance.Core FunctionalityURL-Based Analysis: Accepts a public URL as input via a simple POST request.Web Content Scraping: Intelligently fetches the webpage and extracts the primary article text, stripping away HTML boilerplate.AI-Powered Trend Extraction: Utilizes the Google Gemini API to understand the context of the article and identify specific product names or categories.Structured Data Output: For each identified product, it extracts the associated sales trend (e.g., "increasing sales," "facing competition," "strong market entry").Automated Summarization: Generates a concise, AI-powered summary of the overall market trends discussed in the article.Modular and Scalable: Built with a modular Flask application structure, making it easy to extend and maintain.Technology StackBackend Framework: FlaskAI & Natural Language Processing: Google Gemini API (google-generativeai)Web Scraping: requests & BeautifulSoup4Configuration Management: python-dotenvWeb Server: Development server (can be deployed with Gunicorn, etc.)API Endpoint DetailsAnalyze ArticleAnalyzes the content of a given URL and returns a structured summary of product sales trends.Endpoint: /analyzeMethod: POSTRequest Body: Raw JSON{
    "url": "https://www.example.com/news/article-about-tech-sales"
}
Success Response (200 OK):{
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
Error Response (4xx/5xx):{
    "error": "Descriptive error message here."
}
Local Setup and InstallationFollow these steps to run the project on your local machine.1. Clone the Repositorygit clone <your-repository-url>
cd <your-repository-folder>
2. Create and Activate a Virtual EnvironmentWindows:python -m venv venv
.\venv\Scripts\activate
macOS/Linux:python3 -m venv venv
source venv/bin/activate
3. Install Dependenciespip install -r requirements.txt
4. Set Up Environment VariablesCreate a file named .env in the root directory of the project and add your Google Gemini API key:GEMINI_API_KEY="your_api_key_here"
5. Run the Applicationpython run.py
The application will be running on http://127.0.0.1:5001.6. Test the APIYou can use a tool like Postman or curl to test the endpoint:curl -X POST -H "Content-Type: application/json" \
-d '{"url": "https://www.cnbc.com/2024/05/01/apple-aapl-earnings-q2-2024.html"}' \
http://127.0.0.1:5001/analyze
