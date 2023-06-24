num = int(input("Insira o número de termos da série de Fibonacci:"))
texto = ""
termo = 1
termo2 = 0
soma = 0

i = 0
while i != num:
  i = i+1

  if texto != "":
    texto += ", "
  
  soma = termo + termo2

  texto = texto + str(soma)
  
  termo = termo2
  termo2 = soma

print(texto)
