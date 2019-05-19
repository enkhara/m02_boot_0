#recursividad =funcioón que para repetirse se invoca a si misma i se llama a si misma

def retrocontador(e):
    print('{},'.format(e), end ='')
    if e > 0:
        retrocontador(e-1)
    
retrocontador(10)


    