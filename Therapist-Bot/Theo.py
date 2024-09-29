import os
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Initialize OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_openai_response(user_input):
	response = openai.Completion.create(
		engine="text-davinci-003",
		prompt=f"User: {user_input}\nTherapist:",
		max_tokens=400,
		temperature=0.7,  # Adjust temperature as needed
		top_p=1.0,
		frequency_penalty=0.0, 
		presence_penalty=0.6
	)
	return response.choices[0].text.strip()

@app.route('/chat', methods=['POST'])
def chat():
	data = request.get_json()
	user_input = data.get('message')
	
	if not user_input:
		return jsonify({'error': 'No message provided'}), 400

	therapist_response = get_openai_response(user_input)
	return jsonify({'response': therapist_response})

if __name__ == '__main__':
	app.run(debug=True)

