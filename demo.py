# Demo program for waz shapefile
# The following file was used to aid making the shape file, thanks for g7vjr
# and IV3TMM
# https://g7vjr.org/2019/08/google-earth-kmz-files-for-cq-zones-and-itu-zones/

import cartopy.crs as ccrs
import matplotlib.pyplot as plt

#https://scitools.org.uk/cartopy/docs/latest/gallery/nightshade.html#sphx-glr-gallery-nightshade-py

import cartopy.io.shapereader as shpreader
from cartopy.feature.nightshade import Nightshade
import datetime

date = datetime.datetime.utcnow()

reader = shpreader.Reader("waz.shp")
zones = reader.records()

for zone in zones:
  print(zone.attributes['Name']) 
  ax = plt.axes(projection=ccrs.PlateCarree())
  ax.stock_img()
  ax.coastlines()                  
  
  ax.add_geometries([zone.geometry], crs=ccrs.PlateCarree(), facecolor='g', alpha=0.7)
  ax.add_feature(Nightshade(date, alpha=0.2))
  plt.show()                     
