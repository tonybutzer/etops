from gridmeister import GridMeister

gm = GridMeister('tile40N-80E')

chip_list = gm.chip_list()

print(chip_list)


for chip in chip_list:
        gm.create_chip_shp(chip)

