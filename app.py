from flask import Flask, Response, request, send_from_directory, jsonify
from utils.config import Config
import json
import os
from utils.parsers import *
from utils.request import Request
from utils.gpt4 import GPT4

app = Flask(__name__)

@app.route('/health-check')
def health_check():
    return Response("All Good!", status=200)

@app.route('/submit-statement', methods=['POST'])
def submit_statement():
    """API enpoint for submitting bank statements which needs to be parsed based the file type from either pdf, docs or excel format.
        Args:
            - Just a file consisting bank statement(s).
        Returns:
            - A JSON response containing the parsed transactions along with the details - Date, Description, Amount, Type(Credit/Debit).
    """
    file = request.files['file']
    file_name = request.args['filename']
    file.save(os.path.join(Config.UPLOADED_FILE_PATH.values), file_name)

    ### Create a request object corresponding to an input file. It'll atomatically parse and store the contents.
    request = Request(file, file_name)
    
    ### classify the request and store the results for raw response.
    json_response = gpt4.get_llm_response(request)

    if not json_response:
        return Response("Error occured while parsing the file.", status=400)
    
    return jsonify(json_response)

if __name__ == '__main__':
    gpt4 = GPT4()
    app.run(debug=True)