def Média(lv):
  return sum(lv) / len(lv)

def Moda(lv):
  pass
  
def Mediana(lv):
  lv.sort()
  if len(lv) % 2 == 0:
    return (lv[int(len(lv) / 2) - 1] + lv[int(len(lv) / 2)]) / 2
  else:
    return lv[int(len(lv) / 2 - 0.5)]
  
valores = [
  74,
  101,
  68,
  97, 
  8
]
#print(f"Moda: {Moda(valores)}")
print(f"Média: {Média(valores)}")
print(f"Mediana: {Mediana(valores)}")
