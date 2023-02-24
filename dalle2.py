from flask import Flask, request, jsonify
import openai
import requests


# Set up OpenAI API key
openai.api_key = "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"

# Set up Flask app
app = Flask(__name__)

# Define API endpoint for ChatGPT integration
@app.route('/api/dalle', methods=['POST'])
def chat():
    # Get user input from POST request
    user_input = request.json['description']

    # Call the OpenAI GPT-3 API
    response = openai.Image.create(
    prompt=f"{user_input}",
    model="image-alpha-001",
    size="1024x1024",
    response_format="url"
)

    # Extract the AI response from the API response
    image_url =  response['data'][0]['url']

    # Return the AI response to the user
    response = requests.get(image_url)
    if response.status_code:
        fp = open('download1.png', 'wb')
        fp.write(response.content)
        fp.close()

    return jsonify({'image-url:': image_url})


# Start the Flask app
if __name__ == '__main__':
    app.run()
