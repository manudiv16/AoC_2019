count = 0
encapsule = []
for x in range(134792,675810):
    digit=str(x)
    sor = sorted(digit)
    sort = "".join(sor)
    if digit==sort:
        encapsule.append(digit)
        count=count+1


resposta = []

for digits in encapsule:
    count = 0
    
    dianterior = ""
    n=0
    for di in digits:

        if di==dianterior:
            count = count + 1
            if n==5:
                if count==1:
                    if digits not in resposta:
                        resposta.append(digits)
                        
        else:
            if count == 1 :
                if digits not in resposta:
                        resposta.append(digits)
            count = 0
        n=n+1
        
        dianterior = di
    
print(resposta)
print (len(resposta))