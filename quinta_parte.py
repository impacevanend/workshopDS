import pandas as pd

def limpiar_y_preparar_datos(dataframe):
    # Verificar y eliminar valores faltantes
    dataframe.dropna(inplace=True)

    # Verificar y eliminar filas duplicadas
    dataframe.drop_duplicates(inplace=True)

    # Verificar y eliminar valores atípicos (usando el método de rango intercuartílico)
    Q1 = dataframe.quantile(0.25)
    Q3 = dataframe.quantile(0.75)
    IQR = Q3 - Q1
    dataframe = dataframe[~((dataframe < (Q1 - 1.5 * IQR)) | (dataframe > (Q3 + 1.5 * IQR))).any(axis=1)]

    # Crear una columna para categorizar por edades
    condiciones = [
        (dataframe['age'] <= 12),
        (dataframe['age'] <= 19),
        (dataframe['age'] <= 39),
        (dataframe['age'] <= 59),
        (dataframe['age'] > 59)
    ]
    categorias = ['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor']
    dataframe['Categoria_edad'] = pd.cut(dataframe['age'], bins=[0, 12, 19, 39, 59, float('inf')], labels=categorias, right=False)

    return dataframe

# Cargar el dataset
data = pd.read_csv('heart_failure_dataset.csv')

# Limpiar y preparar el dataset
data_limpio = limpiar_y_preparar_datos(data)

# Mostrar una vista previa de los datos limpios
print(data_limpio.head())

# Guardar el resultado como CSV
data_limpio.to_csv('heart_failure_dataset_limpio.csv', index=False)

print("Dataset limpio y preparado guardado como 'heart_failure_dataset_limpio.csv'.")
