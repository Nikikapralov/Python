from Send_data_to_client_in_real_time.Interfaces.Base_Interface import BaseInterface


class Presence(BaseInterface):
    """Used in the Interface Finder"""
    RAW_DATA = [[{"all_ids": {"lpr": [{"alternatives": [{"confidence": None, "plate": None}],
                                      "confidence": None,
                                       "country": {"code": None, "confidence": None, "state": None},
                                       "id": None, "no_countrylogic_id": None,
                                       "track_id": None, "type": None}]},
                  "gateway": {"direction": None, "gate": None},
                  "last_update": None,
                  "medium": {"lpr": {"alternatives": [{"confidence": None, "plate": None}],
                                     "changed": None, "confidence": None,
                                     "country": {"code": None, "confidence": None, "state": None},
                                     "id": None, "no_countrylogic_id": None,
                                     "track_id": None, "type": None}},
                  "name": None, "present-area-name": None,
                  "source": None, "timestamp": None, "type": None,
                  "vehicle_id": None}]]

    def __init__(self, *args):
        super().__init__(*args)
        self.functions = {"id": self.id, "direction": self.direction}

    def __str__(self):
        return 'presence'

    """Returns the licence plate number. 
    (Hardcoding the direct position is faster than using the search algorithm
    so let's assume we will hardcode the most often requested information and use the search algorithm for
    anything else, should the client require us to send different information on a whim, for example.)"""

    @property
    def id(self):
        try:
            return self.json_data["all_ids"]["lpr"][0]["id"]
        except (KeyError, TypeError, IndexError):
            """Hardcode for different type with different data:
             Imaginary search, will throw key error in this example."""
            try:
                return self.json_data["other_config"]
            except (KeyError, TypeError, IndexError):
                pass

    """Returns the direction."""
    @property
    def direction(self):
        try:
            return self.json_data["gateway"]["direction"]
        except (KeyError, TypeError, IndexError):
            try:
                return self.json_data["other_config"]
            except (KeyError, TypeError, IndexError):
                pass
