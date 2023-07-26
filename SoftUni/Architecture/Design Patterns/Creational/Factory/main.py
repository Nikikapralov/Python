"""
The factory patters provides an interface, a Factory, which is used to decouple business logic from actual object
implementation.

A Factory method consists of a Factory and a Product.
It looks like this:

Product Abstract:
- Product A
- Product B

Factory Abstract:
- Factory A - return Product A
- Factory B - return Product B

For instance, Product A might require some preprocessing and some postprocessing from Factory A.
Having all of the code in the Product A class will result in 2 teams having to mix and match their code.
If we instead move the post and pre processing parts to the Factory A, we can have 1 team work on the Factory
implementation and another - on how the Product A behaves without them having to integrate the changes and facing
merge conflicts.

When to use:
- When the types and dependencies of the objects are still unknown and
potentially different. - Pre Processing and Post Processing are not
detailed enough at this current stage, but it is clear the all Products
should have the same interface and be largely interchangeable.

Perfect example:
UI -> Button
customUI(UI) -> RoundButton(Button)

Another function of the Factory method is returning and reusing existing
objects from a pool or storage. For example, a connection. You wouldn't want to
recreate a connection every time, that can be expensive! (Imagine having to do it 1 000 000 times!)
As such, you can store the created Objects in a data structure inside the Factory! When attempting to
create a new connection, the Factory can check for existing free connections and return one, then add
it to the data structure for later reuse! Neat!

Pros - avoid tight coupling between Factory and Product (pre/post process and logic)
Supports the SRP - move preinitialisation code at one place, making it easier to support.
Open/Closed - easy extension by introducing new subclasses.

Basically a wrapper around the creation of an object.
"""

from Factory.factories import FactoryA, FactoryB
# No need to import the products, they remain hidden.

product_1 = FactoryA.create()
product_2 = FactoryB.create()
print(product_1.do_stuff())
print(product_2.do_stuff())

"""
At the end the product classes are obfuscated for us. We only depend on the factory.

Result:
One team can work on main. One can work on products. One can work on factory post/pre processing.
At the end we start bottom up - Test product, test Factory deploy to main.
"""
