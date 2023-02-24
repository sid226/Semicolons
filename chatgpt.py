from flask import Flask, request, jsonify
import openai

# Set up OpenAI API key
openai.api_key = "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"

# Set up Flask app
app = Flask(__name__)

# Define API endpoint for ChatGPT integration
@app.route('/api/chat', methods=['POST'])
def chat():
    # Get user input from POST request
    user_input = request.json['message']

    # Define the parameters for the GPT-3 API request
    prompt = f"{user_input}"
    temperature = 0.5
    max_tokens = 50

    # Call the OpenAI GPT-3 API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract the AI response from the API response
    ai_response = response.choices[0].text.strip()

    # Return the AI response to the user
    return jsonify({'ai_response': ai_response})

# Start the Flask app
if __name__ == '__main__':
    app.run()
