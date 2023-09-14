import sqlite3
from datetime import datetime

MESSAGE_CATEGORY = 'Genera shape edicion' 

def cambianombresgeopacakage ():
    geopPath = 'D:/Curso_II/Insumos_gpkg/F16D31.gpkg'
    consqlite = sqlite3.connect(geopPath) ##Conectamos con la bd del gpkg
    cursorsqlite = consqlite.cursor()
    layer = QgsVectorLayer(geopPath ,"og","ogr")
    subLayers = layer.dataProvider().subLayers()
    for subLayer in subLayers: ##Recorremos todas las capas del gpkg 
      layername = subLayer.split('!!::!!')[1]      
      if (layername == 'altimetria_p'):
        print(f'Cambiando nombre Campos en: {layername}')
        try: 
             ## Cambiamos los nombres de los campos  geom
             newname  = 'OBJECTID'
             oldname  = 'fid'
             query01 = f"alter table {layername} rename {oldname} to {newname};"
             cursorsqlite.execute(query01)
             consqlite.commit() ##  Se hace un commit por cada layer, esto para poder generar su indice espacial
             uri = "%s|layername=%s" % (geopPath, layername,)
             layer = QgsVectorLayer(uri, layername, 'ogr')   
             layer.dataProvider().createSpatialIndex() ## Creamos el indice espacial
             layer.triggerRepaint() ##Guardamos el indice en el layer
             break
        except:
             continue ##Se pone validacion en caso de que una capa no coinicda con el nombre original del campo geom
        #break     
    cursorsqlite.close()
    consqlite.close() 


def do_task(task, wait_time):
    global pathname
    QgsMessageLog.logMessage('Started task {}'.format(task.description()),
                             MESSAGE_CATEGORY, Qgis.Info)                        
    print ("Inicia Proceso Genera shape a Geopackage")
    cambianombresgeopacakage()
    print ("Termina Proceso")        
    return {'total': 0, 'iterations': 0, 'task': task.description()} 


def completed(exception, result=None):
    if exception is None:
        if result is None:
            #QgsProject.instance().addMapLayer(vector) 
            QgsMessageLog.logMessage(
                'Completed with no exception and no result '\
                '(probably manually canceled by the user)',
                MESSAGE_CATEGORY, Qgis.Warning)
        else:
            #QgsProject.instance().addMapLayer(vector) 
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
task1 = QgsTask.fromFunction(u'Catalago cpu 1', do_task,
                             on_finished=completed, wait_time=1)                           
                             
QgsApplication.taskManager().addTask(task1)