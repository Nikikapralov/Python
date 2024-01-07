"""
Decorator -> Adding Pre/Post Processing (Like the normal Factory).
Chain of Responsibility -> Handling something at runtime.

The Decorator pattern, also known as a wrapper is used to add qualities to a class that normally
does not possess them. In a sense, it is near to the Chain of Responsibility pattern. The difference is
that Chain of Responsibility decides what events to fire at runtime and depending on the specific request,
while the Decorator builds an object with a specific set of behaviours defined by the user.

For example: A notifier system to notify the user on specific channels.
We may want to send a notification on Facebook, Email and SMS or any combination of the aforementioned.
With the Decorator pattern, we can simply do Notifier(Facebook(Email(SMS()))) and send a message to all 3.
This is built by the user. A better implementation for this would most likely be the Chain of Responsibility
where depending on the request, each system will either notify or not notify the user.

A better example of the Decorator pattern is the Encryption and Compression problem.
Imagine we have a Data Source. We may want to add the ability to Encrypt and Compress it.
We don't have to create a class DataEncryptedCompressed, instead we use the Data(Encrypt(Compress)) interface.
The Data Class gets the data and calls the Encrypt interface which then calls the Compress interface. At the end,
we have a modular chain of events that cannot be broken up once set up but provides us greater flexibility. In a sense,
this is near to the Bridge pattern as it uses Composition.

A real world example of this pattern is to be found in the Django Framework. When we create a class of our own and we
inherit a different class, we always call the parent class super() of the method we want to rewrite. For example,
CustomCookie(Cookie).get_cookie(){ super().get_cookie() - returns the old cookie and then we add our own data to the
cookie.) That way, we get to keep the old functionality, but we also very easily add our own by the means of a Decorator
class. We can then write the following versions and decorate them: AddLocationCookie(AddAddsCookie(Cookie))).

The pattern is useful for creating modular extensions. Yes, Chain of Responsibility does act in a similar way but,
since it is heavily dependent on runtime conditions, it is harder to debug and test.
"""
from Structural.Decorator.decorators import CompressionDecorator, EncryptionDecorator, DataHandler

data_compression_encryption = CompressionDecorator(EncryptionDecorator(DataHandler()))
print(data_compression_encryption.handle())

"""
For this to work we basically need 2 types of classes. A decorator type and a component type, but they both
have to have the same interface! The decorator receives the component and calls its interface to receive the data,
then modifies it itself and returns it. Another decorator may have invoked this chain and can now itself modify the 
data before returning it to the client. This allow for modularity and the ability for multiple teams to design 
independent decorators that can be reused when building a specific object.
"""