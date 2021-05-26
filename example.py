import numpy as np
from pyhdf import SD
from pyhdf import VS
from pyhdf import HDF
import pprint as pp
import sys

#import cartopy.crs as ccrs
#import cartopy.feature as cfeature
#import matplotlib
import matplotlib.pyplot as plt
#import matplotlib.ticker as mticker
#from matplotlib.dates import DateFormatter
#from matplotlib import cm
#import matplotlib.dates as mdates
#import numpy as np

import imp
import vfm_type
import vfm_expand
import vfm_plot
imp.reload(vfm_type)
imp.reload(vfm_expand)
imp.reload(vfm_plot)

plt.ion()
plt.interactive(True)

# point to the file to be read
filen = 'samples/CAL_LID_L2_VFM-ValStage1-V3-30.2013-05-06T17-20-01ZD_Subset.hdf'
print('Reading from file: ' + filen)

# read the VFM
h4sd = SD.SD(filen)
print(f'number of datasets, number of attributes: {h4sd.info()}')
for idx,sds in enumerate(h4sd.datasets()):
    print(idx,sds)

sds = h4sd.select('Feature_Classification_Flags')
print(f'Selected: {sds.info()}')

data = sds.get()
print(f'Size of dataset: {np.shape(data)}')
[cnt, cline] = np.shape(data)

# convert VFM rows into blocks
vfmblock = vfm_expand.vfm_expand(data)
print(f'Size of VFM block: {np.shape(vfmblock)}')
[nz, nt] = np.shape(vfmblock)

# read latitude
# Not all data files have the ssLatitude variable
# This is the latitude at the level 1 data (i.e. 333m)
# If we don't have that, we have to interpolate
if 'ssLatitude' in h4sd.datasets():
    lat = np.float64(h4sd.select('ssLatitude').get())
    lon = np.float64(h4sd.select('ssLongitude').get())
else:
    # Not sure if this is correct. Need to check "where" the Latitute of a L2
    # product is placed relative to the L1 positions.
    tmp = np.float64(h4sd.select('Latitude').get()[:,0])
    lat = np.interp(np.arange(nt)-0.5, 15*(np.arange(cnt)-0.5), tmp)
    tmp = np.float64(h4sd.select('Longitude').get()[:,0])
    lon = np.interp(np.arange(nt)-0.5, 15*(np.arange(cnt)-0.5), tmp)

# read altitude
h4 = HDF.HDF(filen)
vs = h4.vstart()
vs_meta = vs.attach('metadata')
field_names = vs_meta.inquire()[2]
print('file metadata: ')
pp.pprint(vs_meta.fieldinfo())

if not vs_meta.fexist('Lidar_Data_Altitudes'):
    print('ERROR: Lidar_Data_Altitudes not found')
    sys.exit()

for i,tag in enumerate(field_names):
    if tag == 'Lidar_Data_Altitudes':
        alt = np.array(vs_meta[:][0][i])
    
alt = alt[ (alt > -0.5) & (alt < 30) ]

vfmtypes = ['type', 'typeqa', 'phase', 'phaseqa', 'aerosol', 'cloud',
            'psc', 'subtype', 'subtypeqa', 'averaging']

for tag in vfmtypes:
    # extract the feature flag
    vfmflag = vfm_type.vfm_type(vfmblock, tag)

    # plot the flag
    vfm_plot.vfm_plot(vfmflag, [lat, lon], alt)

#vs_meta.detach()
#vs.end()
#h4.close()
#sds.endaccess()
#h4sd.end()

# other features
#[vfmdata, vfmtype] = vfm_plot(data,[1 223],'typeqa')
#[vfmdata, vfmtype] = vfm_plot(data,[1 223],'phase')
#[vfmdata, vfmtype] = vfm_plot(data,[1 223],'phaseqa')
#[vfmdata, vfmtype] = vfm_plot(data,[1 223],'aerosol')
#[vfmdata, vfmtype] = vfm_plot(data,[1 223],'cloud')
#[vfmdata, vfmtype] = vfm_plot(data,[1 223],'psc')
#[vfmdata, vfmtype] = vfm_plot(data,[1 223],'subtype')
#[vfmdata, vfmtype] = vfm_plot(data,[1 223],'subtypeqa')
#[vfmdata, vfmtype] = vfm_plot(data,[1 223],'averaging')

#function [alt] = Ind2Alt(ind)
#sz = length(ind)
#for i=1:sz,
#  if ind(i) < 56,
#    alt(i) = 30.1 - (i)*180/1000
#  elseif ind(i) < 256,
#    alt(i) = 20.2 - (i-55)*60/1000
#  else
#    alt(i) = 8.2 - (i-255)*30/1000
#  end
#end

