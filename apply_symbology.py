import arcpy, os, sys

#layers = ["hex_seq_276","hex_seq_277","hex_seq_278", "hex_seq_279","hex_seq_280","hex_seq_281",
            #"hex_seq_282","hex_seq_283","hex_seq_284","hex_seq_285","hex_seq_286",
            #"hex_seq_287","hex_seq_288"]

#symbology_layer = r"C:\Users\talis\Hexagons\hexagons_1_to_175\hexagons_001_to_025\soil_delineation_symbology.lyrx"
symbology_layer = r"C:\Users\talis\Hexagons\HexagonSymbology\HexagonSymbology.lyrx"


mm = arcpy.GetParameterAsText(0)
ll = arcpy.GetParameter(1)

arcpy.AddMessage(type(ll).__name__)


aprx = arcpy.mp.ArcGISProject('current')
m = aprx.listMaps(mm)[0]


lyrx = arcpy.mp.LayerFile(symbology_layer)
symLyr = lyrx.listLayers()[0]
sym = symLyr.symbology

for l in ll:
    lyr = m.listLayers(l)[0]
    lyr.symbology = sym
    lyr.transparency = 50

