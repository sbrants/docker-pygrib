import pygrib

#remember to set environment variable GRIB_DEFINITION_PATH to wherever the
#grib api definitions folder is, for example /Users/tvik/Development/grib_api/share/grib_api/definitions/

grbs = pygrib.open('nam.t00z.awphys00.grb2.tm00')

#grbs.seek(2)
grb = grbs.select(name='Temperature', typeOfLevel='surface')[0]
print grb

data=grb.values
lat,lon = grb.latlons()

print grb.values