import pandas as pd

data = pd.read_csv('insuficiencia_cardiaca.csv')

print(data.dtypes)

smokers = data.groupby('sex')['smoking'].sum()
print(f"Hombres fumadores: {smokers[1]}")
print(f"Mujeres fumadoras: {smokers[0]}")