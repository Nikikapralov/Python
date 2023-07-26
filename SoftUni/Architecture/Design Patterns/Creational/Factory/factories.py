from abc import ABC, abstractmethod

from Factory.products import ProductA, ProductB


class FactoryInterface(ABC):

    @staticmethod
    @abstractmethod
    def __factory_method():
        """
        Used for creation of the objects
        """
        pass

    @classmethod
    def create(cls):
        """
        Used for creation of objects and extra business logic.
        """
        # Pre-process code
        product = cls.__factory_method()
        # Post-process code
        return product


class FactoryA(FactoryInterface):

    @staticmethod
    def __factory_method():
        return ProductA()

    @classmethod
    def create(cls):
        print("Pre processing")
        product = cls.__factory_method()
        return product


class FactoryB(FactoryInterface):
    @staticmethod
    def __factory_method():
        return ProductB()

    @classmethod
    def create(cls):
        product = cls.__factory_method()
        print("Post processing")
        return product
