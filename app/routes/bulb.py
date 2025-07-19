from functools import wraps
from flask import request, jsonify, Blueprint
from iot.yeelight_bulb import YeelightBulb

bulb_bp = Blueprint('bulb_bp', __name__)


def with_bulb(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        ip = request.args.get("ip")
        token = request.args.get("token")

        if not ip or not token:
            return jsonify({
                "error":
                    "Missing required query parameters: ip and token"
            }), 400
        try:
            bulb = YeelightBulb(ip, token)
        except Exception as e:
            return jsonify({"error": f"Failed to create bulb: {str(e)}"}), 500

        return f(*args, bulb=bulb, **kwargs)
    return decorated_function


@bulb_bp.route("/is_on")
@with_bulb
def is_on(bulb):
    return jsonify({
        "state": bulb.is_on()
    })


@bulb_bp.route("/color_mode")
@with_bulb
def color_mode(bulb):
    return jsonify(bulb.get_color_mode())


@bulb_bp.route("/brightness")
@with_bulb
def brightness(bulb):
    return jsonify(bulb.get_brightness())


@bulb_bp.route("/color_temp")
@with_bulb
def temp(bulb):
    return jsonify(bulb.get_color_temp())


@bulb_bp.route("/color_rgb")
@with_bulb
def rgb(bulb):
    return jsonify(bulb.get_color_rgb())
