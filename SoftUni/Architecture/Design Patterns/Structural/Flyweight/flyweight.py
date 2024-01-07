class FlyweightFactory:
    def __init__(self, flyweight):
        self.flyweights = {}
        self.flyweight = flyweight
    @staticmethod
    def get_key(dictionary):
        """
        Get unique flyweight key. Dictionary of flyweight information.
        """
        return "_".join(sorted(dictionary))

    def get_flyweight(self, flyweight_shared_state):
        key = self.get_key(flyweight_shared_state)
        requested_flyweight = self.flyweights.get(key)
        if not requested_flyweight:
            requested_flyweight = self.flyweight(flyweight_shared_state)
            print("Adding new Flyweight.")
            self.flyweights[key] = requested_flyweight
        else:
            print("Cached Flyweight found.")
        return requested_flyweight


class Bullet:
    def __init__(self, bullet_flyweight, bullet_damage,
                 bullet_speed):
        self.bullet_flyweight = bullet_flyweight
        self.bullet_damage = bullet_damage
        self.bullet_speed = bullet_speed


class BulletFlyweight:
    def __init__(self, shared_state):
        """
        Can set it once, but as soon as it is different than None,
        it becomes immutable.
        """
        self.__shared_state = shared_state

    @property
    def shared_state(self):
        return self.__shared_state

    @shared_state.setter
    def shared_state(self, value):
        if self.__shared_state is None:
            self.__shared_state = value
        else:
            raise Exception("Immutable!")

