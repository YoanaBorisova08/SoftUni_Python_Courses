from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans: list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []

    def add_customer(self, customer: Customer):
        self.add_object(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        self.add_object(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        self.add_object(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan):
        self.add_object(plan, self.plans)

    def add_subscription(self, subscription: Subscription):
        self.add_object(subscription, self.subscriptions)

    def subscription_info(self, s_id: int):
        subscription = self.get_obj_by_id(s_id, self.subscriptions)
        customer = self.get_obj_by_id(subscription.customer_id, self.customers)
        trainer = self.get_obj_by_id(subscription.trainer_id, self.trainers)
        plan = self.get_obj_by_id(subscription.exercise_id, self.plans)
        equipment = self.get_obj_by_id(plan.equipment_id, self.equipment)
        result = [repr(subscription), repr(customer), repr(trainer), repr(equipment), repr(plan)]
        return "\n".join(result)

    @staticmethod
    def get_obj_by_id(_id, collection):
        return next((o for o in collection if o.id == _id), None)

    @staticmethod
    def add_object(obj, collection):
        if obj not in collection:
            collection.append(obj)