import re
import numpy as np


class Skil(object):
    """Skilaverkefni 8 f. REI

    """


    def f(self,x):
        fall = (4*x[0]**2) - (4*x[0]*x[1]) + (2*x[1]**2) + (10*x[0]) - (6*x[1]) 
        return fall  

    def df(self,x):
        df_y = -4*x[0] + 4*x[1] - 6
        df_x = 8*x[0] - 4*x[1] + 10
        return np.array([df_x, df_y])
    
    def gradient_descent(self, df, x0, step, tol):
        x_i = x0
        for i in range(1001): 
            dx_i = df(x_i) 
            x_new = x_i - step * dx_i 
            if np.linalg.norm(x_new - x_i) < tol or np.linalg.norm(df(x_i)) < tol:
                return x_new
            x_i = x_new 
        return x_new

if __name__ == '__main__':
    skil = Skil()

