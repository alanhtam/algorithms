import math
import random
import copy

graph = {}
with open('kargerMinCut.txt', 'r') as f:
  for line in f:
    string = line.strip().split()
    index = int(string[0])
    graph[index] = {}
    for i in range(1, len(string)):
      target = int(string[i])
      if target in graph[index]:
        graph[index][target] += 1
      else:
        graph[index][target] = 1

def add_to_dict(dict_, key, value):
  dict_[key] = dict_.setdefault(key, 0) + value

def contract(graph):
  random.seed()
  while len(graph) > 2:
    source = random.sample(graph.keys(), 1)[0]
    target = random.sample(graph[source].keys(), 1)[0]
    for tot in graph[target]:
      graph[tot].pop(target)
      if tot != source:
        add_to_dict(graph[source], tot, graph[target][tot])
        add_to_dict(graph[tot], source, graph[target][tot])
    graph.pop(target)
  return graph.values()[0].values()[0]

print graph.keys()