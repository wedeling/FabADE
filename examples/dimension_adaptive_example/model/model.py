#!/usr/bin/env python3

# scalar analytic test function, defined on [0, 1]**d
import numpy as np
import json
import sys

def sobol_g_func(theta):
    Y = 1.0
    for i in range(d):
        Y *= 2.0 * (np.abs(4.0 * theta[i] - 2.0) + a[i]) / (1.0 + a[i])
    return Y

# def poly_model(theta):
    
#     return np.prod(3*theta**2 + 1)/2**d

# parameters required by test function
a = [1.0, 1.0, 2.0, 4.0, 8.0, 16]

# stocastic dimension of the problem
d = 5

# the json input file containing the values of the parameters, and the
# output file
json_input = sys.argv[1]

with open(json_input, "r") as f:
    inputs = json.load(f)
output_filename = inputs['outfile']

theta = []
for i in range(d):
    theta.append(float(inputs['x' + str(i + 1)]))
theta = np.array(theta)

print(theta)

result = sobol_g_func(theta)
# result = poly_model(theta)
# print(result)

# output csv file
header = 'f'
np.savetxt(output_filename, np.array([result]),
           delimiter=",", comments='',
           header=header)
