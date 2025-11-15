from abc import abstractmethod, ABC

class BaseToy(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class RubberDuck(BaseToy):
    def make_sound(self):
        return "Squeek"


class RobotDuck(BaseToy):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    def make_sound(self):
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0




