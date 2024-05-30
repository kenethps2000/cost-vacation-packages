from clases.passenger import Passenger
from clases.total_time import Total_time


class Vacation:
    costBas = 1000

    def __init__(self, dist, num, dur):
        self.myclass = myclass()
        self.passenger = Passenger(num)
        self.total_TIME = Total_time(dur)
        self.dist = dist

    def sum(self):
        """sum the cost of the vacation package here"""
        if not self.myclass.validThis(self.dist) or not self.passenger.validNumber() or not self.total_TIME.is_valid_total_TIME():
            return -1

        """sum the total cost"""
        numberTotal = self.costBas
        numberTotal += self.myclass.get_extraCost(self.dist)
        numberTotal += self.total_TIME.getFee()
        numberTotal -= self.total_TIME.getTheBestPromoEver()

        discount = self.passagner.forHereDiscount()
        numberTotal = numberTotal - (numberTotal * discount)

        return max(int(numberTotal), 0)