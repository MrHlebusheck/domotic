from functools import wraps
from flask import request, jsonify, Blueprint
from iot.xiaomi_kettle import XiaomiKettle

kettle_bp = Blueprint('kettle_bp', __name__)


def with_kettle(f):
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
            kettle = XiaomiKettle(ip, token)
        except Exception as e:
            return
            jsonify({"error": f"Failed to create kettle: {str(e)}"}), 500

        return f(*args, kettle=kettle, **kwargs)
    return decorated_function


@kettle_bp.route("/status")
@with_kettle
def status(kettle):
    return jsonify(kettle.get_status())


@kettle_bp.route("/temp")
@with_kettle
def temp(kettle):
    return jsonify(kettle.get_temp())


@kettle_bp.route("/is_lifted")
@with_kettle
def is_lifted(kettle):
    return jsonify(kettle.is_lifted())
