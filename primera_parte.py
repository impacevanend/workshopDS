import pandas as pd
import numpy as np


data = pd.read_csv('insuficiencia_cardiaca.csv')

ages = np.array(data['age'])

average_age = np.mean(ages)
print(f"El promedio de edad es: {average_age}")