from random import randint 

while True:
  print("----------\n[j] para jogar o dado\n[e] para fechar")
  res = str(input().replace(" ", "").lower())
  if res == "j":
    print(f"\nvalor do dado: {randint(1, 6)}")
  if res == "e":
    break
  print("----------\n")
