from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Initialize OpenAI API key
openai.api_key = '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'

@app.route('/chat', methods=['POST'])
def chat():
	user_input = request.json.get('message')
	if not user_input:
		return jsonify({'error': 'No message provided'}), 400

	# Generate response using OpenAI
	response = openai.Completion.create(
		engine="text-davinci-003",
		prompt=f"User: {user_input}\nTherapist:",
		max_tokens=150
	)

	therapist_response = response.choices[0].text.strip()
	return jsonify({'response': therapist_response})

if __name__ == '__main__':
	app.run(debug=True)
