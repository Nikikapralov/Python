from Send_data_to_client_in_real_time.Interfaces.Base_Interface import BaseInterface


class VehicleImage(BaseInterface):

    """Used in the Interface Finder"""
    RAW_DATA = [[{"gateway": {"direction": None, "gate": None},
                  "name": None,
                  "plate": None,
                  "source": None, "timestamp": None,
                  "type": None, "vehicle_id": None}]]

    def __init__(self, *args):
        super().__init__(*args)
        self.functions = {'vehicle_id': self.vehicle_id}

    def __str__(self):
        return 'vehicle_image'

    """Returns the vehicle_id."""
    @property
    def vehicle_id(self):
        try:
            return self.json_data["vehicle_id"]
        except (KeyError, TypeError, IndexError):
            try:
                return self.json_data["other_config"]
            except (KeyError, TypeError, IndexError):
                pass


