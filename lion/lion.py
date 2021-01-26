from zebra_array import ZebraArray
zeb = ZebraArray()
class Lion:


    def  __init__(self):
        self.miss_count = 0
        self.kill_count = 0
        self.year_count = 0
    def kill(self):
        for i in range(0, 99):
            if self.kill_count == 10:
                break

