import sqlite3

# Ruta al archivo GeoPackage y nombre de la capa shapefile
ruta_geopackage = 'D:/Curso_II/areas_geoestadisticas/areas_geoestadisticas.gpkg'
nombre_capa_shapefile = 'areas_geoestadisticas_municipales'

# Conectar a la base de datos del GeoPackage
conexion = sqlite3.connect(ruta_geopackage)

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Obtener el nombre de la tabla de la capa shapefile
consulta_tabla = "SELECT table_name FROM gpkg_contents WHERE table_name = 'areas_geoestadisticas_municipales'"
cursor.execute(consulta_tabla)
tabla_capa_shapefile = cursor.fetchone()

# Verificar si la capa shapefile existe en el GeoPackage
if tabla_capa_shapefile:
    # Eliminar la entrada de la capa shapefile de las tablas de metadatos
    consulta_eliminar_metadatos = "DELETE FROM gpkg_contents WHERE table_name = 'areas_geoestadisticas_municipales'"
    cursor.execute(consulta_eliminar_metadatos)

    # Eliminar la tabla de la capa shapefile
    consulta_eliminar_tabla = "DROP TABLE IF EXISTS 'areas_geoestadisticas_municipales'"
    cursor.execute(consulta_eliminar_tabla)

    # Confirmar los cambios en la base de datos
    conexion.commit()
    print("\nCapa shapefile: \n'areas_geoestadisticas_municipales'\n eliminada exitosamente del GeoPackage.")
else:
    print("\nNo se encontró la capa shapefile:\n'areas_geoestadisticas_municipales' en el GeoPackage.")

# Cerrar la conexión con la base de datos
cursor.close()
conexion.close()