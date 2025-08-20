e  = [input('Digite a expressao: ')]
f = []
x = []
con1 = con2 = 0
fecha = 0
for pos,letra in enumerate(e[0]):
    f.append(letra)
    if letra in '()':
        if letra =="(":
            con1 +=1
        else:
            con2 +=1
        x.append(letra)
    
print(x)
if x[0] == '(' and x[-1] == ')' and con1 == con2:
    print('EXPRESSAO VALIDA')
else:
    print('EXPRESSAO INVALIDA')

    

#()()()
#(())()
#(()(()))
#())(()



    
    

#print(f.count('('))
#print(f.count(')'))


            

#print(f"{e.index('(')}")
#print(e.count('('))

    
        

    




