import processing #Importa la clase para procesar
processing.runAndLoadResults("qgis:buffer",
 {'INPUT': "D:/curso_qpy/shp/Shapes/jalisco.shp",
 'DISTANCE': 10.0,
 'SEGMENTS': 5,
 'DISSOLVE': False,
 'OUTPUT': "D:/curso_qpy/shp/Shapes/resultados/jalisco_buffer.shp"})