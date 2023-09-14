#Importamos los módulos necesarios
from time import sleep
from qgis.core import *
from processing.tools import *
import processing
from qgis.core import QgsApplication, QgsTask, QgsMessageLog, Qgis
from PyQt5 import QtWidgets, QtSql

#Definimos la ruta de la carpeta que contiene los archivos shape
path = "D:/Curso_II/Insumos/multigeometrias"       
#Definimos una constante MESSAGE_CATEGORY que se utilizará como categoría de mensaje para registrar eventos relacionados con la tarea
MESSAGE_CATEGORY = 'Revisa Multigeometrias'   

#Definimos una función llamada listaShapes que recorre la carpeta especificada y devuelve una lista de rutas de los archivos shape
def listaShapes ():     
        lista = []
        for root, dirs, files in os.walk(path):
            swmsg = False
            for archivo in files:
                if (archivo.endswith('shp')):         
                    lista = lista + [root+"/"+archivo]                       
                    #break                         
        return lista       

#Definimos una función llamada verificaMultiSingleGeoemetry que recibe una lista de rutas de archivos shape 
#y verifica si cada shape tiene una geometría múltiple o una geometría simple
def verificaMultiSingleGeoemetry(lista):
    for shape in lista:
           print (shape)
           layer = QgsVectorLayer(shape,"Vectorial","ogr") 
           features = layer.getFeatures()
           for f in features:
               geom = f.geometry()
               tipoGeom = geom.wkbType() # Obtiene el codigo del tipo de geometria
               print ("ID            : " + str (f.id()))
               if QgsWkbTypes.isMultiType(tipoGeom):
                   print ("tipo de Geometria : "+geom.asWkt() [0: geom.asWkt().find("(") ])  
                   print("\nContiene Multiple Geometrias")       
               elif QgsWkbTypes.isSingleType(tipoGeom):
                   print ("tipo de Geometria : "+geom.asWkt() [0: geom.asWkt().find("(") ])  
                   print("\nContiene Geometria Simple")   
               #break  
           print (" ")                
           print (" ")

#Definimos una función llamada do_task que representa la tarea que se ejecutará en segundo plano. 
#Esta función llama a listaShapes y verificaMultiSingleGeoemetry para procesar los archivos shape 
#y mostrar los resultados por pantalla. Al final, retorna un diccionario con información sobre la tarea realizada
def do_task(task, wait_time):
    print ("Inicia Proceso")
    QgsMessageLog.logMessage('Started task {}'.format(task.description()),
                             MESSAGE_CATEGORY, Qgis.Info)
    #QgsProject.instance().removeAllMapLayers()  
    listashapes = listaShapes ()
    verificaMultiSingleGeoemetry(listashapes)
    print ("Termina Proceso")        
    return {'total': 0, 'iterations': 0, 'task': task.description()}      

#Definimos una función llamada completed que se ejecutará cuando la tarea haya finalizado. 
#Esta función registra mensajes de información o errores según el resultado de la tarea
def completed(exception, result=None):
    if exception is None:
        if result is None:
            QgsMessageLog.logMessage(
                'Completed with no exception and no result '\
                '(probably manually canceled by the user)',
                MESSAGE_CATEGORY, Qgis.Warning)
        else:
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

#En resumen, estas líneas de código crean una tarea en segundo plano utilizando la función do_task 
#y la agregan al administrador de tareas para su ejecución. Una vez que la tarea se complete, 
#la función completed se ejecutará para manejar los resultados o cualquier error.
task1 = QgsTask.fromFunction(u'Encuentra Multigeoemtrias cpu 1', do_task,
                             on_finished=completed, wait_time=1)
QgsApplication.taskManager().addTask(task1) 