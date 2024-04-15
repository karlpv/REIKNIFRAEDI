import re
import numpy as np
import pandas as pd 
class Skil(object):
    """Timadaemi 2 f. REI
hello there team  im gay as hell
    """
    def pd_calc(self,arr, col_names, row_names):
        n, m = arr.shape 
        if len(col_names) < m:
            col_names += [col_names[-1]] * (m - len(col_names))
        else:
            col_names = col_names[:m]
        
        if len(dow_names) < n:
            row_names += [row_names[-1]] * (n - len(row_names))
        else:
            row_names = row_names[:n]
        
        df = pd.DataFrame(arr, columns=col_names, index=row_names)
        return df


if __name__ == '__main__':
    skil = Skil()

