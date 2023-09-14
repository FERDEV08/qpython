print ("Inicia Proceso")
import sqlite3
conn = sqlite3.connect("D:/Curso_II/areas_geoestadisticas/areas_geoestadisticas.gpkg")
cursor = conn.cursor()
conn.enable_load_extension(True)#activa la carga de exensiones de Sqllite
conn.load_extension("mod_spatialite")
sql = "SELECT ST_AsText (CastAutomagic(geom)) as geom,cve_ent,cve_mun,nomgeo from areas_geoestadisticas_municipales where cve_ent = '01' or cve_ent = '02'"
cursor.execute(sql)#Ejecuta la consulta y regresa una tabla con el resultado de la consulta
rows = cursor.fetchall()
print ("Nombre de los Campos")
for tupla in cursor.description: ## Muestra los nombres de los campos de la tabla resultante de la consulta 
    print (tupla[0])
listaQgsField = []
polygon_layer=QgsVectorLayer("Polygon?crs=epsg:6365", "filtro_cve_ent", "memory") 
pr = polygon_layer.dataProvider()
listaQgsField.append (QgsField("cve_ent",QVariant.String,'', 2, 0))  
listaQgsField.append (QgsField("cve_num",QVariant.String,'', 59, 0)) 
listaQgsField.append (QgsField("nom_geo",QVariant.String,'', 110, 0))  
pr.addAttributes(listaQgsField)
polygon_layer.updateFields()
for row in rows:
    feat = QgsFeature();
    geometria = QgsGeometry.fromWkt (row [0]) #se utiliza el metodo fromWkt de la clase QgsGeometry para convertir el WKT en geometria de QGIS
    feat.setGeometry(geometria) #Se agrega la geometria al registro con el metodo setGeometry de la clase QgsFeature
    feat.setAttributes([row [1],row [2],row [3]])
    pr.addFeature(feat)

conn.close()     #Close the database connection
print ("Conteo : ",polygon_layer.featureCount())
QgsProject.instance().addMapLayer(polygon_layer) 
print ("Termina Proceso")