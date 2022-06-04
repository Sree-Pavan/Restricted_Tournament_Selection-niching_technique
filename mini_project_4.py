# -*- coding: utf-8 -*-
"""mini_project_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GUEVbFHRpx3SWoe06upH8XBMnyJLt9DQ
"""

## Importing necessary modules
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import math
import random
import pandas as pd

# The test function is defined and solutions or peaks are found
def func(x): 
  return float(np.sin(5*np.pi*float(x))**6)
max = 0
y_max_index = []
for i in np.arange(0,1,0.1):
  y = func(i)
  if y > max:
    max = y
  elif y == max:
    y_max_index.append(np.round(i,1))
print(max)
print(y_max_index)

"""Restricted Tournament Selection

"""

def fitness(x):
  return float(np.sin(5*np.pi*float(x))**6)

def crossover(parents,n_decimals):
  word_1 = ''
  word_2 = ''
  temp = []
  children = []
  a1 = parents[0]
  b1 = parents[1]
  n = n_decimals
  a1 = '0'*(n-len(str(int(a1*(10**n))))) + str(int(a1*(10**n)))
  b1 = '0'*(n-len(str(int(b1*(10**n))))) + str(int(b1*(10**n))) 
  c1 = a1 + b1
  w = [char for char in c1]
  for i in range(n-1):
    w[i+1] = w[-i-1]
  for i in range(n):
    temp.append(w[i])
  for i in range(n):
    w.pop(i)
  word_1 = ''.join(temp)
  word_2 = ''.join(w)
  child_1 = float(word_1)
  child_1 /= 10**n
  child_2 = float(word_2)
  child_2 /= 10**n
  children.append(child_1)
  children.append(child_2)
  return children


def mutation(offspring_crossover,n_decimals):
  r = random.randint(0, 9)
  n = n_decimals
  lis = []
  a1 = offspring_crossover
  a1 = '0'*(n-len(str(int(a1*(10**n))))) + str(int(a1*(10**n)))
  w = [char for char in a1]
  for i in range(n-1):
    lis = list(range(10))
    lis.remove(int(w[-i-1]))
    r = random.choice(lis)
    w[-i-1] = str(r)

  mut_1 = float(''.join(w))
  mut_1 /= 10**n
  return mut_1
def tournament_selection(two_new):
  parents = two_new
  if fitness(parents[0]) > fitness(parents[1]):
    bestparent = parents[0]
  else:
    bestparent = parents[1]
  return round(bestparent,2)

def restricted_tournament_selection(pop,x):
  selected = 0
  candidates = random.choices(pop, k=3)
  min = abs(abs(x)-abs(candidates[0]))
  for i in range(len(candidates)):
    if abs(abs(x)-abs(candidates[i])) < min:
      min = abs(abs(x)-abs(candidates[i]))
      index = i
  selected = candidates[i]
  return round(selected,2)

"""Algorithm process


"""

n_decimals = 1
pop = list(np.arange(0,1,0.1))
temp_pop = pop
temp_pop_1 = pop
import numpy as np
import random
from statistics import mean
optimal = set()
values = []
times = 0
solution = [0.1,0.3,0.5,0.7,0.9]
n_iter = 5000
for m in range(n_iter):
  
  if len(temp_pop)>2:
    Parents = random.sample(temp_pop,2)
    Next_gen = []
    New = []
    new_2 = [] 
    new_1 = []

    ## Step 2 : Performing GA
    Children = crossover(Parents,n_decimals) # Crossover is performed
    for child in Children:
      New.append(mutation(child,n_decimals)) # New is A'

    ## Step 3 : RTS scans for w(window size)

    a_2 = restricted_tournament_selection(Parents,New[0])
    b_2 = restricted_tournament_selection(Parents,New[1])
    new_1.append(New[0])
    new_1.append(a_2)
    new_2.append(New[1])
    new_2.append(b_2)
    ## Step 4 : selecting best individuals (A'')
    Next_gen_1 = tournament_selection(new_1)
    Next_gen_2 = tournament_selection(new_2)
    Next_gen.append(Next_gen_1)
    Next_gen.append(Next_gen_2)

    ## Step 5: Steady state GA is performed so children replace parents

    temp_pop.remove(Parents[0])
    temp_pop.remove(Parents[1])
    temp_pop.append(Next_gen[0])
    temp_pop.append(Next_gen[1])

    ## Step 6: Peaks are found and solutions are appended to optimal set
    sum =0 
    value = 0

    for i in range(len(temp_pop)-1):
      if temp_pop[i] == temp_pop[i+1]:
        sum += 1
        value = temp_pop[i]
        values.append(value)
    if sum >= len(temp_pop)-1:
      optimal.add(value)
      temp_pop = list(np.arange(0,1,0.1))

    if len(optimal) == len(solution) and [x for x in sorted(optimal)] == [y for y in sorted(solution)] :
      times += 1

## Accuracy is found and optimal set is printed
print(sorted(optimal))
accuracy = float(times*100/n_iter)
print("Accuracy: %d" % accuracy)

"""Plotting graph

"""

import matplotlib.pyplot as plt
import numpy as np



x = np.linspace(0,1,10000)
def f(x):
  return float(np.sin(5*np.pi*float(x))**6)
f2 = np.vectorize(f)
x2 = np.array(sorted(optimal))
y = [1]*len(optimal)

# setting the axes
fig = plt.figure()

# plot the functions
plt.plot(x,f2(x),color='black')
plt.plot(x2,y,'o',color = 'red')

# show the plot
plt.show()