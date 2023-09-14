#scriptOperaciones
d = QgsDistanceArea()
d.setEllipsoid('WGS84')
capa = QgsProject.instance().mapLayersByName('estados')[0]
query = '"NOMGEO" LIKE \'C%\''
registros = capa.getFeatures(QgsFeatureRequest().setFilterExpression(query))

for r in registros:
    geom = r.geometry()
    print(r.attribute('NOMGEO'))
    print("Perimetros (m):", d.measurePerimeter(geom))
    print("Area(m2):", d.measureArea(geom))
    print("Area(km2):")