import processing # Importa la clase para procesar
processing.runAndLoadResults ( "qgis:difference",
                              { 'INPUT': 'D:/curso_qpy/shp/Shapes/resultados/jalisco_buffer.shp',
                              'OVERLAY': 'D:/curso_qpy/shp/Shapes/jalisco.shp',
                              'OUTPUT': 'D:/curso_qpy/shp/Shapes/resultados/jalisco_diferencia.shp'})