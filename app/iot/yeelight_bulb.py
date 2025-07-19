from miio import Yeelight


class YeelightBulb:
    def __init__(self, ip, token):
        self.device = Yeelight(ip, token)
        self.update_status()

    def update_status(self):
        self.status = self.device.status()

    def is_on(self):
        return self.status.is_on

    def get_color_mode(self):
        if not self.is_on():
            return {
                "mode": 0,
                "desc": "Off"
            }
        color_mode = self.status.color_mode

        return {
            "mode": color_mode.numerator,
            "desc": color_mode.name
        }

    def get_brightness(self):
        if not self.is_on():
            return {"brightness": 0}
        return {"brightness": self.status.brightness}

    def get_color_temp(self):
        if not self.is_on() or self.status.color_mode.numerator != \
                self.status.color_mode.ColorTemperature:
            return {"temp": 0}
        return {"temp": self.status.color_temp}

    def get_color_rgb(self):
        if not self.is_on() or self.status.color_mode.numerator != \
                self.status.color_mode.RGB:
            return {
                "red": 0,
                "green": 0,
                "blue": 0,
            }
        rgb = self.status.rgb
        return {
            "red": rgb[0],
            "green": rgb[1],
            "blue": rgb[2],
        }
