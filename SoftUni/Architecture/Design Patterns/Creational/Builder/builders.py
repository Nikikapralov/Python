from abc import ABC, abstractmethod


class AbstractBuilder(ABC):
    def __init__(self, house_type):
        self.house_type = house_type
        self._reset()

    def _reset(self):
        self.built_object = self.house_type

    @property
    def built_object(self):
        result = self._built_object
        self._reset()
        return result

    @built_object.setter
    def built_object(self, value):
        """
        Set a new object every time we try to build
        """
        self._built_object = value()

    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_doors(self):
        pass

    @abstractmethod
    def build_shed(self):
        pass

    @abstractmethod
    def build_pool(self):
        pass

    @abstractmethod
    def build_windows(self):
        pass

    @abstractmethod
    def build_garden(self):
        pass


class Builder(AbstractBuilder):

    def build_doors(self):
        self._built_object.house_parts.append("doors")
        return self

    def build_pool(self):
        self._built_object.house_parts.append("pool")
        return self

    def build_shed(self):
        self._built_object.house_parts.append("shed")
        return self

    def build_walls(self):
        self._built_object.house_parts.append("walls")
        return self

    def build_windows(self):
        self._built_object.house_parts.append("windows")
        return self

    def build_garden(self):
        self._built_object.house_parts.append("garden")
        return self
