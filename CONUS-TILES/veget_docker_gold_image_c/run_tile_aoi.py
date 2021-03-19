import os
import sys

import geopandas as gpd

from gridmeister import GridMeisterTile


def return_geojson_extent(geojson_file):
    my_geo = gpd.read_file(geojson_file)
    smallest_extent = my_geo.geometry[0].bounds
    return(smallest_extent)
    pass

def get_tile_file_name():
    tile_name = input("Please enter tile name:  ")
    print(tile_name)
    return tile_name



tile_name = get_tile_file_name()
geojson_file = f'/opt/etops/CONUS-TILES/tile_aoi/{tile_name}.geojson'

print("GEO", geojson_file)

smallest_extent = return_geojson_extent(geojson_file)

print(smallest_extent)


tile_cust=os.getcwd()
tile_cust=tile_cust.split('/')[-1]
tile = 'run_'+tile_cust + '_' + tile_name

optimize=True
if len(sys.argv) > 2:
    if 'no' in sys.argv[2]:
        optimize = False;


divisor=5
gm = GridMeisterTile(tile, smallest_extent, divisor)


lst = gm.chip_list()

#chip_output = './AOI/'

for l in lst:
    gm.create_chip_shp(l)


bash_chip_list=lst
gm.build_docker_run_bash(bash_chip_list, optimize)

print('more code here')


