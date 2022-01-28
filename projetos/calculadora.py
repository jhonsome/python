from math import *

operação = "√(-3!) + √(39)"
limite = 100

c = 0
while True:
  if "f(" in operação:
    f = operação[operação.index("f("):operação.index(")") + 1]
    ic = {n.split("=")[0].strip(): n.split("=")[1].strip() for n in f[f.index("(") + 1:f.index(")")].split(",")} 
    operação = operação.replace(f, "").strip()
    for k, v in ic.items():
      operação = operação.replace(k, v)
  elif "|" in operação:
    op = operação[operação.index("|"):operação.index("|", operação.index("|") + 1) + 1]
    print(op)
    operação = operação.replace(op, str(abs(float(op.replace('|', ''))))) 
  elif "!" in operação:
    op = operação[operação.index("!")::-1][::-1]
    operação = operação.replace(op, str(factorial(float(op.replace('!', ''))))) 
    print(operação)
  elif "√" in operação:
    op = operação[operação.index("√"):][:operação.index(")") + 1]
    print(op[op.index('(') + 1:op.index(')')])
    operação = operação.replace(op, str(sqrt(float(op[op.index('(') + 1:op.index(')')])))) 
  else:
    break
  c += 1 
  if c >= limite:
    raise Exception("Erro ao solucionar")

print(operação)
print(eval(operação)) 
