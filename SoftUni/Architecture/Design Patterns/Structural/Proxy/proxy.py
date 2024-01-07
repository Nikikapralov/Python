from abc import ABC, abstractmethod


class AbstractAuthorisation(ABC):

    @abstractmethod
    def log_in(self, name):
        pass

    @abstractmethod
    def log_out(self, name):
        pass


class Authorisation(AbstractAuthorisation):

    def log_in(self, name):
        print(f"Logged in {name}, token: 12931iaejdaosda")

    def log_out(self, name):
        print(f"Logged out {name}, token invalidated.")


class AuthorisationAuthenticationProxy(AbstractAuthorisation):
    def __init__(self, list_of_admins, authorisation):
        self.authorisation = authorisation()
        self.list_of_admins = list_of_admins
        self.logged_in = []

    def log_in(self, name):
        print("Log in proxy.")
        if name in self.list_of_admins and name not in self.logged_in:
            self.authorisation.log_in(name)
            self.logged_in.append(name)
        else:
            print("Proxy deny.")

    def log_out(self, name):
        print("Log out proxy.")
        if name in self.logged_in:
            self.authorisation.log_out(name)
            self.logged_in.remove(name)
            """
            Yes, this code is far from perfect and very bug prone, the idea of the Proxy is important,
            not those details.
            """
        else:
            print("Proxy not logged in. Deny.")


"""
We can use a simple Authorisation object without the need of the Authentication Proxy. The Proxy is a drop in
replacement and uses the same interface as the Authorisation but builds upon it. Not unlike the Decorator.
A Proxy manages the lifecycle of the Object on its own (meaning the object is created inside the Proxy, unlike here
in our case.), whereas a Decorator does not. (Simple builds on top of it, moke akin to our current implementation).
"""