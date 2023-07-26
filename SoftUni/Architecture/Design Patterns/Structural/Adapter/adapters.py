from Adapter.clients import ClientA


class FromClientAdapter(ClientA):
    """
    Adapter must implement all client methods.
    """
    def __init__(self, third_party_app):
        self.third_party_app = third_party_app

    def request(self):
        """
        The adapter provides an API similar to the Client (request method)
        but it may adjust the data accordingly (from XML to JSON) and then call
        the API of the third party. It is basically a wrapper class.
        """
        return self.third_party_app.request_third_party()