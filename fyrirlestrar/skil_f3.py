import re
import numpy as np
class Skil(object):
    """Skilaverkefni 2 f. REI

    """
    def numpy_test(self,ls):
        arr = np.array(ls)
        arr_t = arr.T
        return arr, arr_t
