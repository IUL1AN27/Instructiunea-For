n=int(input('Introduceti numarul'))
suma=0
for i in range(1,n):
    if(i%3==0 and i%5==0):
        suma=suma+i
print(suma)