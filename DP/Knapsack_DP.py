# O/1 Knapsack Problem

import numpy as np


def knapsack(t_wt, val, wt):
    res_idx = []
    T = np.array([[0 for j in range(0, t_wt + 1)] for _ in range(0, len(val))])
    D = np.array([["" for j in range(0, t_wt + 1)] for _ in range(0, len(val))])

    for i in range(0, len(val)):
        for j in range(0, t_wt + 1):
            if j < wt[i]:
                T[i][j] = T[i - 1][j]
                D[i][j] = "u"
            else:
                T[i][j] = max(val[i] + T[i - 1][j - wt[i]], T[i - 1][j])
                if T[i][j] == val[i] + T[i - 1][j - wt[i]]:
                    D[i][j] = "l"
                else:
                    D[i][j] = "u"

    sh_len = np.shape(D)
    i, j = sh_len[0] - 1, sh_len[1] - 1
    while i > 0 and j > 0:
        if D[i][j] == "u":
            i -= 1
            res_idx.append(i)
        elif D[i][j] == "l":
            j -= wt[i]

    res_val = []
    res_wt = 0
    for i in res_idx:
        res_wt += wt[i]
        res_val.append(str(val[i]))

    print("total_weight", res_wt)
    print("the items value", ", ".join(res_val))


if __name__ == "__main__":
    total_weight = 7
    val = [1, 4, 5, 7]
    wt = [1, 3, 4, 5]
    knapsack(total_weight, val, wt)
