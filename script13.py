# Importar módulos necesarios
from qgis.core import QgsProject

 
# Obtener la capa a eliminar por su nombre o ID
layer_name = "capaTraslape"  # Reemplaza con el nombre de tu capa
layer_id = QgsProject.instance().mapLayersByName(layer_name)[0].id()

# Eliminar la capa
QgsProject.instance().removeMapLayer(layer_id)