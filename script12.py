#Agregar columna
from qgis.core  import QgsVectorLayer, QgsField
capa=QgsVectorLayer(r"D:/curso_qpy/traslapeError_.shp","capaTraslape","ogr")
#capa.dataProvider().addAttributes([QgsField("myId",QVariant.Int),QgsField("myText",QVariant.String)])
#Agregar registros
"""fid=0
attrs={1:6,2:"Hola"}
capa.dataProvider().changeAttributeValues({fid:attrs})"""
#Eliminar columnas
#capa.dataProvider().deleteAttributes([2])

#Borrar registros
capa.dataProvider().deleteFeatures([4])