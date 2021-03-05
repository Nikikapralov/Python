class Gym:
    def __init__(self):  # all inside are objects
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.subscriptions = []
        self.plans = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def get_subscription(self, subscription_id):
        subscription = [subscription for subscription in self.subscriptions if subscription_id == subscription.id]
        return subscription[0]

    def get_plan(self, id):
        plan = [plan for plan in self.plans if plan.id == id]
        return plan[0]

    def get_equipment(self, id):
        equipment = [equipment for equipment in self.equipment if equipment.id == id]
        return equipment[0]

    def get_trainer(self, id):
        trainer = [trainer for trainer in self.trainers if trainer.id == id]
        return trainer[0]

    def get_customer(self, id):
        customer = [customer for customer in self.customers if customer.id == id]
        return customer[0]

    @staticmethod
    def get_output(subscription, customer, trainer, plan, equipment):
        output = ''
        output += subscription.__repr__() + '\n'
        output += customer.__repr__() + '\n'
        output += trainer.__repr__() + '\n'
        output += equipment.__repr__() + '\n'
        output += plan.__repr__()
        return output

    def subscription_info(self, subscription_id):
        subscription = self.get_subscription(subscription_id)
        customer = self.get_customer(subscription_id)
        trainer = self.get_trainer(subscription_id)
        plan = self.get_plan(subscription_id)
        equipment = self.get_equipment(subscription_id)
        output = self.get_output(subscription, customer, trainer, plan, equipment)
        return output
