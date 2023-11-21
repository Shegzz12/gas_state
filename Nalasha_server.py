from flask import Flask, request, jsonify
import util

util_path = "util.py"

app = Flask(__name__)

# Initialize values to be used if no data is received
val1 = 2
val2 = 0
val3 = 2

@app.route('/send_data', methods=['POST'])
def receive_data():
    global val1, val2, val3
    received_data = request.get_json()
    if 'result1' in received_data and 'result2' in received_data and 'result3' in received_data:
        val1 = received_data['result1']
        val2 = received_data['result2']
        val3 = received_data['result3']
        print(f"Received result1: {val1}, result2: {val2}, result3: {val3}")
        return "Data received successfully", 200
    else:
        return "Invalid data format", 400

@app.route('/gas_state', methods=['GET'])
def predict_user_input():
    try:
        global val1, val2, val3
        # Use the received values or default values if not received
        input1 = val1
        input2 = val2
        input3 = val3

        # Call the utility function to make predictions
        result = util.predict_user_input(input1, input2, input3)
        # Construct the response
        response = jsonify({
            'result': result
        })

        return response

    except ValueError as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
