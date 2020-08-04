from flask import Flask, jsonify, request
from logic import logic_adapter
import traceback
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/")
def test():
    return jsonify({"Hello": "world"})


@app.route("/derivatives")
def derivatives():
    expr = request.args.get("expr")
    n = request.args.get("n")
    start = request.args.get("start")
    end = request.args.get("end")
    points = request.args.get('points')

    try:
        t, nt, nt_err, intvl = logic_adapter.getAllDerivativesForInterval(
            expr, start, end, n, points)
        return jsonify({'success': True,
                        'x': [x for x in intvl],
                        'y': t,
                        'approxs': [{'name': "Newton's Method", "y": nt, "error": nt_err}]
                        })
    except Exception:
        traceback.print_exc()
        return jsonify({'success': False}), 400


if __name__ == "__main__":
    port = os.environ.get('PORT')
    port = 5000 if port is None else port
    app.run(port=port)
