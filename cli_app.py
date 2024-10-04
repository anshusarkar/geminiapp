import requests
import json

# Replace with your actual API key and the endpoint
api_key = 'AIzaSyArcW7CQtSDhnFJiMkDZh7wxPM-Yew9Dl8'
# city = 'London'
url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}'

# Define the headers and data
headers = {
    'Content-Type': 'application/json'
}
query = str(input("Enter your request : "))
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

# Send the request
response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    # Parse the response data
    result = response.json()
    explanation_text = result['candidates'][0]['content']['parts'][0]['text']
    print(explanation_text)
else:
    print(f"Request failed. Status Code: {response.status_code}")
    print(response.text)