"""
Bridge is a structural pattern that aim to lower the amount of classes one has to create
when creating variations of a subject. For example, we have shapes and colours.
We have the shapes circle, square and triangle and the colours red and blue.
What this means is that we will have 6 classes in total:
CircleRed
CircleBlue
SquareRed
SquareBlue
etc

We multiply the dimensions to cater for the behaviour of each combination.
Colours X Shapes.

This can quickly get out of hand, plus it will lead to a mix of code. For example, a blue square and a
blue circle have to encompass the same logic for the blue colour. The more shapes we have, the harder this
gets to maintain. It also leads to highly coupled code and ruins the SRP since a class will be responsible
for both shape and colour behaviour.

The solution is to use a Bridge, or basically - Composition.

We break the monolithic glasses based on their dimensions. Back end/Front end. UI/Business Logic. Shape/Colour.
We create classes for shape and classes for colour.
The shape classes receive the colour classes as instances in the constructor and have access to all of
their methods.
This lowers the amount of classes needed from NxM to N+M, does not violate the SRP and incorporates the
Open Closed principle. Assuming the Liskov Substitution Principle is followed with an abstract Interface,
the Bridge pattern is a good solution of breaking up a Monolith, Decoupling the code and allowing for
simultaneous development from multiple teams.
"""

from Bridge.character_class import Mage, Barbarian
from Bridge.personality import EvilPersonality, GoodPersonality

# Here we turn a NxM to N+M by using the Bridge pattern (Composition).

evil_personality = EvilPersonality()
good_personality = GoodPersonality()
evil_barb = Barbarian(personality=evil_personality)
good_barb = Barbarian(personality=good_personality)
evil_mage = Mage(personality=evil_personality)
good_mage = Mage(personality=good_personality)

print(evil_mage.use_skill())
print(good_mage.use_skill())
print(evil_barb.use_skill())
print(good_barb.use_skill())