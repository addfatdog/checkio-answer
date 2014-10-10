import math
# using the formula here http://en.wikipedia.org/wiki/Triangle
def simple_areas(*arg):
  if len(arg) == 1:
    area = ((arg[0] / 2.0) ** 2) * math.pi
  elif len(arg) == 2:
    area = arg[0] * arg[1]
  else:
    operator_a = sum([i * i for i in arg]) ** 2
    operator_b = 2 * (sum([i ** 4 for i in arg]))
    area = math.sqrt(operator_a - operator_b) / 4.0
  return round(area, 2)