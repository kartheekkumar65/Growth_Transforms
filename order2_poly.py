# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def poly(x1, x2):
    return x1**2 + 3*x1*x2 + x2**2

def G(x1, x2, k, index):
    """ k is the non negetive real number which helps in keeping the x1, x2 inside the manifold.
    index is something either 1 or 2. Since dP/dx1 is different from dP/dx2, we use index to distinguish between them."""
    if index is 1:
        return x1*(2*x1 + 3*x2 + k)
    elif index is 2:
        return x2*(2*x2 + 3*x1 + k)
    else:
        print("Pass the correct index")    
    
def GT(x1, x2, k):
    """Growth Transform function
    Returns the single step Growth Transform output for the chosen Polynomial function"""
    tmp1 = G(x1, x2, k, 1)
    tmp2 = G(x1, x2, k, 2)
    if tmp1 < 0 or tmp2 < 0 or tmp1 + tmp2 <= 0 :
        print("Wrong choice of k")
    else:
        x1_out = tmp1 / (tmp1+tmp2)
        x2_out = 1 - x1_out
        return [x1_out, x2_out]

x1 = 0.3
x2 = 0.7
k = 0

x1_in = x1; x2_in = x2; x1_list = []; x2_list = []
for iter in range(100):
    
    [x1_out, x2_out] = GT(x1_in, x2_in, k)
    x1_list.append(x1_out); x2_list.append(x2_out)
    x1_in = x1_out; x2_in = x2_out
