import requests as re

# Endpoint of API
url = "http:127.0.0.1:8000/fbsummarize_text"

# Input text and summarization parameters
data = {
    "text": "Your input text goes here.",
    "params": {
        "max_length": 150,  # Set your desired maximum length
        "min_length": 30    # Set your desired minimum length
    }
}


# Send POST request
response = re.post(url, json=data)
# Print summary (output)
print (response.json())