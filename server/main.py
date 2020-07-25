from flask import Flask, jsonify, request
from logic import logic_adapter
import traceback

app = Flask(__name__)


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
        res = logic_adapter.getAllDerivativesForInterval(expr, start, end, n, points)
        return jsonify({'success': True, 'result': res})
    except Exception:
        traceback.print_exc()
        return jsonify({'success': False})


if __name__ == "__main__":
    app.run(debug=True)
