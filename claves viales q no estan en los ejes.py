from osgeo import ogr
from processing.tools import *
import processing

def validaClaveVialfmejevial (shp,shpII):
    layer = QgsVectorLayer (shp, "EjeVial_I","ogr")
    layerII = QgsVectorLayer(shpII ,"EjeVial II","ogr")
    iter = layer.getFeatures()
    idx = layer.fields().indexFromName ("CVEVIAL")
    claves = layer.uniqueValues (idx)
    totclaves = str(len(claves))
    #print ("Total de Claves viales en Frentes de Manzana: "+totclaves)
    vialnoesta = "" ; listacvevial = []
    #for unique value in claves:
    # print ("unique value : " + unique value)
    # break
    x = 0;

    for cvevial in claves:
        request = QgsFeatureRequest().setFilterExpression(u'"CVEVIAL" = \'' +cvevial + '\'')
        it= layerII.getFeatures(request); ids = [i.id() for i in it]
        if (len (ids) == 0):
            listacvevial = listacvevial + [cvevial]
        x=x+1
    print (vialnoesta)
    if (len (listacvevial) > 0):
        print (u"Claves viales de la capa"+u""+layer.name() +u""+"que no estan en "+ layerII.name())
        print("")
        for cvevial in listacvevial:
            print (u" Clave vial " + u""+ cvevial + u" no esta en la capa " + u""+ layerII.name())
        print (" ")
    pass

print ("----------------------------")
print ("Inicia Proceso")
print ("----------------------------")
shapeI = r'D:\Curso_II\Insumos\30001fm.shp'
shapeII = r'D:\Curso_II\Insumos\30001e.shp'
validaClaveVialfmejevial (shapeI,shapeII)

print ("----------------------------")
print ("Termina Proceso")
print ("----------------------------")