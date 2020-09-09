import sys
from gridmeister import GridMeister


tile = 'drb_tile_40yr'

optimize=True
if len(sys.argv) > 2:
    if 'no' in sys.argv[2]:
        optimize = False;


gm = GridMeister(tile)

chip_list = gm.chip_list()

print(chip_list)


for chip in chip_list:
        gm.create_chip_shp(chip)

gm.build_docker_run_bash(chip_list, optimize)



