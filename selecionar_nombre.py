layer = QgsProject.instance().layerStore().mapLayersByName('estados_wgs84')[0]
#layer.selectAll()
#layer.removeSelection()
#layer.selectByExpression('"CVEGEO"=\'01\' OR "CVEGEO"= \'32\'OR "CVEGEO" = \'14\'')
selectionName = layer.getFeatures(QgsFeatureRequest().setFilterExpression('"CVEGEO" = \'01\''))
feature = next(selectionName)
print(feature['NOMGEO']+  "-" + str(feature.id()))
print(feature.geometry())
print(feature.geometry().asWkt())