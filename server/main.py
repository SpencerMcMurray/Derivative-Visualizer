from flask import Flask, jsonify, request
from logic import logic_adapter
import traceback

app = Flask(__name__)


@app.route("/")
def test():
    return jsonify({"Hello": "world"})


@app.route("/derivative")
def trueValue():
    expr = request.args.get("expr")
    n = request.args.get("n")
    value = request.args.get("value")

    try:
        res = logic_adapter.getAll(expr, value, n)
        return jsonify({'success': True, 'result': res})
    except Exception:
        traceback.print_exc()
        return jsonify({'success': False})


if __name__ == "__main__":
    app.run(debug=True)
