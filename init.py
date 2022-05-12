import numpy as np
from Global import *
import random


class init:
    mp = np.zeros([Width, Height])

    def initWork(self):
        for i in range(Width):
            for j in range(Height):
                tmp = random.random()
                if tmp >= 0.8:
                    self.mp[i][j] = 1
                else:
                    self.mp[i][j] = 0
        return self.mp
