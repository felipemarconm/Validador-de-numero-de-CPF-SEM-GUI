class CPF_VALIDATOR:

    def functionOne(x): 
        w = x.replace('-', '').replace(' ', '').replace('.', '') 
        y = len(w)
        n = w
        s = 0

        for i in range(0,len(n)):
            s = s + int(n[i])
                
        if y == 11 and s == 44:
            print(f'O CPF de número {w[:3]}.{w[3:6]}.{w[6:9]}-{w[9:11]} é verdadeiro.')
            return True
        else:
            print(f'O CPF de número {w} é falso.') 
            return False 


    fOne = functionOne(input('Digite o número do CPF: '))
