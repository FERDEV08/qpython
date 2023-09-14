import sqlite3
MESSAGE_CATEGORY = 'POSGIS_SQLITE' 
layerconsulta = None


def genera_poligonocaneva():
    geompolygonowkt = "POLYGON((-102.61059184481686657 22.14161563870987948, -102.18059887394691998 22.13951811202271003, -102.18059887394691998 21.81230394882411616, -102.60849431812970067 21.81230394882411616, -102.61059184481686657 22.14161563870987948))"
    geomepoly = QgsGeometry.fromWkt (geompolygonowkt)
    feat = QgsFeature();
    feat.setGeometry(geomepoly) #Se agrega la geometria al registro con el metodo setGeometry de la clase QgsFeature
    pr_polygono.addFeature(feat) #Se agrega el registro a la clase QgsVectorLayer   


def consultapostgis ():   
     conn = sqlite3.connect("D:/Curso_II/areas_geoestadisticas/areas_geoestadisticas.gpkg")
     cursor = conn.cursor()
     conn.enable_load_extension(True)#activa la carga de exensiones de Sqlite
     conn.load_extension("mod_spatialite")
     conn.execute('SELECT InitSpatialMetaData(1);')       
     #Grados la medida del buffer
     sql = "SELECT ST_AsText(ST_Buffer(CastAutomagic(geom),5)) AS geom, cve_ent from servicios_informacion_complementaria_de_tipo_puntual where ST_Intersects(SetSRID(ST_GeomFromText('POLYGON((-102.61059184481686657 22.14161563870987948, -102.18059887394691998 22.13951811202271003, -102.18059887394691998 21.81230394882411616, -102.60849431812970067 21.81230394882411616, -102.61059184481686657 22.14161563870987948))'), 6365), CastAutomagic(geom)) limit 1"
     cursor.execute(sql)#Ejecuta la consulta y regresa una tabla con el resultado de la consulta
     print ("Nombre de los Campos")
     for tupla in cursor.description: ## Muestra los nombres de los campos de la tabla resultante de la consulta 
         print (tupla[0])
     #Se crea una lista en la cual se agregaran los campos que contendra la clase de tipo QgsVectorLayer (point_layer)
     listaQgsField = []    
     listaQgsField.append (QgsField("cve_ent",QVariant.String,'', 2, 0))  
     #Se agrega al dataProvider del nuestro clase point_layer los atributos que tendra
     pr.addAttributes(listaQgsField)  
     #Se actualiza la clase point_layer con los atributos que se le agregaron
     point_layer.updateFields()       
     rows = cursor.fetchall()    
     #print ("total",len(rows))    
     con = 0
     for row in rows: 
         feat = QgsFeature(); #Se instancea un clase de tipo QgsFeature() para almcenar la informacion geometrica y tabular en un registro
         geometria = QgsGeometry.fromWkt (row [0]) #se utiliza el metodo fromWkt de la clase QgsGeometry para convertir el WKT en geometria de QGIS
         feat.setGeometry(geometria) #Se agrega la geometria al registro con el metodo setGeometry de la clase QgsFeature
         feat.setAttributes([row [1]])#Se agrega los atributos al registro con el metodo setAttributes de la clase QgsFeature             
         pr.addFeature(feat) #Se agrega el registro a la clase QgsVectorLayer   
         con = con + 1
     conn.close()     #Close the database connection
     print ("Conteo : ",point_layer.featureCount())      
     genera_poligonocaneva()
   

def do_task(task, wait_time):
    global pathname
    QgsMessageLog.logMessage('Started task {}'.format(task.description()),
                             MESSAGE_CATEGORY, Qgis.Info)                          
    print ("Inicia Proceso")
    consultapostgis ()
    
    print ("Termina Proceso")        
    return {'total': 0, 'iterations': 0, 'task': task.description()}      

  
def completed(exception, result=None):
    if exception is None:
        if result is None:
            QgsMessageLog.logMessage(
                'Completed with no exception and no result '\
                '(probably manually canceled by the user)',
                MESSAGE_CATEGORY, Qgis.Warning)
        else:
            
            QgsProject.instance().addMapLayer(poligono_layer)             
            QgsProject.instance().addMapLayer(point_layer)  
            QgsMessageLog.logMessage(
                'Task {name} completed\n'
                'Total: {total} ( with {iterations} '
                'iterations)'.format(
                    name=result['task'],
                    total=result['total'],
                    iterations=result['iterations']),
                MESSAGE_CATEGORY, Qgis.Info)
    else:
        QgsMessageLog.logMessage("Exception: {}".format(exception),
                                 MESSAGE_CATEGORY, Qgis.Critical)
        raise exception

#cambiar a polygon para buffer o en point para filtro de puntos
point_layer = QgsVectorLayer("Polygon?crs=epsg:6365", "servicios_informacion_complementaria_de_tipo_puntual", "memory") 
pr = point_layer.dataProvider()
poligono_layer = QgsVectorLayer("Polygon?crs=epsg:6365", "Caneva", "memory") 
pr_polygono = poligono_layer.dataProvider()
task1 = QgsTask.fromFunction(u'Catalago cpu 1', do_task,
                             on_finished=completed, wait_time=1)
QgsApplication.taskManager().addTask(task1) 












