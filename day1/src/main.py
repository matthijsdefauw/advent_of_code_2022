import os
from functions import *

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(base_path+r'\data\input.txt') as f:
    data = [line.rstrip('\n') for line in f]

sol1, sol2 = solution(data)
print('Antwoord 1:', sol1)
print('Antwoord 2:', sol2)