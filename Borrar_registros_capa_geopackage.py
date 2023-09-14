print("Inicia Proceso")
import sqlite3
from qgis.core import QgsVectorLayer
from qgis.core import QgsProject

# Ruta al archivo GeoPackage y nombre de la tabla
ruta_geopackage = 'D:/Curso_II/areas_geoestadisticas/areas_geoestadisticas.gpkg'
nombre_tabla = 'areas_geoestadisticas_municipales'
cve_ent = '11'


# Conectar a la base de datos del GeoPackage
conexion = sqlite3.connect(ruta_geopackage)

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Borrar todos los registros de la tabla que contengan la cve_ent 01 (aguascalientes)
sql = "DELETE FROM '{}' where cve_ent='{}' ".format(nombre_tabla,cve_ent)
cursor.execute(sql)
conexion.commit()

# Obtener la cantidad de registros borrados
registros_borrados = cursor.rowcount
print("\nSe han borrado {} registros de la tabla:\n '{}'\n donde la cve_ent es igual a '{}'.".format(registros_borrados, nombre_tabla,cve_ent))

# Cerrar la conexión con la base de datos
cursor.close()
conexion.close()
print ("\nTermina Proceso")