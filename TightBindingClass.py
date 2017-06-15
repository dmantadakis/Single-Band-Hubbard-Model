from pytriqs.gf.local import *
from pytriqs.archive import *
import numpy as np
import matplotlib.pyplot as plt

class TightBinding:
    """
    With this class one can contruct and study a single or multi-band Hubbard model
    either on a square or a cubic lattice.
    """
    def __init__(self,lattice,numk,archive=None):
        self.lattice = lattice
        self.numk    = numk
        self.hopping = hopping        

    def dispersion_relation(self,kx,ky)
