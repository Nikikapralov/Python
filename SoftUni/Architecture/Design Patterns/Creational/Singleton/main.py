"""
CAREFUL: ANTIPATTERN! It results in a GLOBAL variable and causes code coupling!
VIOLATES THE SRP! - solves 2 problems at once:
- Ensure that only one instance can be alive during runtime, when an attempt of creation
of a new instance is made, the old instance is returned instead. (Database access points, for example.)
- Provide a global access point to that instance. HIGH COUPLING - BAD!

Create a class with a static method that when called either returns an existing cached object,
or it creates the first instance, caches it and returns it, providing a global access point.

Singletons are tricky when multiple threads/processes are involved. Be sure to specify if the
Singleton you are providing is thread safe or not! Writing a thread safe singleton is not very hard,
so always provide a thread safe singleton class!

Singletons can be constructed by using Python Metaclasses. A Metaclass is the class of a class in Python,
since classes themselves are an object. To use a Metaclass do define a singleton, modify its call method
accordingly!

Singletons also don't play well with processes since state there is seperate. A communication and update of the
Singleton must therefor be adjusted for. An absolute nightmare!
"""
import time
from threading import Thread

from Singleton.singleton import Singleton


def create(var):
    singleton = Singleton(var)
    print(singleton.attribute)


if __name__ == "__main__":
    # The second one is not created, instead the first one that is stored in the cache is returned.
    first_p = Thread(target=create, args=[2])
    second_p = Thread(target=create, args=[1])
    first_p.start()
    second_p.start()


