

def _parse_tile_name(tile_name):
    print (tile_name)
    tn = tile_name.split('tile')[-1]
    print(tn)
    ul_lat = tn.split('N')[0]
    tn = tn.split('N')[-1]
    print(tn)
    print(ul_lat)
    ul_lon = tn.split('E')[0]
    print(ul_lon)
    return ul_lat, ul_lon


class GridMeister:
    """
    This class partitions a 10 degree tile into 2 degree chips
    """

    def __init__(self, tile_name):

        self.tile_increment = 10
        self.chip_increment = 2


        print (tile_name)
        
        ul_lat,ul_lon = _parse_tile_name(tile_name)

        print(ul_lat,ul_lon)

        self.tile_ul_lat = int(ul_lat)
        self.tile_ul_lon = int(ul_lon)


    def chip_list(self):
        CHIP_LIST = []
        print(self.tile_ul_lat)

        starting_lat = self.tile_ul_lat
        ending_lat = starting_lat - self.tile_increment

        print(starting_lat, ending_lat)

        starting_lon = self.tile_ul_lon
        ending_lon = starting_lon + self.tile_increment
        print(starting_lon, ending_lon)

        lat = starting_lat
        while lat > ending_lat:
            print(lat)

            lon = starting_lon
            while lon < ending_lon:
                print(lon)
                chip_name = 'chip' + str(lat) + 'N' + str(lon) +'E'
                CHIP_LIST.append(chip_name)
                lon = lon + self.chip_increment

            lat = lat - self.chip_increment

        return CHIP_LIST

