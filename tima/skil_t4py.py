import re
import numpy as np
class Skil(object):
    """Timadaemi 4 f. REI

    """
    def mat1(self,m,n,types):
        if types == "zeros" :
            zeros = np.zeros((m,n))   
            return zeros
        elif types == 'ones':
            ones = np.ones((m,n))
            return ones
        elif types == 'eye':
            eye = np.eye(m,n)
            return eye
        elif types == 'diag':
            diag = np.diag(np.arange(min(m, n)))
            return diag
        else: return None
    def mat2(self,m1,m2,j1,j2):
        m1_j1 = m1[:, j1]
        m2_j2 = m2[:, j2]
        
        z1 = m1_j1 + m2_j2  
        z2 = m1_j1 - m2_j2  
        z3 = m1_j1 * m2_j2  
        z4 = np.dot(m1_j1, m2_j2)  

        return z1, z2, z3, z4


if __name__ == '__main__':
    skil = Skil()

