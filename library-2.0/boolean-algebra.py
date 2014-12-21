def boolean(x, y, operator):
  operator_dict = {}
  
  operator_dict["conjunction"] = lambda a,b: 1 if a and b else 0
  operator_dict["disjunction"] = lambda a,b: 0 if a + b == 0 else 1
  operator_dict["implication"] = lambda a,b: 1 if a - 1 or b else 0
  operator_dict["exclusive"] = lambda a,b: (a + b) % 2
  operator_dict["equivalence"] = lambda a,b: 1 if a == b else 0
  
  return operator_dict[operator](x, y)
