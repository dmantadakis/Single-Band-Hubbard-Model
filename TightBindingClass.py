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

    def dispersion_relation(self,kx,ky):
        pass

    def set_atoms(self,atom):
        """
        Define the unit-cell of the model
        
        Arguments:
        ----------
        unit_cell: list of tuples, where the tuples denote the position of the orbital in the 
                   unit cell (real space coordinates)
        """

    def set_primitive_vectors(self,vectors):
        """
        Define the primitive vectors in real space
        
        Arguments:
        ---------
        vectors: list of tuples, where each tuple represent the coordinates of the primitive vector
        """
        for name,coord in vectors: setattr(self,"a"+name,coord); setattr(self,"k"+name,

    def set_hopping(self,hopping):
        pass

atom = {"A":(0,0),"B":(1,0)

unit_cell = [(0,0),(0,0),(0,0)]
real_space_vectors = {"a1":(1,0),"a2":(0,1)}


