from flask import Blueprint, request, jsonify
from .services import get_text_from_url, analyze_text_with_gemini
main_bp=Blueprint('main', __name__)
@main_bp.route('/analyze', methods=['POST'])
def analyze_article_from_url():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    data=request.get_json()
    url=data.get('url')
    if not url:
        return jsonify({"error": "Missing 'url' field in request body"}), 400
    article_text = get_text_from_url(url)
    if not article_text:
        return jsonify({"error": f"Failed to retrieve or parse content from URL: {url}"}), 500
    analysis_result = analyze_text_with_gemini(article_text)
    if "error" in analysis_result:
        return jsonify(analysis_result), 500
    return jsonify(analysis_result), 200
