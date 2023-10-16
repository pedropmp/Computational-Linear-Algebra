import numpy as np
from utils import finite_differences, gaussian_elimination, display_result

np.set_printoptions(formatter={'float': '{: 0.3f}'.format})

problem_1_2_5 = [[4, -8, 5, 1, 0, 0],
                 [4, -7, 4, 0, 1, 0],
                 [3, -4, 2, 0, 0, 1]]
problem_1_2_5_var = ['x', 'y', 'z']
result_ge = gaussian_elimination(problem_1_2_5)

for column in range(3, 6):
    M = np.hstack((result_ge[:,:3], result_ge[:,column].reshape(3,1)))
    print(f"\n\nFor matrix\n{M}, \nthe result is:\n")
    display_result(M, problem_1_2_5_var)

print('-' * 40)

problem_1_2_8 = [[-1, 3, -2, 1],
                 [-1, 4, -3, 0],
                 [-1, 5, -4, 0],]
problem_1_2_8_var = ['x', 'y', 'z']
result_ge = gaussian_elimination(problem_1_2_8)
display_result(result_ge, problem_1_2_8_var)

print('-' * 40)

problem_1_2_9 = [[-1, 3, -2, 4],
                 [-1, 4, -3, 5],
                 [-1, 5, -4, 6],]
problem_1_2_9_var = ['x', 'y', 'z']
result_ge = gaussian_elimination(problem_1_2_9)
display_result(result_ge, problem_1_2_9_var)

print('-' * 40)

problem_1_4_1 = [[ 2, -1,  0,  0,  0,  0,  0],
                 [-1,  2, -1,  0,  0,  0, -1],
                 [ 0, -1,  2, -1,  0,  0, -2],
                 [ 0,  0, -1,  2, -1,  0, -3],
                 [ 0,  0,  0, -1,  2, -1, -4],
                 [ 0,  0,  0,  0, -1,  2, -5],]
problem_1_4_1_var = ['y0', 'y1', 'y2', 'y3', 'y4', 'y5',]
result_ge = gaussian_elimination(problem_1_4_1)
display_result(result_ge, problem_1_4_1_var)

y0 = 0
y1 = 0
steps = 5 + 1
finite_differences(steps, y0, y1, [125, 0, 0])