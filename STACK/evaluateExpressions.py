#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'circuitsOutput' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY circuitsExpression as parameter.
#

def perform_operation(operator, operand_1=None, operand_2=None):
    res = None
    if operator == "&":
        res = operand_1 and operand_2
    elif operator == "|":
        res = operand_1 or operand_2
    elif operator == "!":
        if operand_1 == "0":
            res = "1"
        else:
            res = "0"
    # print(operator, operand_1, operand_2, res)
    return res
    
def circuitsOutput(circuitsExpression):
    results = []
    for exp in circuitsExpression:

        
        operator_list = ["&", "|", "!"]
        operand_list = ["0", "1"]
        stack = []
        
        
        for char in exp:
            if char in [",", " "]:
                continue
            
            # operator_1 = res
            if char != "]":
                stack.append(char)
                continue 
            
            
            if char == "]":
                print("Before: ",stack)
                operator = None
                operand_1 = None
                operand_2 = None
                res = None
                while True:
                    from_stack = stack.pop()
                    if str(from_stack) in operator_list:
                        operator = str(from_stack)
                    elif str(from_stack) in operand_list and operand_1 is None:
                        operand_1 = str(from_stack)
                    elif str(from_stack) in operand_list and operand_2 is None:
                        operand_2 = str(from_stack)
                    elif from_stack == "[":
                        res = perform_operation(operator, operand_1, operand_2)
                        print(operator, operand_1, operand_2, res)
                        stack.append(str(res))
                        print("After: ",stack)
                        break

            
        results.append(res)
    return results
            
    # Write your code here

if __name__ == '__main__':
    circuitsExpression = ['[|, [&, 1, [!, 0]], [!, [|, [|, 1, 0], [!, 1]]]]']
    result = circuitsOutput(circuitsExpression)
    print(result)
   
