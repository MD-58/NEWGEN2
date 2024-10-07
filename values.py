map_colours = {
    51 : (255, 255, 128),
    41 : (240, 240, 128),
    31 : (96, 240, 128),
    21 : (64, 240, 144),
    11 : (32, 255, 160),
    52 : (224, 224, 128),
    42 : (192, 224, 128),
    32 : (96, 224, 128),
    22 : (32, 224, 192),
    53 : (160, 192, 128),
    43 : (128, 224, 128),
    33 : (96, 192, 128),
    54 : (192, 192, 192),
    44 : (128, 128, 128),
    55 : (255, 255, 255), 
    1 : (15, 94, 156),
    2 : (35, 137, 218),
    3 : (28, 163, 236),
    4 : (90, 188, 216),
    5 : (116, 204, 244)
}


class Temperature:
    FREEZING = 5
    COLD = 4
    TEMPERATE = 3
    WARM = 2
    HOT = 1

class Humidity:
    HUMID = 10
    WET = 20
    MOIST = 30
    DRY = 40
    ARID = 50

class Colours:
    HOT_ARID = (255, 255, 128)               # 51    desert
    HOT_DRY = (240, 240, 128)               # 41    desert 2
    HOT_MOIST = (96, 240, 128)              # 31    tropical seasonal forest
    HOT_WET = (64, 240, 144)                # 21    tropical rain forest 2
    HOT_HUMID = (32, 255, 160)               # 11    tropical rain forest
    WARM_ARID = (224, 224, 128)              # 52    savanna
    WARM_DRY = (192, 224, 128)              # 42    savanna 2
    WARM_MOIST = (96, 224, 128)              # 32    temperate deciduous forest
    WARM_WET = (32, 224, 192)             # 22    temperate rain forest
    TEMP_ARID = (160, 192, 128)              # 53    desert 3
    TEMP_DRY = (128, 224, 128)              # 43    temperate grassland
    TEMP_MOIST = (96, 192, 128)             # 33    temperate deciduous forest 2
    COLD_ARID = (192, 192, 192)             # 54    polar desert
    COLD_DRY = (128, 128, 128)               # 44    taiga
    FREEZING_ARID = (255, 255, 255)          # 55    tundra
    HOT_WATER  = (15, 94, 156)             # 1
    WARM_WATER = (35, 137, 218)            # 2
    TEMP_WATER = (28, 163, 236)             # 3
    COLD_WATER = (90, 188, 216)              # 4
    FREEZING_WATER = (116, 204, 244)         # 5
    RED = (255, 0, 0)

class Biomes:
    HOT_ARID = 51               # 51    desert
    HOT_DRY = 41               # 41    desert 2
    HOT_MOIST = 31              # 31    tropical seasonal forest
    HOT_WET = 21                # 21    tropical rain forest 2
    HOT_HUMID = 11               # 11    tropical rain forest
    WARM_ARID = 52              # 52    savanna
    WARM_DRY = 42              # 42    savanna 2
    WARM_MOIST = 32              # 32    temperate deciduous forest
    WARM_WET = 22             # 22    temperate rain forest
    TEMP_ARID = 52              # 53    desert 3
    TEMP_DRY = 43              # 43    temperate grassland
    TEMP_MOIST = 33             # 33    temperate deciduous forest 2
    COLD_ARID = 54             # 54    polar desert
    COLD_DRY = 44               # 44    taiga
    FREEZING_ARID = 55          # 55    tundra
    HOT_WATER  = 1             # 1
    WARM_WATER = 2            # 2
    TEMP_WATER = 3             # 3
    COLD_WATER = 4             # 4
    FREEZING_WATER = 5
