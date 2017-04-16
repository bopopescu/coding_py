import matplotlib
import matplotlib.pyplot as plt

class DrawHandler(object):
    
    def __init__(self,
                 nrows=1,
                 ncols=1,
                 plot_number=1):
        fig = plt.figure()
        ax = fig.add_subplot(ncols, ncols, plot_number)


