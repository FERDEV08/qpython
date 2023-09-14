from osgeo import ogr
from osgeo import osr
from qgis.core import *

def validaTraslape  (capa1,capa2):
        bandpoligono = False 
        layerpol=QgsVectorLayer(capa1,"capa1","ogr")
        iter = layerpol.getFeatures()
        for feature in iter:
              geom = feature.geometry()
              if (geom.type() == QgsWkbTypes.PolygonGeometry):
                  bandpoligono = True
                  break
        if (bandpoligono):
          conshpgeo = 0
          driver = ogr.GetDriverByName('Esri Shapefile')
          ds = driver.CreateDataSource(r"D:/curso_qpy/shp/traslape.shp")
          proj = osr.SpatialReference()
          proj.SetWellKnownGeogCS(str(layerpol.crs().authid()))
          print ("Referecia Espacial : "+str(layerpol.crs().authid()))
          layshp = ds.CreateLayer("",proj, ogr.wkbPolygon)
          layshp.CreateField(ogr.FieldDefn('id', ogr.OFTInteger))
          defn = layshp.GetLayerDefn()
          print ("Capa  : "+capa1)
          file = ogr.Open(capa1);   #Abrir Shape Libreria de osgeo
          shape = file.GetLayer(0)  #Obtener la Informacion del shape          
          lonshape = shape.GetFeatureCount(); #Obtener el total de registros del shape 
          con = 0; terror = 0;listaempalme =  []   
          while (con < lonshape):
                feature = shape.GetFeature(con);#Obtener los datos del registro
                valorfid = feature.GetFID(); #Obtener  el OID
                geom = feature.geometry();#Obtener  la Geoemetria
                f = ogr.Open(capa2);shp = f.GetLayer(0);lonshp = shp.GetFeatureCount()
                c = 0;  geointercepta = False; conintercepta  = 0; error = False; bandintercepta = False 
                while (c < lonshp):
                          feat= shp.GetFeature(c);  valorfid2 = feat.GetFID()
                          geo = feat.geometry(); 
                          intersection = geo.Intersection(geom)
                          if (geom.Intersects(geo) and (valorfid != valorfid2)): #Condicional para ver si hay intercepcion de Geometria
                             geointer = geom.Intersection(geo)#Obeneter  la geoemtria donde esta la Intercepcion
                             if (geointer.GetArea() > 0):
                                bandintercepta = True
                                vfid = feat.GetFID()
                                #if ((valorfid not in listaempalme) or (vfid not in listaempalme)):                               
                                if (valorfid not in listaempalme):                               
                                        print ("Error en la capa "+  capa1  + " con  registro " + str (valorfid)  + " CVEGEO " + feature ['CVEGEO'] + " Se traslapa con geometria con registro "+ str(vfid)  + " CVEGEO " + feat ['CVEGEO'])
                                        print (" ")                              
                                        listaempalme = listaempalme +  [valorfid]
                                        listaempalme = listaempalme +  [vfid]
                                        terror = terror + 1
                                        feat = ogr.Feature(defn)
                                        feat.SetField('id', conshpgeo)
                                        feat.SetGeometry(geointer)
                                        layshp.CreateFeature(feat) 
                                        conshpgeo  = conshpgeo + 1
                          c = c  + 1
                con = con + 1
          ds = layers = None      
          print ("La capa : "+ capa1 + " Tiene  " +  str (terror) + " Errores de Traslape entre geometrías")
          print (" ")     
          capaRes = QgsVectorLayer(r"D:/curso_qpy/traslape.shp","traslape","ogr")
          QgsProject.instance().addMapLayer(capaRes)
pass

print ('Validacion de Traslape')
capa1 = 'D:/curso_qpy/01001m/01001m.shp'
validaTraslape  (capa1,capa1)
