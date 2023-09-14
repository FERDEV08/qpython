
le = QgsVectorLayer(r"D:\curso_qpy\shp\Shapes\FM_EJEVIAL\30001e.shp")
request = QgsFeatureRequest().setFilterExpression('"CVEVIAL"')
it = le.getFeatures(request)
    
ids = [i.id() for i in it]
idx = le.dataProvider().fieldNameIndex("CVEVIAL")
cl_eje = le.uniqueValues(idx)


lfm = QgsVectorLayer(r"D:\curso_qpy\shp\Shapes\FM_EJEVIAL\30001fm.shp")
request = QgsFeatureRequest().setFilterExpression('"CVEVIAL"')
it = lfm.getFeatures(request)
    
ids = [i.id() for i in it]
idx = lfm.dataProvider().fieldNameIndex("CVEVIAL")
cl_fm = lfm.uniqueValues(idx)


print("Las claves viales de Frente de Manzana (30001fm) que no está en la capa de eje Vial (30001e): ")
print(cl_fm-cl_eje)