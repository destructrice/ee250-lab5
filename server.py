from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    # Parse the JSON sent to this endpoint
    data = request.get_json()
    
    # Extract the message from the JSON
    message = data.get('message', 'No message received')
    
    # Return the same message in the response
    return jsonify({'echo': message})

if __name__ == "__main__":
    app.run(debug=True)


