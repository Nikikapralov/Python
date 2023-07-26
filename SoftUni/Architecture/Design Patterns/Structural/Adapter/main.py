"""
Adapter, also known as a wrapper is a way of making two incompatible interfaces - compatible.
For example, we have a program that works with XML and now have to integrate it with an app
that uses JSON as a format. We can create an Adapter that will wrap around the data and turn it
from XML to JSON and maybe also from JSON to XML.

AppXML -> Wrapper(Data) -> AppJSON

The Client code is not coupled with the Adapter (Wrapper). That allows for 2 teams to work on the
project without merge issues, one developing the AppXML and the other developing the Wrapper.
As such we can now create multiple Wrappers for communication with different third party APIs.

The Adapter has to implement all methods of the client class, which will allow the clients
to use the adapter through the client class, giving us the option to change or extend the code
of the adapter without affecting the client in any way. -> leads to decoupled code. As such,
if the adapter changes, we will not have to redeploy the client as well.

Incorporates the SRP and Open/Closed.
Can be built through composition or through multiple inheritance by inheriting all the client
and third party app features to wrap around.

Example:
    Client has API and wants to call TP with data as XML.
    Now TP takes only JSON and the data must be converted
    somewhere in the program. Instead of writing utility functions and
    mixing them on multiple places in the code, we can create an Adapter class,
    which will use the interface for Client, in the wrapper function do the
    necessary code modifications and then call the third party api from there.

    Sure we don't really need a class, we can just use a wrapper function, but this
    is in Python and it wouldn't work in non scripting languages for example.
"""

from Adapter.adapters import FromClientAdapter
from Adapter.clients import ClientA
from Adapter.third_party_app import ThirdParty
client = ClientA()
third_party = ThirdParty()
adapter = FromClientAdapter(third_party_app=third_party)

print(client.request())
print(third_party.request_third_party())
print(adapter.request())