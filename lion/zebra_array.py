from functools import reduce

import numpy as np

from zebra import Zebra
from settings import zebra_count, lion_max_speed
from settings import nec_kills, mutation, speed_max
import random
from settings import speeds


class ZebraArray:

    def __init__(self):
        self.years_passed = 0
        self.zebras = []
        self.failed_year = 0
        self.failed_total = 0
        for i in range(zebra_count):
            self.zebras.append(Zebra(random.choice(speeds)))

    def zeb_picker(self):
        cur = random.choice(self.zebras)
        while not cur.alive:
            cur = random.choice(self.zebras)
        return cur

    def killer(self):
        self.failed_year = 0
        success_counter = 0
        while success_counter != nec_kills:
            cur = self.zeb_picker()
            if cur.speed < random.randrange(0, lion_max_speed):
                cur.alive = False
                success_counter += 1
            else:
                self.failed_year += 1
                self.failed_total += 1


    def breeder(self):
        for i in range(0, zebra_count - 1):
            if not self.zebras[i].alive:
                zeb1 = self.zeb_picker()
                zeb2 = self.zeb_picker()
                while zeb1 is zeb2:
                    zeb2 = self.zeb_picker()
                self.zebras[i].alive = True
                self.zebras[i].speed = (zeb1.speed + zeb2.speed) / 2 + random.randrange(-mutation, mutation + 1)
                if self.zebras[i].speed > speed_max:
                    self.zebras[i].speed = speed_max
        self.years_passed += 1

    def print_stats(self):
        avg = reduce(lambda x, y: x + y.speed, self.zebras, 0) / len(self.zebras)
        print(f"the average speed is {avg}")
        dv = np.sqrt(reduce(lambda x, y: x + (y.speed - avg) ** 2, self.zebras, 0)) / len(self.zebras)
        print(f"the standard deviation is {dv}")
