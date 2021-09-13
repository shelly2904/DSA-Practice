from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    # O(n^2) solution
    res = [0] * len(temperatures)

    for i in range(len(temperatures)):
        j = i+1
        while j < len(temperatures):
            if temperatures[j] > temperatures[i]:
                res[i] = j -i
                break
            else:
                j += 1

    return res

def dailyTemperaturesEff(temperatures: List[int]) -> List[int]:
    # O(n) Solution
    res = [0] * len(temperatures)
    stack = []
    i = len(temperatures) - 1
    for i in range(0, len(temperatures)):
        while len(stack) != 0 and temperatures[stack[-1]] < temperatures[i]:
            res[stack[-1]] = i - stack[-1]
            stack.pop(-1)
        stack.append(i)
    return res

print(dailyTemperaturesEff([73,74,75,71,69,72,76,73]))



