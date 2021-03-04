class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    def __repr__(self):
        customers = ''
        dvds = ""
        last = len(self.dvds) - 1
        for customer in self.customers:
            customers += customer.__repr__() + '\n'
        for index in range(len(self.dvds)):
            if index == last:
                dvds += self.dvds[index].__repr__()
                break
            dvds += self.dvds[index].__repr__() + '\n'
        result = customers + dvds
        return result

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def already_rented_by_same(self, customer, dvd):
        if dvd in customer.rented_dvds:
            return True
        return False

    def already_rented_by_another(self, dvd):
        for customer in self.customers:
            if dvd in customer.rented_dvds:
                return True
        return False

    def underage(self, customer, dvd):
        if customer.age >= dvd.age_restriction:
            return False
        return True

    def get_customer(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer

    def get_dvd(self, dvd_id):
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                return dvd

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.get_customer(customer_id)
        dvd = self.get_dvd(dvd_id)
        if self.already_rented_by_same(customer, dvd):
            return f'{customer.name} has already rented {dvd.name}'
        if self.already_rented_by_another(dvd):
            return f'DVD is already rented'
        if self.underage(customer, dvd):
            return f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f'{customer.name} has successfully rented {dvd.name}'

    def return_dvd(self, customer_id, dvd_id):
        customer = self.get_customer(customer_id)
        dvd = self.get_dvd(dvd_id)
        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f'{customer.name} has successfully returned {dvd.name}.'
        return f'{customer.name} does not have that DVD'
















