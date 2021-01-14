import os
import sys
import argparse
#from etopsLib.degree_gridmeister import GridMeister
from etopsLib.numeric_gridmeister import GridMeister



def do_work(geojson_file):
    tile_cust=os.getcwd()
    tile_cust=tile_cust.split('/')[-1]
    tile = 'run_'+tile_cust

    optimize=True
    if len(sys.argv) > 2:
        if 'no' in sys.argv[2]:
            optimize = False;


    gm = GridMeister(tile)
    my_geo = gpd.read_file(geojson_file)
    #smallest_extent_darin_greg = (-76.788, 38.362, -73.723, 42.809)

    smallest_extent = my_geo.geometry[0].bounds
    gm.set_extent(smallest_extent)

    x_raster_res=0.002310233679679207525
    y_raster_res=0.002310233679679207525
    gm.set_xy_res(x_raster_res, y_raster_res)

    lst = gm.chip_list()

    chip_output = './AOI/'

    for l in lst:
        gm.create_chip_shp(l[0], l[-1], out_location=chip_output)

    filenames = gm.get_json_filenames()

    bash_chip_list = []
    for long_ugly_name in filenames:
        bash_name = long_ugly_name.replace(chip_output,'')
        bash_name = bash_name.replace('.json','')
        bash_chip_list.append(bash_name)

    gm.build_docker_run_bash(bash_chip_list, optimize)

def get_parser():
    parser = argparse.ArgumentParser(description='Run the eto code')
    parser.add_argument('-g', '--geojson_file', help='specify geojson files ', default='a.geojson', type=str)
    return parser


def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())

    if args['geojson_file']:
        print("geojson_file", args['geojson_file'])
        geojson_file = args['geojson_file']
        do_work(geojson_file)

if __name__ == '__main__':
    command_line_runner()
