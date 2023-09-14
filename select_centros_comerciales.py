print ("Inicia Proceso")
import sqlite3
# Connect to the database
conn = sqlite3.connect("D:/Curso_II/areas_geoestadisticas/areas_geoestadisticas.gpkg")
cursor = conn.cursor()
conn.enable_load_extension(True)#activa la carga de exensiones de Sqllite
conn.load_extension("mod_spatialite")#carga módulos de extensión para este caso se carga mod_spatialite para hacer uso de la funcion CastAutomagic
sql = "SELECT ST_AsText (CastAutomagic(geom)) as geom,cve_ent,geografico,nomserv,tipo,ambito from servicios_informacion_complementaria_de_tipo_puntual where cve_ent = '01' and upper (geografico) = 'CENTRO COMERCIAL'"
cursor.execute(sql)#Ejecuta la consulta y regresa una tabla con el resultado de la consulta
## Fetch the results
rows = cursor.fetchall()
print ("Nombre de los Campos")
for tupla in cursor.description: ## Muestra los nombres de los campos de la tabla resultante de la consulta 
    print (tupla[0])
#Se crea una lista en la cual se agregaran los campos que contendra la clase de tipo QgsVectorLayer (point_layer)
listaQgsField = []    
#Crea una clase del tipo QgsVectorLayer para almacenar datos vectoriales tipo punto en memoria
point_layer = QgsVectorLayer("Point?crs=epsg:6365", "Centros Comerciales", "memory") 
#Se instancea la clase dataprovider 
pr = point_layer.dataProvider()
#listaQgsField.append (QgsField("id",QVariant.Int))  
listaQgsField.append (QgsField("cve_ent",QVariant.String,'', 2, 0))  
listaQgsField.append (QgsField("geografico",QVariant.String,'', 59, 0)) 
listaQgsField.append (QgsField("nomserv",QVariant.String,'', 110, 0))  
listaQgsField.append (QgsField("tipo",QVariant.String,'', 48, 0))  
listaQgsField.append (QgsField("ambito",QVariant.String,'', 6, 0))  
#Se agrega al dataProvider del nuestro clase point_layer los atributos que tendra
pr.addAttributes(listaQgsField)  
#Se actualiza la clase point_layer con los atributos que se le agregaron
point_layer.updateFields()      
for row in rows: ## Itera  sobre los resultados del la consulta 
     feat = QgsFeature(); #Se instancea un clase de tipo QgsFeature() para almcenar la informacion geometrica y tabular en un registro
     geometria = QgsGeometry.fromWkt (row [0]) #se utiliza el metodo fromWkt de la clase QgsGeometry para convertir el WKT en geometria de QGIS
     feat.setGeometry(geometria) #Se agrega la geometria al registro con el metodo setGeometry de la clase QgsFeature
     feat.setAttributes([row [1],row [2],row [3],row [4],row [5]])#Se agrega los atributos al registro con el metodo setAttributes de la clase QgsFeature             
     pr.addFeature(feat) #Se agrega el registro a la clase QgsVectorLayer   
conn.close()     #Close the database connection
print ("Conteo : ",point_layer.featureCount())
QgsProject.instance().addMapLayer(point_layer) 
print ("Termina Proceso")

