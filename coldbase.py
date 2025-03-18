from itertools import product
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
lista_cidades = ["Itapetininga", "Tatui", "São Miguel Arcanjo", "Capela do Alto", "Sorocaba", "Buri"]
lista_frutas = ["Banana", "Maçã", "Uva", "Pera", "Morango"]
np.random.seed (42)

df = pd.DataFrame(product(lista_cidades, lista_frutas), columns = ["lista_cidades","lista_frutas",])
df["producao"] = np.random.randint (0, 1000, size=len(df))

soma_frutas = df.groupby("lista_frutas").producao.sum()

soma_frutas.to_csv("soma_frutas.csv", sep = ";", decimal = ",")

g_frutas_conjunto = plt.bar (soma_frutas.index, soma_frutas)

plt.savefig('soma_frutas.pdf')

morangos = df[df.lista_frutas == "Morango"]
_ = plt.pie(morangos.producao, labels=morangos.lista_cidades, autopct="%.0f%%")
plt.show()

sorocaba = df[df.lista_cidades == "Sorocaba"]
macas_sorocaba = sorocaba[sorocaba.lista_frutas == "Maçã"].producao
chance_maca_sorocaba_teorica = macas_sorocaba / sorocaba.producao.sum ()


repeticoes = [10, 100, 1000, 10000, 100000, 1000000]
frutas_pool = sorocaba.lista_frutas.repeat (sorocaba.producao).reset_index(drop=True)
chance_maca_sorocaba_sim = []
for n in repeticoes:
    np.random.seed(42)
    indices = np.random.randint(0, len(frutas_pool), size = n)
    caixas_selecionadas = frutas_pool.iloc[indices]  
    macas_selecionadas = (caixas_selecionadas == "Maçã").sum()
    chance_maca_sorocaba_sim.append(macas_selecionadas/n)