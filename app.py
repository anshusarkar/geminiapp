import requests
import json
import os
from flask import Flask, request, render_template

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve the input from the form fields
    query = request.form.get('query', '')
    # search_query = request.form.get('search_query', '')

    api_key = os.getenv('API_KEY')
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}'

    headers = {
        'Content-Type': 'application/json'
    }

    # Function to make API requests
    def get_explanation(query_text):
        data = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": query_text
                        }
                    ]
                }
            ]
        }
        try:
            response = requests.post(url, headers=headers, data=json.dumps(data))
            if response.status_code == 200:
                # Parse the response data
                result = response.json()
                return result['candidates'][0]['content']['parts'][0]['text']
            else:
                return f"Error: Request failed with status code {response.status_code}"
        except Exception as e:
            return f"Error: An exception occurred - {str(e)}"

    # Get explanations for both queries
    explanation_text = get_explanation(query)
    # search_explanation_text = get_explanation(search_query)

    # Pass the results back to the template for rendering
    return render_template(
        'index.html',
        query=query,
        # search_query=search_query,
        result=explanation_text,
        # search_result=search_explanation_text
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0.', port=10000)
