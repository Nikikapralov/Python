from composite import CompositeInterface


class Container(CompositeInterface):

    def __init__(self, assembly_cost=None, name="Container"):
        super().__init__(name=name)
        self.children = []
        self.assembly_cost = assembly_cost
        self.root = self

    def add(self, component):
        self.children.append(component)
        component.parent = self
        component.root = self.root
        return self

    def remove(self, component):
        self.children.remove(component)
        component.parent = None
        return self

    def is_container(self):
        return True

    def execute(self):
        results = []
        if self.is_container():
            # Assembly cost
            results.append(self.assembly_cost)
        for child in self.children:
            for result in child.execute():
                results.append(result)
        return results


