"""
Allows the copying of existing objects without a dependency on their classes.
For example, if we have class Cake and we want to create a copy of a cake we already have,
we take the data from the existing cake and we create a new cake as such Cake(data). Now,
this means that our code is dependent on the Cake class and if the cake class were to be
changed, a redeploy of the system will be needed.

The prototype pattern incorporates a copy method inside the Cake. That way, you can call Cake.copy and
receive a new Cake object but be independent of the class Cake.

Also, what if some attributes of the Cake are private and cannot be seen? You will copy a Cake,
but you won't copy it fully.

A Prototype is a class that has the .clone() method. It creates a new object and makes the code
independent on the class itself. A PrototypeRegistry can be used for independent access to multiple
objects. For example Buttons. If we wanted a red button we would have to create such a button every time
we needed it. Instead, we can create those buttons and add them to a registry, then work with that
registry and retrieve the instances of the buttons whenever we need them, coupling our code with the
Registry, but leaving it decoupled with the Buttons and allowing for another team to work on them independently.

When to use Prototype?
- when providing an API where the clients do not have access to the initialisation class but may want
to copy and modify or use objects of their own.
- when we want to decouple our code from the Class. We use the clone method to receive copies from the
objects that we want to reuse.
- when inheritance is used to create subclasses, that are only differentiated in the way they create the
instance and not in how it works. To solve the problem of having multiple dummy subclasses with different
configs in their constructors, just have a set of Prototypes that can be copied.

Python has a library and 2 dunder methods that cater for copy and deepcopy of a prototype.
"""
import copy

from Prototype.prototype_classic import Prototype

# Implementation 1 disregarding the current python capabilities.

first = Prototype(1, 2)
print(first.attribute_1, first.attribute_2, first.list_1, first.dict_1)
second = first.clone()
print(second.attribute_1, second.attribute_2, second.list_1, second.dict_1)
second.dict_1["hello"] = 3
second.list_1.append("goodbye")
print(second.attribute_1, second.attribute_2, second.list_1, second.dict_1)
print(first.attribute_1, first.attribute_2, first.list_1, first.dict_1)

# Implementation 2 taking into account the __copy__ and __deepcopy__ python methods.
print("-" * 100)
from Prototype.prototype_pythonic import SomeClass

first = SomeClass(1, 2)
first.list = [[1, 2, 3], [1, 2, 3, 4]]
first.dict = {"1": 1}
print(first.attribute_1, first.attribute_2, first.list, first.dict)
second = copy.copy(first)
second.dict["2"] = 2
second.list[0].append("word")
print(second.attribute_1, second.attribute_2, second.list, second.dict)
print(first.attribute_1, first.attribute_2, first.list, first.dict)
# Here, the innerlists are still linked and one must be careful. We have to use deepcopy.
print("-" * 100)

first = SomeClass(1, 2)
first.list = [[1, 2, 3], [1, 2, 3, 4]]
first.dict = {"1": 1}
print(first.attribute_1, first.attribute_2, first.list, first.dict)
second = copy.deepcopy(first)
second.dict["2"] = 2
second.list[0].append("word")
print(second.attribute_1, second.attribute_2, second.list, second.dict)
print(first.attribute_1, first.attribute_2, first.list, first.dict)










