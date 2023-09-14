layer = QgsProject.instance().layerStore().mapLayersByName('estados_wgs84')[1]
idx = layer.fields().indexFromName("CVE_ENT")
claves = layer.uniqueValues(idx)
print(claves)