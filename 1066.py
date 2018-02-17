par = 0
impar = 0
positivo = 0
negativo = 0
x = 0

while x < 5:
    a = int(input())
    if a % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
    if a > 0:
        positivo = positivo + 1
    elif a < 0:
        negativo = negativo + 1
    x = x + 1
print("%d valor(es) par(es)" %par)
print("%d valor(es) impar(es)" %impar)
print("%d valor(es) positivo(s)" %positivo)
print("%d valor(es) negativo(s)" %negativo)