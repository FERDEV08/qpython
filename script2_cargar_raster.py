# -*- coding: utf-8 -*-
#from PyQt5.QtCore import QFileInfo
#Objeto QFileInfo que contenga la ruta desde donde el proyecto será cargado
fileName = "D:\curso_qpy\shp\Raster\wsiearth.tif"
fileInfo = QFileInfo(fileName)
baseName = fileInfo.baseName() # Devuelve el nombre base del archivo sin la ruta
mylayer = QgsRasterLayer(fileName, baseName) #Crea un Objeto Raster
QgsProject.instance().addMapLayer(mylayer)