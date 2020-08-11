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
        t, dt, dt_err, intvl = logic_adapter.getAllDerivativesForInterval(
            expr, start, end, n, points)
        return jsonify({'success': True,
                        'x': [x for x in intvl],
                        'y': t,
                        'approxs': [
                            {'name': "Newton's Method",
                                "y": dt[0], "error": dt_err[0]},
                            {'name': "Lanczo's Method",
                                "y": dt[1], "error": dt_err[1]},
                            {'name': "Stencil Method",
                                "y": dt[2], "error": dt_err[2]}
                        ]
                        })
    except Exception:
        traceback.print_exc()
        return jsonify({'success': False}), 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
