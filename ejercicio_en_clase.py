def localidadisla(cveent, cvemun, cveloc):
    print("Clave a consultar:  "+cveent + cvemun + cveloc)
    layer = QgsVectorLayer(r"D:\curso_qpy\shp\Shapes\locs_islas_feb2018.dbf")
    request = QgsFeatureRequest().setFilterExpression('"CVE_ENT"=\''+""+cveent+'\'AND "CVE_MUN"=\''+""+cvemun+'\'and "CVE_LOC"=\''+""+cveloc+'\'')
    it = layer.getFeatures(request)
    
    ids = [i.id() for i in it]
    idx = layer.dataProvider().fieldNameIndex("CVE_ENT")
    claves = layer.uniqueValues(idx)
    print(sorted(claves))
    print("Total CVE_ENT: "+str(len(claves)))
    if(len(ids)>0):
        return True
    return False
    
print("----Inicio Proceso----")
if(localidadisla("12","13","0007")):
    print("Si es una localidad tipo Isla")
else:
    print("No es una localidad de tipo Isla")
print("----Termina Proceso----")

