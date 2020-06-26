import sys
from gridmeister import GridMeister


tile = 'tile40N-80E'

if 'tile' in sys.argv[1]:
    tile = sys.argv[1]
else:
    print("No tile specified\n")
    sys.exit(1)


gm = GridMeister(tile)

chip_list = gm.chip_list()

print(chip_list)


for chip in chip_list:
        gm.create_chip_shp(chip)

gm.build_docker_run_bash(chip_list)



