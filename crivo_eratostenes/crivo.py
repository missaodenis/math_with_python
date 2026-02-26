import math 

numeros = [] 

for i in range(101): # Criando uma posição correspondente dos índices aos números de 0 a 100

    numeros.append(True) # Assumindo que todos esses números são primos

i = 2 # Sabendo que 0 e 1 não são primos, o 2 é o primeiro elemento da nossa lista

while(i <= int(math.sqrt(100))): # Testando apenas até a raiz quadrada de 100
   
    if numeros[i]: # Selecionando os índices marcados como verdadeiros
        
        for j in range(i*2, 101, i): # Escolhendo todos múltiplos de i (i=2 -> 4, 6, 8... / i=3 -> 6, 9, 12... e etc.)
        
            numeros[j]=False # Marcando esses valores como não primos
            
    i = i+1 # Avançando para o próximo índice
    
for i in range(2,101): # Correspondendo esses índices com os valores de 2 a 100
    
  if numeros[i]: # Selecionando os índices marcados como verdadeiros
      
      print(i) 
     