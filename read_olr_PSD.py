# Ahmed Shaaban
# Oct,2,2017
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import sys  
from scipy import interpolate
import os
#%% reading the data.
diri="/Users/ahmedlasheen/codes4packages/lecture_python/new_lectures/"
tmp_file = xr.open_dataset(diri+"olr.day.mean.nc")
olrP  = tmp_file['olr']
latP  = tmp_file['lat']
lon   = tmp_file['lon']
timeP = tmp_file['time']

lat   = latP[::-1]
olr   = olrP[:,::-1,:]

dti    = timeP.to_index()
periods= dti.to_period(freq='D')
print('------------------------------------------------------------')
print(' First time is '+str(periods[0])+' Last time is '+str(periods[-1]))
np.where(np.isnan(olr))
#%%
periods
#%%
# the OLR file has the same grid (spatial) as the ERAI that I downloaded so 
# need for interpolation. I just will cut the file to match the one EARI files 
# that I am using.
t1  =np.where(periods == '1979-01-01')[0][0]
t2  =np.where(periods == '2018-12-31')[0][0]
lat1=np.where(latP ==  20)[0][0]
lat2=np.where(latP == -20)[0][0]

olr4tilt =olrP[t1:t2+1,lat1:lat2+1,:]
lat4tilt =latP[lat1:lat2+1]
dti4tilt =dti[t1:t2+1]

input_base    =lines[0]+"/data_center/Reanalysis/kelvin_tilt/"
diri_input    =input_base+"/"+'olr_2.5'+"/vert/"
filename      = 'all_daily.nc'

varF = xr.Dataset(
data_vars={
		'olr':(('time','lat','lon'),olr4tilt),
		},
coords={
		'time':(('time'),dti4tilt),
		'lat':(('lat'),lat4tilt),
		'lon':(('lon'),lon),
		}
)

if os.path.exists(diri_input+filename):
	os.remove(diri_input+filename)
	print('removing the file ')
else:
	print('the file doesnot exist')
	
varF.to_netcdf(path=diri_input+filename)
#%%
# Interpolating the OLR to the ERA-I so that I 
# can overlay the OLR over the ERA-I fields.
###############################################################
diri_outFiles           =lines[2]+"/data_center/outFiles/kelvin_tilt/uwind_2.5_50_50/daily_data/"
timeMe=np.load(diri_outFiles+'metadata.npz')
print(timeMe.files)
lat_eraI                 =timeMe['lat']
lon_eraI                 =timeMe['lon']
time_var_all_eraI        =timeMe['time_var_ll']
dtime_vard_all_eraI      =timeMe['dtime_vard_all']
dates_pd_var_d_all_eraI  =timeMe['dates_pd_var_d_all']

lon_re=np.concatenate((lon[72:]-360,lon[0:72]))
lat_50N=int(np.where(lat == 50)[0])
lat_50S=int(np.where(lat == -50)[0])
lat_50N_50S=lat[lat_50N:lat_50S+1]
olr_lon_re=np.concatenate((olr_data[:,:,72:],olr_data[:,:,0:72]),axis=2)
olr_all_50N_50S=olr_lon_re[:,lat_50N:lat_50S+1,:]

# interpolation from 2.5X2.5 to 2.5X2.5 to  be in the same grid of the ERA-I.
olr_all_2p5=np.zeros((len(time),len(lat_eraI),len(lon_eraI)))
for i in np.arange(len(time)):
    tmp=np.reshape(olr_all_50N_50S[i,::-1,:].T,(len(lat_50N_50S)*len(lon)))
    plt_f = interpolate.interp2d(lon_re,lat_50N_50S[::-1],tmp,'linear')
    olr_all_2p5[i,:,:]=plt_f(lon_eraI,lat_eraI)
    print('working on the interpolation '+str(i))

p4m.quick_plot1(lat_50N_50S,lon_re,olr_all_50N_50S[0,:,:],"before interpolation 2.5X2.5")
p4m.quick_plot1(lat_eraI,lon_eraI,olr_all_2p5[0,:,:],"after interpolation 2.5X2.5")
plt.figure();plt.contourf(olr_all_50N_50S[:1000,20,:]);plt.colorbar();plt.show(block=False)
plt.figure();plt.contourf(olr_all_2p5[:1000,20,:]);plt.colorbar();plt.show(block=False)
plt.figure();plt.contourf(olr_all_50N_50S[:1000,20,:]-olr_all_2p5[:1000,20,:]);plt.colorbar() ## almost zeros, this is perfect.
# calling the function and saving the file
print('saving the file .....')
name_OLR1 = lines[2]+"/data_center/outFiles/kelvin_tilt/olr_2.5_50_50/daily_data/OLR_PSD_1974_2013.npz"
np.savez(name_OLR1,olr_all_2p5=olr_all_2p5,lat=lat_50N_50S,lon=lon_re,time=time,dtime=dtime,dates_pd=dates_pd,periods=periods)
################################################################
### save file that begin from 1979-1-1 to 1016-12-31
year_1979=m.find((periods.year == 1979) &
                 (periods.month==1) &
                 (periods.day==1))[0];

year_2013=m.find((periods.year == 2013) &
                 (periods.month==12) &
                 (periods.day==31))[0];
# those are from Jan 1979 - Dec 2013
dates_pd_79_13 = dates_pd[year_1979:year_2013+1]
periods_79_13=dates_pd_79_13.to_period(freq='D')
olr_all_2p5_79_13=olr_all_2p5[year_1979:year_2013+1,:,:]

sys.exit()
print('saving the file .....')
name_OLR1 = lines[2]+"/data_center/outFiles/kelvin_tilt/olr_2.5_50_50/daily_data/OLR_PSD_1979_2013.npz"
np.savez(name_OLR1,olr_all_2p5_79_13=olr_all_2p5_79_13,\
                   lat=lat_50N_50S,\
                   lon=lon_re,\
                   dates_pd_79_13=dates_pd_79_13,\
                   periods_79_13=periods_79_13)

# plotting the data.
mylat=int(np.where(lat_50N_50S == 0)[0])       
mylon=int(np.where(lon_re == 145)[0])        
plt.figure();plt.contourf(lon_re,dates_pd_79_13,olr_all_2p5_79_13[:,mylat,:]);plt.colorbar();plt.show(block=False)


lat1=int(np.where(lat_50N_50S == -10)[0])
lat2=int(np.where(lat_50N_50S == 10)[0])
lon1=int(np.where(lon_re == -120)[0])
lon2=int(np.where(lon_re == -170)[0])
oni_olr=np.nanmean(np.nanmean(olr_all_2p5_79_13[:,lat2:lat1+1,lon2:lon1+1],2),1)
plt.figure();plt.plot(dates_pd_79_13,oni_olr);plt.show(block=False)

