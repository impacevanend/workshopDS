import requests

def descargar_dataset(url, nombre_archivo):
 
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(respuesta.text)
        print(f"Archivo '{nombre_archivo}' guardado con éxito.")
    else:
        print(f"Error al descargar el archivo. Código de estado: {respuesta.status_code}")


url_dataset = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"


nombre_archivo_csv = "heart_failure_dataset.csv"

descargar_dataset(url_dataset, nombre_archivo_csv)