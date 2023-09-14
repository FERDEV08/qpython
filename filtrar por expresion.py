print("\nInicia proceso")
from qgis.core import QgsExpression, QgsFeatureRequest

#Obtener la capa activata
capa_activa = iface.activeLayer()

#Definir la expresión de filtro con dos campos
expresion_filtro = QgsExpression("CVEGEO = '01' OR  CVEGEO = '32'")

solicitud_caracteristicas = QgsFeatureRequest(). setFilterExpression(expresion_filtro.expression())
caracteristicas_filtradas = capa_activa.getFeatures(solicitud_caracteristicas)

for caracteristica in caracteristicas_filtradas:
    print("\n", caracteristica.attributes())


print("\nTermina Proceso")