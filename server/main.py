from flask import Flask, jsonify, request
from logic import logic_adapter
import traceback

app = Flask(__name__)


@app.route("/")
def test():
    return jsonify({"Hello": "world"})


@app.route("/derivatives", methods=["POST"])
def derivatives():
    expr = request.form["expr"]
    n = request.form["n"]
    start = request.form["start"]
    end = request.form["end"]
    points = request.form['points']

    try:
        res = logic_adapter.getAllDerivativesForInterval(
            expr, start, end, n, points)
        return jsonify({'success': True, 'result': res})
    except Exception:
        traceback.print_exc()
        return jsonify({'success': False}), 400


if __name__ == "__main__":
    app.run(debug=True)
