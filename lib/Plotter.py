import matplotlib.pyplot as plt
import numpy as np
import datetime
import os

class Plotter:
    def __init__(self, var):
        self.img_dir = './img/'
        self.var = var
        
        if not os.path.exists(self.img_dir):
            os.makedirs(self.img_dir)
        
    def plot(self, mean, sd):
        varUnique = list(set(self.var))
        varCounts = [self.var.count(x) for x in varUnique]
        varInt = list(map(round, map(float, self.var)))
        
        fig, ax = plt.subplots()
        n, bins, patches = ax.hist(varInt, round(len(varUnique) / 1.2), density=True)
        y = ((1 / (np.sqrt(2 * np.pi) * sd)) * np.exp(-0.5 * (1 / sd * (bins - mean))**2))
        ax.plot(bins, y, '--')
        ax.set_title('$\mu=' + str(mean) + '$ $\sigma=' + str(sd) + '$')
        name = str(datetime.datetime.now()).split()[0]
        pathname = self.img_dir + name + '.png'
        
        if not os.path.isfile(pathname):
            plt.savefig(pathname, format='png') 
