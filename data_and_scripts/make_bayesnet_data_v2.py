# I'll be using this code to generate some data for a simple Bayesian network.
# (c) 2015 by Daniel Seita
# EDIT: here's an even simpler one. X_1 -> X_2, for binary variables. That's it!
# Pr(X_1 = 0) = 0.75, Pr(X_1 = 1) = 0.25.
# Pr(X_2 = 0 | X_1 = 0) = 2/3, Pr(X_2 = 0 | X_1 = 1) = 0.1. Ideally this provides enough balance.

import numpy as np

ncols = 1000000 # Change as needed
nrows = 2 # Change as neded
data = np.zeros([nrows,ncols])
data[0,:] = np.random.choice(2, ncols, p = [0.75, 0.25])
second = []
for i in range(ncols):
    if data[0,i] == 0:
        second.append( np.random.choice(2, 1, p = [0.6666667, 0.3333333])[0] )
    else:
        second.append( np.random.choice(2, 1, p = [0.1, 0.9])[0] )
data[1,:] = second
np.savetxt('dataTrivial_' + str(ncols) + '.txt', data, fmt='%i')    
