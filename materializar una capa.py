print("\Inicia Proceso")
layer_existente = QgsProject.instance().mapLayersByName('estados_wgs84')[0]

filtro_expresion = QgsExpression('"CVEGEO"= \'01\' OR "CVEGEO" =\'14\' OR "CVEGEO" =\'32\'')
contexto_expresion = QgsExpressionContext()
contexto_expresion.setFields(layer_existente.fields())
filtro_expresion.prepare(contexto_expresion)

solicitud_caracteristicas = QgsFeatureRequest().setFilterExpression(filtro_expresion.expression())

layer_materializada = layer_existente.materialize(solicitud_caracteristicas)

if layer_materializada.isValid():
    QgsProject.instance().addMapLayer(layer_materializada)
else:
    print("\nCapa materializada aggregada al lienzo.")

print("\n Finaliza Proceso")