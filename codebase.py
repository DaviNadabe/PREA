##hackear_santander = true
##hackear_governo = em progresso...
##hackear_tigurinho = 99% completo
##import itertools
import numpy as hp
import seaborn as sns
##import random
from itertools import product
import pandas as pd
import matplotlib.pyplot as plt
listacity = ['Itapetinigga', 'Tatuí', 'São Miguel Arcanjo', 'Capela do Alto', 'Sorocaba', 'Buri'] 
listafruit = ['Banana', 'Maçã', 'Pera', 'Uva', 'Morango']
#listacombinada = listacity + listafruit
#print(listacombinada)

df = pd.DataFrame (product (listacity, listafruit), columns = ['cidades', 'frutas']) 
hp.random.seed(42)
df ['produção' ]=hp.random.randint(0, 1000, size=len (df)) 
soma_frutas=df.groupby('frutas')['produção' ].sum() 
soma_frutas.to_csv('soma_frutas.csv', sep=';', decimal=',')

print(df)
print(soma_frutas)

plt.bar(listafruit,soma_frutas)
plt.xlabel('frutas')
plt.ylabel('produção')
plt.show()

plt.savefig('graphics.pdf')
