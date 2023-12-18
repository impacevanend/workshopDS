import pandas as pd
import numpy as np

data = pd.read_csv('insuficiencia_cardiaca.csv')

ages = np.array(data['age'])

average_age = np.mean(ages)
print(f"El promedio de edad es: {average_age}")

df_deceased = data[data['DEATH_EVENT'] == 1]
df_survived = data[data['DEATH_EVENT'] == 0]

average_age_deceased = df_deceased['age'].mean()
average_age_survived = df_survived['age'].mean()

print(f"El promedio de edad de las personas fallecidas es: {average_age_deceased}")
print(f"El promedio de edad de las personas que sobrevivieron es: {average_age_survived}")