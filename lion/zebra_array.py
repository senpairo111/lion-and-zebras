from zebra import Zebra
from settings import zebra_count
from settings import nec_kills
import random
from settings import speeds
class ZebraArray:

    def __init__(self):
        self.success_counter = 0
        self.years_passed = 0
        self.zebras = []
        for i in range(zebra_count):
            self.zebras.append(Zebra(random.choice(speeds)))
    def zeb_picker(self):
        cur = random.choice(self.zebras)
        while cur.alive == False:
            cur = random.choice(self.zebras)
        return cur



    def killer(self):
        while self.success_counter != nec_kills:
            cur = self.zeb_picker()
            if cur.speed > random.randrange(0, 99):
                cur.alive = False
                self.success_counter += 1
                self.years_passed += 1



    def breeder(self):
        for i in range (0, zebra_count - 1):
            if self.zebras[i].alive == False:
                zeb1 = self.zeb_picker()
                zeb2 = self.zeb_picker()
                self.zebras[i].alive = True
                self.zebras[i].speed = (zeb1.speed + zeb2.speed)/2


