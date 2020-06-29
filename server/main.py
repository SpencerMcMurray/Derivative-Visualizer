from flask import Flask, jsonify, request
from logic import TrueValue
import traceback

app = Flask(__name__)


@app.route("/")
def test():
    return jsonify({"Hello": "world"})


@app.route("/trueValue")
def trueValue():
    expr = request.args.get("expr")
    var = request.args.get("var")
    n = request.args.get("n")
    value = request.args.get("value")

    try:
        result = float(
            TrueValue.nth_derivative_from_string(expr, var, n, value))
        return jsonify({"success": True, "result": result})
    except Exception:
        traceback.print_exc()
        return jsonify({"success": False})


if __name__ == "__main__":
    app.run(debug=True)
