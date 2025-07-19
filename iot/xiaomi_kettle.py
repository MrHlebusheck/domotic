from miio import Device

# https://home.miot-spec.com/spec/xiaomi.kettle.v20


class XiaomiKettle:
    def __init__(self, ip, token):
        self.device = Device(ip, token)

    def update(self):
        self.device.update_state()

    def get_props(self, siid, piid):
        return self.device.raw_command("get_properties", [{
            "siid": siid,
            "piid": piid
        }])[0]["value"]

    def get_status(self):
        status = self.get_props(2, 1)
        result = {"status": status}
        match status:
            case 0:
                result["desc"] = "Idle"
            case 1:
                result["desc"] = "Heating"
            case 2:
                result["desc"] = "Boiling"
            case 3:
                result["desc"] = "Cooling Down"
            case 4:
                result["desc"] = "Keep Warm"

        return result

    def get_temp(self):
        return {"temp": self.get_props(2, 3)}

    def is_lifted(self):
        return {"lifted": self.get_props(3, 7)}
