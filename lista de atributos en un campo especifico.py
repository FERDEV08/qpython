layer = QgsProject.instance().layerStore().mapLayersByName('estados_wgs84')[0]
for feature in layer.getFeatures():
    #print(feature)
    print(feature.id())
    print(feature['NOMGEO'])
    print('-----')