#Importamos los módulos necesarios
from functools import partial
from qgis.core import (QgsTaskManager, QgsMessageLog,
                       QgsProcessingAlgRunnerTask, QgsApplication,
                       QgsProcessingContext, QgsProcessingFeedback,
                       QgsProject)

#Definimos una constante MESSAGE_CATEGORY que se utilizará como categoría de mensaje para registrar eventos relacionados con la tarea
MESSAGE_CATEGORY = 'Puntos_Aleatorios_5000'

#Definimos una función llamada task_finished que se ejecutará cuando la tarea haya finalizado. 
#Esta función recibe el contexto de procesamiento, un indicador de éxito y los resultados de la tarea
def task_finished(context, successful, results):
    if not successful:
        QgsMessageLog.logMessage('Tarea sin finalizar',
                                 MESSAGE_CATEGORY, Qgis.Warning)
    output_layer = context.getMapLayer(results['OUTPUT'])
    # debido a que getMapLayer no transfiere la propiedad, la capa se eliminará cuando el contexto se salga del alcance 
    #y obtendrá un crash.
    # takeMapLayer transfiere la propiedad para que sea seguro agregarla al proyecto 
    #y darle la propiedad del proyecto.
    if output_layer and output_layer.isValid():
        QgsProject.instance().addMapLayer(
             context.takeResultLayer(output_layer.id()))

#Obtenemos el algoritmo de procesamiento de QGIS que queremos ejecutar.
#En este caso, se utiliza el algoritmo "qgis:randompointsinextent"
alg = QgsApplication.processingRegistry().algorithmById(
                                      'qgis:randompointsinextent')
#Creamos un contexto de procesamiento
context = QgsProcessingContext()
#Creamos una instancia de QgsProcessingFeedback para proporcionar retroalimentación durante el procesamiento
feedback = QgsProcessingFeedback()
#Definimos los parámetros de entrada para el algoritmo de procesamiento
params = {
    'EXTENT': '0.0,10.0,40,50 [EPSG:6365]',
    'MIN_DISTANCE': 0.0,
    'POINTS_NUMBER': 5000,
    'TARGET_CRS': 'EPSG:6365',
    'OUTPUT': 'memory:5000_Puntos_aleatorios '
}
#reamos una instancia de QgsProcessingAlgRunnerTask que representa la tarea de ejecución del algoritmo de procesamiento.
#Le pasamos el algoritmo, los parámetros, el contexto de procesamiento y el objeto de retroalimentación:
task = QgsProcessingAlgRunnerTask(alg, params, context, feedback)
#Conectamos la señal executed de la tarea a la función task_finished, utilizando partial para pasar el contexto de 
#procesamiento como argumento adicional
task.executed.connect(partial(task_finished, context))
#Agregamos la tarea al administrador de tareas de QGIS para que se ejecute en segundo plano:
QgsApplication.taskManager().addTask(task)
print("\nFinalizo Correctamente la tarea en segundo plano")