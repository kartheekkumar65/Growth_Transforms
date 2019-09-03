#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 19:20:56 2019

@author: kartheek
"""

import numpy as np
import matplotlib.pyplot as plt
import sys

def poly(x1, x2):
    """This is the old and original cost function, which we aim to maximize over 
    given manifold"""
    return -5*x1**2 + 2*x1*x2 - x2**2

def poly_mod(z1, z2):
    """This is the new cost function after transforming the manifold"""
    x1 = 2*z1 - 2; x2 = 2*z2 - 4
    return -5*x1**2 + 2*x1*x2 - x2**2

def G(x1, x2, k, index):
    """ k is the non negetive real number which helps in keeping the x1, x2 inside the manifold.
    index is something either 1 or 2. Since dP/dx1 is different from dP/dx2, we use index to distinguish between them."""
    if index is 1:
        return x1*(24 - 40*x1 + 8*x2 + k)
    elif index is 2:
        return x2*( 8 +  8*x1 - 8*x2  + k)
    else:
        print("Pass the correct index")    
    
def GT(x1, x2, k):
    """Growth Transform function
    Returns the single step Growth Transform output for the chosen Polynomial function"""
    tmp1 = G(x1, x2, k, 1)
    tmp2 = G(x1, x2, k, 2)
    if tmp1 < 0 or tmp2 < 0 or tmp1 + tmp2 <= 0 :
        error("Wrong choice of k")
    else:
        x1_out = tmp1 / (tmp1+tmp2)
        x2_out = 1 - x1_out
        return [x1_out, x2_out]

# lets try with (12, 17) as initilization
# observe the 100 iterations of growth transform

x1 = 12
x2 = 17
k = 16




x1_in = x1; x2_in = x2; x1_list = []; x2_list = []
for iter in range(100):
    # we need to transform the initialized variables before passing them into 
    # algorithm
#    print(iter)
    z1_in = (x1_in + 2)/2 ; z2_in = (x2_in + 4)/2
    
    if iter is 0:
        tmp  = z1_in + z2_in
        z1_in /= tmp ; z2_in /= tmp
        print((z1_in, z2_in))
    
    [z1_out, z2_out] = GT(z1_in, z2_in, k)
    
    # undo the transform 
    x1_out = 2*z1_out - 2; x2_out = 2*z2_out - 4
    
    # store them in a list so, we can print them
    x1_list.append(x1_out); x2_list.append(x2_out)
    x1_in = x1_out; x2_in = x2_out

plt.plot(x1_list); plt.show()
plt.plot(x2_list); plt.show()