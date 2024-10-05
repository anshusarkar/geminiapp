from flask import Flask, render_template, request
import os
import requests, json

app = Flask(__name__)


# Route to display the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve the input from the form field
    query = request.form['querry']
    
    # Handle the query however you'd like (e.g., print it or process it)
    


    api_key = os.getenv('API_KEY')
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}'

    headers = {
        'Content-Type': 'application/json'
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"{query}"
                    }
                ]
            }
        ]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        # Parse the response data
        result = response.json()
        explanation_text = result['candidates'][0]['content']['parts'][0]['text']
        return explanation_text
    else:
        print(f"Request failed. Status Code: {response.status_code}")
        return response.text


if __name__ == "__main__":
    app.run(debug=True)
