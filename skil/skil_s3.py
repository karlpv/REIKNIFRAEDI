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
        staerd = max(max(key) for key in d.keys()) + 1  
        
        ls = [[0]*staerd for i in range(staerd)]
        
        for (i, j), value in d.items():
            ls[i][j] = value
        
        return ls
        
    def snuavid(self,d1):
        d2 = {}
        for key, value in d1.items():
            
            if value in d2:
                if not isinstance(d2[value], list):
                    d2[value] = [d2[value]]
                d2[value].append(key)
            else:
                d2[value] = key
        return d2


if __name__ == '__main__':
    skil = Skil()
