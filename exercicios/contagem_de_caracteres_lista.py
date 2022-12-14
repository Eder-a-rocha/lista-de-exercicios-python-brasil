def contar_caracteres(s):
    """Função que conta os caracteres de uma string
    
    Ex: 
    >>> contar_caracteres('renzo')
    r: 1
    e: 1
    n: 1
    z: 1
    0: 1
    >>> contar_carateres('banana')
    b: 1
    a: 3
    n: 2
    
    :param s: string a ser contada
    :return:
    """
    caracteres_ordenados = sorted(s)
    
    caracter_anterior = caracteres_ordenados[0]
    contagem = 1
    
    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}: {contagem}')     
            caracter_anterior = caracter
            contagem = 1
    
    print(f'{caracter_anterior}: {contagem}')  
    
if __name__ == '__main__':
    contar_caracteres('renzos')      
    print()
    contar_caracteres('banana')  
            
            