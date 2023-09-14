from qgis.core import QgsVectorLayer

# Ruta al archivo shapefile
ruta_shapefile = "D:\Curso_II\Insumos\estados_wgs84.shp"

# Cargar la capa shapefile
capa = QgsVectorLayer(ruta_shapefile, "nombre_de_capa", "ogr")

if capa.isValid():
    campos = capa.fields()
    
    #"BLOB" significa "Binary Large Object" (Objeto Binario Grande, en español).
    tipo_campos = {
        0: "String",
        1: "Integer",
        2: "Double",
        3: "Date",
        4: "Time",
        5: "DateTime",
        6: "Decimal",
        7: "Boolean",
        10: "Blob"
    }
    
    for campo in campos:
        nombre = campo.name()
        tipo_numero = campo.type()
        
        tipo = tipo_campos.get(tipo_numero, "Desconocido")
        
        if campo.length() > 0:
            longitud = campo.length()
            print(f"Campo: {nombre}, Tipo: {tipo}, Longitud: {longitud}")
        else:
            print(f"Campo: {nombre}, Tipo: {tipo}")
else:
    print("Error al cargar la capa shapefile.")
