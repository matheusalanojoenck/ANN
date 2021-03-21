import numpy as np

def q4():
    M = [[-4.184, -0.943, 4.738], [0.733, 1.306, 0.256], [-1.18, -0.791, 3.64]]

    # 1.86⋅L2+L1→L1
    for i in range(len(M[0])):
        M[0][i] = 1.86 * M[1][i] + M[0][i]

    # 4.545⋅L1 + L3→L3
    for i in range(len(M[0])):
        M[2][i] = 4.545 * M[0][i] + M[2][i]

    # L1↔L3
    temp = M[0]
    M[0] = M[2]
    M[2] = temp

    # -4.184⋅L2→L2
    for i in range(len(M[0])):
        M[1][i] = -4.184 * M[1][i]

    # L2↔L3
    temp = M[1]
    M[1] = M[2]
    M[2] = temp

    print(M)

def q3():
    M = [[-0.378, -1.283, 1.087], [-2.668, 1.349, 1.976], [-1.443, 0.368, 0.801]]

    # -3.51⋅L2→L2
    for i in range(len(M[0])):
        M[1][i] = -3.51 * M[1][i]

    # L1↔L2
    temp = M[0]
    M[0] = M[1]
    M[1] = temp

    # 3.455⋅L2+L3→L3
    for i in range(len(M[0])):
        M[2][i] = 3.455 * M[1][i] + M[2][i]

    print(M)

if __name__ == '__main__':

    q3()