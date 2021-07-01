import os
import sys
#from etopsLib.degree_gridmeister import GridMeister
from etopsLib.numeric_gridmeister import GridMeister



tile_cust=os.getcwd()
tile_cust=tile_cust.split('/')[-1]
tile = 'run_'+tile_cust

optimize=True
if len(sys.argv) > 2:
    if 'no' in sys.argv[2]:
        optimize = False;


gm = GridMeister(tile)
darin_extent = (169.752, 9.290, 170.297, 9.609)
smallest_extent_darin_greg = (169.752, 9.290, 170.297, 9.609)

gm.set_extent(smallest_extent_darin_greg)

x_raster_res=0.00027314408
y_raster_res=0.00027314408
gm.set_xy_res(x_raster_res, y_raster_res)


#chip_list = gm.chip_list()
#print(chip_list)

lst = gm.chip_list()
#print('resulting chip list \n', lst)

chip_output = './AOI/'
#gm.create_chip_shp(ul_lat=None, ul_lon=None, out_location=chip_output, unit_chip=True)

for l in lst:
    gm.create_chip_shp(l[0], l[-1], out_location=chip_output)

filenames = gm.get_json_filenames()

bash_chip_list = []
#print('==='* 30)
for long_ugly_name in filenames:
    #print(long_ugly_name)
    bash_name = long_ugly_name.replace(chip_output,'')
    bash_name = bash_name.replace('.json','')
    #print(bash_name)
    bash_chip_list.append(bash_name)


#for chip in chip_list:
        #gm.create_chip_shp(chip)

gm.build_docker_run_bash(bash_chip_list, optimize)



