from flask import Flask
from routes.bulb import bulb_bp
from routes.kettle import kettle_bp

app = Flask(__name__)
app.register_blueprint(bulb_bp, url_prefix="/api/bulb")
app.register_blueprint(kettle_bp, url_prefix="/api/kettle")

if __name__ == "__main__":
    app.run(debug=True)
