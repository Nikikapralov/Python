"""
The Composite design pattern is used with data and classes that can be represented in a tree
structure. For example a car and the parts it consists of. A car can be looked at as a container of its parts.
Subsequently, each part can be considered a possible container of the parts that make it up.

Example:
    Car consists of Engine and Tires. Subsequently, the Tires consist of Rims and Rubber and the Engine
    of its own parts and so on and so forth.

The Container holds information of other Leafs and Containers. They all share the same Interface, that allows
for methods of add, remove, is_container, execute. The first 2 are methods used by the Containers and only
declared by the Leafs so that we can use the same interface without consideration of the underlying class.
(Yes, that does break the Interface Segregation Principle but remember, no dogma!)
The execute function is to be employed by both Leafs their Containers.
The execute function of a Leaf does all the work. It computes whatever it has to compute, while
the execute function of the Container calls the execute functions of all its leafs. Basically, that results
in a recursive pre_order tree traversal. Here is the moment to mention
that since this is a tree data structure, one can implement also the different kinds of traversal methods.

At the end, each Leaf will return its result and all of those results will be returned to the root container.
(For example, price checking.)

REAL WORLD EXAMPLE: Message Groups.
Imagine that Groups are Containers and the people inside are Leafs.
We have 2 groups, Friends and College friends that is a subgroup of college friends.
We will send a single message to all friends in those 2 subgroups. This is the execute command which
checks for all people in a certain group and subsequently sends them the message.

(Not sure if this is real world now that I think about it, but its what the website said so...Still, I wouldn't
implement it with a composite.)
"""


from Composite.container import Container
from Composite.leaf import Leaf

Car = Container(assembly_cost=10000, name="Car")
Engine = Leaf(price=1000)
Tire = Container(assembly_cost=1)
Rubber = Leaf(price=10)
Rim = Leaf(price=100)
Car.add(Engine)
Tire.add(Rubber).add(Rim)
Car.add(Tire).add(Tire).add(Tire).add(Tire)
print(sum(Car.execute()))

# Special assignments may be directed to objects that are containers due to the is_container method,
# without having to check their specific underlying class due to the violation of the ISP.


def client(components):
    for component in components:
        if component.is_container():
            print(f"This is a container with root {component.root}")
            client(component.children)
        else:
            print(f"This is a leaf with root {component.root}")

client([Car, Tire, Engine])