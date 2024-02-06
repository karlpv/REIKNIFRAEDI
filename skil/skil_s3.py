import re
import numpy as np
class Skil(object):
    """Skilaverkefni 3 f. REI

    """

    def arr_to_dict(self,arr):
        d = {}
        for i,row in enumerate(arr):
            for j,value in enumerate(row):
                d[(i,j)] = value
        return d   

    def dict_to_arr(self,d):
        fylki = np.zeros
        
        
    def snuavid(self,d1):
        

if __name__ == '__main__':
    skil = Skil()
