#Interseccion

import processing #importa la clase para procesar

processing.runAndLoadResults("qgis:intersection",
                            {'INPUT': 'D:/curso_qpy/shp/Shapes/ZONA_DE_HELADAS.shp',
                            'OVERLAY':  'D:/curso_qpy/shp/Shapes/aguascalientes.shp',
                            'OUTPUT': 'D:/curso_qpy/shp/Shapes/resultados/ags_isoyeta.shp'})