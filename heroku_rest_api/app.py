import os
from flask import Flask, jsonify
import run


app = Flask(__name__)


result = run.output


@app.route('/ml/api/v1.0/output', methods=['GET'])
def get_output():

    return jsonify(result)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
