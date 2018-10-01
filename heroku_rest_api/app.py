from flask import Flask
import run


app = Flask(__name__)


@app.route('/ml/api/v1.0/output', methods=['GET'])
def get_output():

    output = run.model()
    # print(output)
    return output


if __name__ == '__main__':
    app.run(host='0.0.0.0')
