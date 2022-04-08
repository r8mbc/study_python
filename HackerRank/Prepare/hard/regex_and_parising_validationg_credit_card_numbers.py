# https://www.hackerrank.com/challenges/matrix-script/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

i = 0
text = ""
for i in range(m):
    for a in range(n):
        text += matrix[a][i]

text = re.sub(r"(\w)(\W)+(\w)", r"\1 \3", text)

print(text)
