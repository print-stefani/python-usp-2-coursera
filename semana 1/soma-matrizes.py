#Função que soma as duas matrizes, retornando falso caso o tamanho delas sejam distintos.

def soma_matrizes(m1, m2):
    linhas_m1 = len(m1)
    #le o tamanho das linhas da matriz 1
    linhas_m2 = len(m2)
    #le o tamanho das linhas da matriz 2
    
    if linhas_m1 != linhas_m2:
        return False
      #condição para verificar se as linhas das matrizes são diferentes, retornando False
      
    colunas_m1 = len(m1[0])
    #le o tamanho das colunas da matriz 2
    colunas_m2 = len(m2[0])
    #le o tamanho das colunas da matriz 2
    
    if colunas_m1 != colunas_m2:
        return False
       #condição para verificar se as colunas das matrizes são diferentes, retornando False
        
    soma = [] #cria uma lista para armazenar as somas das matrizes
    
    for i in range(linhas_m1):   #numero de linhas da matriz 
        linha = []   
        #lista nova para armazenar a soma
        
        for j in range(colunas_m1): #numero de coluna da matriz
            linha.append(m1[i][j] + m2[i][j])
            #soma as matrizes e adiciona na nova lista criada acima 
            
        soma.append(linha)
        #lista linha adicionada na lista soma 
        
    return soma
