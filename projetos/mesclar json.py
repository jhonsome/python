dict1= {"valor1": 1, "valor2": 2, "valor3": [8, {"o": 5}], "valor4": {"a": 5, "b": 4, "c": [8, 3, 5, 2]}}  
dict2 = {"valor1": 6, "valor3": [2, 3, [9, 2, 3], {"o": 7}], "valor4": {"a": 1, "b": 4, "c": [7, 3]}, "uu": [6, 3]} 

def merge(d1, d2, tp = dict):
  if tp == dict:
    for key, value in d2.items():
      if type(value) == list or type(value) == dict:
        try:
          d1[key]
        except KeyError:
          d1[key] = value
        else:
          merge(d1[key], d2[key], list if type(value) == list else dict)
      else:
        d1[key] = value
  elif tp == list:
    for value in d2:
      d1.append(value)
  return d1
  
print(merge(dict1, dict2))
