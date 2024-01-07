"""
Flyweight, also known as a type of Cache is a Structural design pattern that saves RAM at the
cost of CPU cycles. For example, we have a file with data and we have 6 parameters that we have
to compute using this data. Those parameters are independent and we can use multiprocessing for the
task. Unfortunately, the data is too big and can only be loaded once. How do we proceed? We load the
data before we start the processes and we give each process a pointer to the now shared data. If
implemented in a class and the data is immutable, it now becomes a Flyweight implementation!

Another use case is in games, where we have to spawn entities that share most of their state and
do not require for it to be copied each time. For example bullets that have always the same color and
sprite. We can extract the data for color and sprite in a separate class (the Flyweight) and pass a pointer
to a global instance of that class each time a bullet is generated. Now all bullets will share one Flyweight
implementation and this will save us RAM. We may have different Flyweight implementations, save them in an array
and request specific ones be used with specific bullets. This will unfortunately use up CPU cycles. We can
also use a map (dictionary) although that will make it a bit more complicated to develop. BulletType: FlyweightType

A Flyweight Factory is a good way to control the usage and initialisation of Flyweights. It resembles Singleton and
Proxy in a way, since the Factory checks if the requested Flyweight exists in a list of Flyweights and if not,
it gets created. If it exists, it gets returned. The existing flyweights can be kept in a list or a dictionary,
where the latter is considerably harder and messier to document.

A Flyweight is similar to a Singleton with a few differences. A Singleton has just one instance, whereas as Flyweight
can have multiple instances with different parameters. A Flyweight is immutable, whereas a Singleton is mutable.

Since the code becomes quite complicated, always write in the documentation the reason for the separation
of the data. In this care, saving lots of RAM! To you that may be obvious, to new people - that won't be!
"""

from Structural.Flyweight.flyweight import FlyweightFactory, BulletFlyweight, Bullet
import psutil

bullets = []
for i in range(10**7):
    bullets.append(Bullet(BulletFlyweight({"tangra": 10}), 10, 20))
print(psutil.Process().memory_info().rss / 1024 ** 2) # This uses about 3.9GBs of RAM!

bullets = []
factory = FlyweightFactory(BulletFlyweight)
flyweight = factory.get_flyweight({"tangra": 10})
flyweight_2 = factory.get_flyweight({"tangra": 10})# Created once and reused by being passed through reference to each Bullet
for i in range(10**7):
    bullets.append(Bullet(bullet_flyweight=flyweight, bullet_speed=20, bullet_damage=10))
print(psutil.Process().memory_info().rss / 1024 ** 2) # This uses about 1.2GBs of RAM!
