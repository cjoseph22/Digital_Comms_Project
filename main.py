# This code will implement a simple Binary PAM mod/demod

import numpy as np

#Constants
N = 12 #Samples per symbol

#Generate a vector of random bits
Bits_in = np.random.randint(0, 2, (10, 1))

#Convert to Symbols
Symbols_in = (Bits_in*2-1)

#Define the Pulse Shape, Let's go with NRZ
p = np.ones((N,1))

#Upsample the Symbols Vector
delta_train = np.zeros((Symbols_in.size*N,1))
delta_train[0:N:] = Symbols_in

print(delta_train)

