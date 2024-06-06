import pandas as pd
import os  # Importar el módulo os para operaciones del sistema operativo


df_categoria = pd.read_csv('C:/Users/ajzvp/OneDrive/Escritorio/AmazonSkills/EntidadesReal1.csv',
                           encoding='utf-8')


columna_entidad = 'Text'
lista_entidades = list(set(df_categoria[columna_entidad]))

# Función para identificar si una palabra es subcadena de otra
def es_subcadena(palabra, lista_palabras):
    for otra_palabra in lista_palabras:
        if palabra != otra_palabra and palabra in otra_palabra:
            return True
    return False

# Filtrar las palabras que no son subcadenas de otras
entidades_no_solapadas = [palabra for palabra in lista_entidades if not es_subcadena(palabra, lista_entidades)]

# Crear un nuevo DataFrame sin solapamientos
df_categoria_sin_solapamientos = pd.DataFrame(entidades_no_solapadas, columns=[columna_entidad])

# Ruta del archivo de destino
archivo_destino = 'C:/Users/ajzvp/OneDrive/Escritorio/AmazonSkills/EntidadesNoSolapadas1.txt'

# Comprobar si el archivo existe y eliminarlo si es necesario
if os.path.exists(archivo_destino):
    os.remove(archivo_destino)

# Guardar el nuevo DataFrame en un archivo CSV
df_categoria_sin_solapamientos.to_csv(archivo_destino, index=False, encoding='utf-8')  # Cambia 'Categoria' por el nombre adecuado

print(f"Archivo guardado como '{archivo_destino}'.")  # Asegúrate de cambiar 'Categoria'