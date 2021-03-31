class HDMI:
    def connect_to_device_via_hdmi_cable(self, device): pass


class RCA:
    def connect_to_device_via_rca_cable(self, device): pass


class Ethernet:
    def connect_to_device_via_ethernet_cable(self, device): pass


class PowerOutlet:
    def connect_device_to_power_outlet(self, device): pass


class Television:
    def __init__(self):
        self.rca = RCA()
        self.hdmi = HDMI()
        self.power = PowerOutlet()

    def connect_to_dvd(self, dvd_player):
        self.rca.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.hdmi.connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self):
        self.power.connect_device_to_power_outlet(self)


class DvDPlayer:
    def __init__(self):
        self.hdmi = HDMI()
        self.power = PowerOutlet()

    def connect_to_tv(self, television):
        self.hdmi.connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        self.power.connect_device_to_power_outlet(self)


class GameConsole:
    def __init__(self):
        self.hdmi = HDMI()
        self.power = PowerOutlet()
        self.ethernet = Ethernet()

    def connect_to_tv(self, television):
        self.hdmi.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.ethernet.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        self.power.connect_device_to_power_outlet(self)


class Router:
    def __init__(self):
        self.power = PowerOutlet()
        self.ethernet = Ethernet()

    def connect_to_tv(self, television):
        self.ethernet.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.ethernet.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        self.power.connect_device_to_power_outlet(self)
