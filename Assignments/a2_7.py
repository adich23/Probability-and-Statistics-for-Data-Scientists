import numpy as np
def steady_state_power(transition_matrix):
    # k >> 1 
    k = 1000
    # raise to power function
    res = np.linalg.matrix_power(transition_matrix,k)
    print ("Steady_State: Power iteration >> " + str(res[1,:]))
    return res[1,:]

matrix = [[0.9, 0, 0.1, 0],
          [0.8, 0, 0.2, 0],
          [0, 0.5, 0, 0.5],
          [0, 0.1, 0, 0.9]
          ]
steady_state_power(matrix)
