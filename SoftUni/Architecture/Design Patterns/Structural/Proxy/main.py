"""
A Proxy is a structural design pattern that is akin to multiple patterns. Factory, Decorator for example.
The idea of the Proxy is that it is a class that has the same interface like an object, but the Proxy can
perform some additional operations before or after the operation of the main class is used.

The Proxy pattern is very similar to the Decorator pattern in that it builds upon a simpler object.
There is a big difference though. Usually the proxy manages the lifecycle of the object from begin to end,
meaning the instance is created inside the Proxy and deleted with the Proxy.

For example, a Proxy can check the credentials of a user before it honours the request.

There are different types of proxies, some of which can be implemented as Decorators, Factories or Singletons
themselves.

Logging Proxy.
Credential checking Proxy.
Lazi initialisation Proxy.
Instance holder and deleter proxy. (Keeps track of which instances are in use and if not, deletes them.)
Caching Proxy. (Keeps just one database connection for the whole app and reuses it.)
Network Proxy. (Like an adapter, builds all the necessary stuff for a request and adds it to the operation.)

We will implement a credential checking proxy.
"""

from Structural.Proxy.proxy import Authorisation, AuthorisationAuthenticationProxy

admins = ["Tony", "Pesho"]
not_admin = "Petko"
auth = Authorisation
auth_inst = Authorisation()
auth_pswd = AuthorisationAuthenticationProxy(list_of_admins=admins, authorisation=auth)
auth_pswd.log_in("Tony")
auth_pswd.log_in("Tony")
auth_pswd.log_out("Pesho")
auth_pswd.log_out("Tony")
auth_pswd.log_in("Petko")
auth_inst.log_in("Petko")
auth_inst.log_out("Petko")