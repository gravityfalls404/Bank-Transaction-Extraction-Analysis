from flask import Flask, Response, request, send_from_directory, jsonify
import json
import os


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'statements'

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
    file_type = file_name.split('.')[-1]
    if file_type not in ['pdf', 'doc', 'docx', 'xls', 'xlsx']:
        return Response(json.dumps({'error': 'File type not supported'}), status=400)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))

    response = {}

    with open('dummy.json', 'r') as f:
        response = json.load(f)

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)