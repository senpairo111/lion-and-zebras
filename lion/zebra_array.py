from functools import reduce
import matplotlib.pyplot as plt
import numpy as np
from zebra import Zebra
from settings import zebra_count, lion_max_speed
from settings import nec_kills, mutation, speed_max, year_deadline
import random
from settings import SPEEDS


class ZebraArray:

    def __init__(self):
        self.years_passed = 0
        self.zebras = []
        self.failed_year = 0
        self.failed_total = 0
        self.total_speeds = []
        self.failed_list = []
        zeb_div = zebra_count / len(SPEEDS)
        for i in range(zebra_count):
            if i > zeb_div:
                zeb_div += zebra_count / len(SPEEDS)
            self.zebras.append(Zebra(SPEEDS[i % len(SPEEDS)]))

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
        self.failed_list.append(self.failed_year)


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

    def print_stats(self, print_stats=False):
        avg = reduce(lambda x, y: x + y.speed, self.zebras, 0) / len(self.zebras)
        self.total_speeds.append(avg)
        dv = np.sqrt(reduce(lambda x, y: x + (y.speed - avg) ** 2, self.zebras, 0)) / len(self.zebras)
        if print_stats:
            print(f"the average speed is {avg}")
            print(f"the standard deviation is {dv}")
