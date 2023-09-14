import sqlite3
MESSAGE_CATEGORY = 'POSGIS_SQLITE' 

def genera_poligono(geompolygonowkt):    
    geomepoly = QgsGeometry.fromWkt (geompolygonowkt)
    feat = QgsFeature();
    feat.setGeometry(geomepoly) #Se agrega la geometria al registro con el metodo setGeometry de la clase QgsFeature
    pr_polygono.addFeature(feat) #Se agrega el registro a la clase QgsVectorLayer   

def consultapostgis ():   
     conn = sqlite3.connect("D:/Curso_II/areas_geoestadisticas/areas_geoestadisticas_aguascalientes.gpkg")
     cursor = conn.cursor()
     conn.enable_load_extension(True)#activa la carga de exensiones de Sqlite
     conn.load_extension("mod_spatialite")         
     sql = "SELECT ST_AsText (ST_Buffer(CastAutomagic(geom),0.00018)) AS geom from poligonos_de_manzana where cvegeo = '010010001159A017'"    
     cursor.execute(sql)
     rows = cursor.fetchall()         
     geometriamanzana = ""
     for row in rows: 
         geometriamanzana = row [0]        
     conn.close()     #Close the database connection          
     genera_poligono (geometriamanzana)

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

poligono_layer = QgsVectorLayer("Polygon?crs=epsg:6365", "Buffer", "memory") 
pr_polygono = poligono_layer.dataProvider()
task1 = QgsTask.fromFunction(u'Catalago cpu 1', do_task,
                             on_finished=completed, wait_time=1)
QgsApplication.taskManager().addTask(task1) 