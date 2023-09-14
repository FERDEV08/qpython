# -*- coding: utf-8 -*-
capa = QgsVectorLayer("D:/curso_qpy/shp/Shapes/estados.shp","Estados","ogr")
print (" ---------------------------------")
print ("Listado de Campos de la capa")
print (" ")
"""for campo in capa.fields(): #Obtener Informacion de la Estructura de la Tabla
 print (campo.name(), campo.typeName())"""

registros = capa.getFeatures()
for r in registros:
    """attrs = r.attributes()
    print(attrs)"""
    print("OID: ",  r.id())
    print("Clave GEO: ", r['CVEGEO'])
    print("Clave ENT: ", r[1])
    print("Nombre Estado:  ", r[2])
    print("Area: ",str(r['Shape_AREA']))
    print('/n')