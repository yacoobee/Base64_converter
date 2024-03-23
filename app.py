from flask import Flask, render_template, request
import base64

app = Flask(__name__)

def encode_base64(text):
    try:
        encoded_bytes = base64.b64encode(text.encode('utf-8'))
        encoded_string = encoded_bytes.decode('utf-8')
        return encoded_string
    except Exception as e:
        return f"Error encoding text to Base64: {str(e)}"

def decode_base64(encoded_string):
    try:
        decoded_bytes = base64.b64decode(encoded_string)
        decoded_text = decoded_bytes.decode('utf-8')
        return decoded_text
    except Exception as e:
        return f"Error decoding Base64: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def base64_operations():
    encoded_result = None
    decoded_result = None

    if request.method == 'POST':
        input_text = request.form['input_text']
        operation = request.form['operation']

        if operation == 'encode':
            encoded_result = encode_base64(input_text)
        elif operation == 'decode':
            decoded_result = decode_base64(input_text)

    return render_template('base64_operations.html', encoded_result=encoded_result, decoded_result=decoded_result)

if __name__ == '__main__':
    app.run(debug=True, port=8082, host='localhost')