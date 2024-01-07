"""
The Builder is a creational design patter that is used when we have a big class that executes a lot of steps
in the creation of the object. For example, we may have a Data class. Now we might have some preprocessing for the
data that may encompass many steps, with a lof of conditions. Implementing all of that in the constructor will
bloat it significantly.
What if we want to build different types of Data with different preconditions? Do we have to create multiple
Builder classes just for a slightly different implementation? Well, either that, or we put the conditions in this
one class with multiple variables, that may not all be used. This creates a bloated class that is hard to maintain
and also forces us to pass variables that we may not always need, bloating the constructor.
class Product:
    constructor(val1, val2, val3, val4, val5)
    If something:
    (use val1 and 2)
        do this
    elif something else:
    (use val3, 4, 5)
        do that
    ....
etc.

This is rarely an optimal solution and should be avoided. Instead, we should implement a Builder class.
The Builder class will provide an Interface with the methods that are required to build the Product step
by step. The client will then use the Builder to invoke those steps and build exactly the object that it
expects with using the exact parameters that are needed, nothing more, nothing less.
Moreover, one can use a Director, where the most common patterns for the Builder may be stored, to further
decouple the client from having to know how the Builder is implemented.

For example, building a House. It needs walls, doors, windows. But it may also have a pool, a garage, a
shed, a cool backyard etc.
The Builder will have the methods to build the House step by step and depending on what we want, we can just do
buildWalls,
buildDoors,
buildWindows,
buildPool,
build... ooops we are out of money. Someone else could definitely add a garage, a shed and a backyard though!
The Director will have methods to build the most requested types of houses without us having to chain all those
methods every time. For example, build barebones and build luxurious.
"""
from Builder.builders import Builder
from Builder.directors import HousingDirector
from Builder.houses import NormalHouse, Mansion

builder_mansion = Builder(house_type=Mansion)
builder_normal = Builder(house_type=NormalHouse)

builder_normal.build_pool().build_windows().build_doors().build_walls()
builder_mansion.build_walls().build_doors().build_windows() # No pool and other parts.

"""
Requesting the built object triggers a reset function, that resets the builder to its zero state,
allowing for the building of a new item. This is required, since the Builder class holds the state
of the currently to be built House and once it is requested, the state is nullified and the Builder
is ready to build a new item.
"""
house = builder_normal.built_object
mansion = builder_mansion.built_object
print(house.check_available_to_live())
print(mansion.check_available_to_live())

builder_normal.build_pool().build_doors().build_windows()
house_2 = builder_normal.built_object
print(house_2.check_available_to_live()) # No walls.

"""
Using Directors, we do not have to possess knowledge on how exactly the Houses and Mansions are built 
in order to construct them. We just have to call Director construct_mansion and construct_normal_house
to receive a mansion and a normal house.
"""
builder_normal = Builder(house_type=NormalHouse)
director = HousingDirector(builder=builder_normal)
minimal_house = director.construct_normal_house()
house_with_extras = director.construct_mansion()
print(minimal_house.check_available_to_live())
print(house_with_extras.check_available_to_live())

"""
Here we can see a slight problem. Our builder can work with Mansions and with Normal Houses, but our
director can build both Mansions AND Normal Houses. Now we have to split this director into 2 directors,
one for Mansions and one for Normal Houses where each director will have a simplified version and a more
robust version with added extras. 

We have then eventually separated our code in the following modules:
Builders - for different type of functionality, easy to extend. Open Closed.
Houses - for different types of Houses, easy to extend, code separation. SR + OC.
Directors - A director for each type of house and builder assuming they have different requirements
that cannot be summed up by one director. In the usual case, we would have a construct barebones and construct
full project, where the code will be different for Mansions and Normal houses.

That way, we have loose coupling, we have the ability for multiple directors, houses and builders, should 
some houses be prohibited of building specific constructions.
"""