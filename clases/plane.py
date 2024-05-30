from clases.passenger import Passenger
from clases.total_time import Total_time
from clases.popularSpot import PopularSpot


class Plane:
    def __init__(self, dist, num, dur):
        self.myclass = myclass()
        self.passanger = Passenger(num)
        self.total_TIME = Total_time(dur)
        self.dist = dist
        self.seats = 200

    def sum(self):
        if not self.myclass.validThis(self.dist) or not self.passanger.validNumber() or not self.total_TIME.is_valid_total_TIME():
            return -1

        numberTotal = self.costBas
        numberTotal += self.myclass.get_extraCost(self.dist)
        numberTotal += self.total_TIME.getFee()
        numberTotal -= self.total_TIME.getTheBestPromoEver()

        discount = self.passanger.forHereDiscount()
        numberTotal = numberTotal - (numberTotal * discount)

        return max(int(numberTotal), 0)