import numpy as np

def gaussian_elimination(coef_list) -> np.ndarray:
    M =  np.array(coef_list)
    M = M.astype('float64')
    m, n = M.shape
    
    for pivot_index in range(m-1):
        print(f"Pivot line: {M[pivot_index,:]}\n")
        for row_index in range(pivot_index+1,m):
            if M[row_index, pivot_index] == 0:
                continue
            temp_array = -M[row_index, pivot_index] / M[pivot_index,pivot_index] * M[pivot_index,:]
            print(f"{M[row_index,:]} (line #{row_index+1})")
            print(f"{temp_array} ({-M[row_index, pivot_index] / M[pivot_index,pivot_index]} * pivot line)")
            M[row_index,:] += temp_array
            print(M[row_index,:])
            print()
            # M[row_index,:] -= M[row_index, pivot_index] / M[pivot_index,pivot_index] * M[pivot_index,:]
        print(f"Pivot #{pivot_index+1} iteration:")
        print(M)
        print()

    for pivot_index in range(m):
        print(f"Pivot line: {M[pivot_index,:]}\n")
        if M[pivot_index, pivot_index] == 0:
            continue
        for row_index in range(m):
            if M[row_index, pivot_index] == 0 or row_index == pivot_index:
                continue
            temp_array = -M[row_index, pivot_index] / M[pivot_index, pivot_index] * M[pivot_index,:]
            print(f"{M[row_index,:]} (line #{row_index+1})")
            print(f"{temp_array} ({-M[row_index, pivot_index] / M[pivot_index,pivot_index]} * pivot line)")
            M[row_index,:] += temp_array
            print(M[row_index,:])
            print()
            # M[row_index,:] -= M[row_index, pivot_index] / M[pivot_index,pivot_index] * M[pivot_index,:]
        print(f"Pivot #{pivot_index+1} iteration:")
        print(M)
        print()


    return M

def display_result(M:np.ndarray, var_list):
    m, _ = M.shape
    for i, var in enumerate(var_list):
        if M[i,i] == 0:
            if M[i,m] == 0:
                print(f"{var} = {M[i,m]}/{M[i,i]}", end=' ')
                print("Divisão indefinida. Este sistema possui infinitas soluções.")
            else:
                print(f"{var} = {M[i,m]}/{M[i,i]}", end=' ')
                print("Divisão por zero. Este sistema é impossível de ser resolvido.")
        else:
            print(f"{var} = {M[i,m]/M[i,i]}")

def finite_differences(steps, initial_value, final_value, ode):
    step_size = (final_value - initial_value) / steps
    print(steps)
    M = np.zeros((steps, steps+1))
    
    # First line coefficients
    M[0, 0] = 2
    M[0, 1] = -1

    for i in range(1, steps):
        M[i, i-1] = -1
        M[i, i] = 2
        M[i, i+1] = -1
    
    print(M)