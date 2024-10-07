import random
import numpy as np
import opensimplex as simplex
import values as val
from random import sample
from values import Temperature, Humidity, Biomes, Colours
from PIL import Image
def generate_world(width: int, height: int, features: int, scale: int, seed: int):
    # check if we have a seed
    if seed == 0:
        seed = random.randint(0, 99999999)
    else:
        seed = seed

    #initialise the world
    thisWorld = np.full((width, height), fill_value=0, order="F")
    # add the temperature layer
    temp_layer(thisWorld, features, seed)
    # add the humidity
    humidity_layer(thisWorld, features, seed)
    # add the water, 20% seems to give sort of what i want
    add_water(thisWorld, seed)
    # output image of the world
    #output_world_image(thisWorld, "world.png")
    # scale up
    thisWorld = np.repeat(np.repeat(thisWorld, 8, axis=1), 8, axis=0)
    output_world_image(thisWorld, "test.png")
    # debug/check
    print('MAX: ', np.max(thisWorld))
    print('MIN: ', np.min(thisWorld))
    print('VALS: ', np.unique(thisWorld))
    print('SIZE: ', np.size(thisWorld))
    print('COLOUR: ', val.map_colours[3])
    return thisWorld

def temp_layer(world: np.array, features: int, seed: int):
    # set the seed
    simplex.seed(seed)

    # variables
    width = world.shape[0]
    height = world.shape[1]
    # generate the temperatures
    for y in range(0, height):
        for x in range(0, width):
            thisValue = simplex.noise2(x / (features / 1), y / (features / 1))
            thisValue = (thisValue + 0.7) / 1.4
            if thisValue <= 0.1:
                thisValue = Temperature.HOT
            elif thisValue > 0.1 and thisValue <= 0.3:
                thisValue = Temperature.WARM
            elif thisValue > 0.3 and thisValue <= 0.7:
                thisValue = Temperature.TEMPERATE
            elif thisValue > 0.7 and thisValue <= 0.9:
                thisValue = Temperature.COLD
            elif thisValue > 0.9:
                thisValue = Temperature.FREEZING
            world[x, y] = thisValue
    # smooth the values so that FREEZING isnt next to WARM or HOT and WARM isnt next to FREEZING or COLD
        for y in range(0, height - 1):
            for x in range(0, width - 1):
                x1 = x - 1 if x - 1 > 0 else 0
                x2 = x + 1 if x + 1 < width else width
                y1 = y - 1 if y - 1 > 0 else 0
                y2 = y + 1 if y + 1 < height else height
                if world[x, y] == Temperature.WARM:
                    if (world[x1, y] == Temperature.FREEZING or world[x2, y] == Temperature.FREEZING or world[x, y1] == Temperature.FREEZING or world[
                        x, y2] == Temperature.FREEZING) or (world[x1, y] == Temperature.COLD or world[x2, y] == Temperature.COLD or world[x, y1] == Temperature.COLD or world[x, y2] == Temperature.COLD):
                        world[x, y] = Temperature.TEMPERATE
                if world[x, y] == Temperature.FREEZING:
                    if (world[x1, y] == Temperature.WARM or world[x2, y] == Temperature.WARM or world[x, y1] == Temperature.WARM or world[
                        x, y2] == Temperature.WARM) or (world[x1, y] == Temperature.TEMPERATE or world[x2, y] == Temperature.TEMPERATE or world[x, y1] == Temperature.TEMPERATE or world[x, y2] == Temperature.TEMPERATE):
                        world[x, y] = Temperature.COLD
                    
    return

def humidity_layer(world: np.array, features: int, seed: int):
    # reverse the seed
    reverse_seed = str(seed)
    reverse_seed = reverse_seed[::-1]
    reverse_seed = int(reverse_seed)
    simplex.seed(reverse_seed)

    # variables
    width = world.shape[0]
    height = world.shape[1]

    # use a temporary world to hold the humidity vals
    humid_layer = np.full((width, height), fill_value=0, order="F")
    for y in range(0, height):
        for x in range(0, width):
            thisValue = simplex.noise2(x / (features / 1), y / (features / 1))
            thisValue = (thisValue + 0.7) / 1.4
            if thisValue <= 0.1:
                thisValue = Humidity.HUMID
            elif thisValue > 0.1 and thisValue <= 0.3:
                thisValue = Humidity.WET
            elif thisValue > 0.3 and thisValue <= 0.7:
                thisValue = Humidity.MOIST
            elif thisValue > 0.7 and thisValue <= 0.9:
                thisValue = Humidity.DRY
            elif thisValue > 0.9:
                thisValue = Humidity.ARID
            humid_layer[x, y] = thisValue
    # smooth the values so that HUMID isnt next to DRY or ARID and DRY isnt next to HUMID or WET
        for y in range(0, height - 1):
            for x in range(0, width - 1):
                x1 = x - 1 if x - 1 > 0 else 0
                x2 = x + 1 if x + 1 < width else width
                y1 = y - 1 if y - 1 > 0 else 0
                y2 = y + 1 if y + 1 < height else height
                if world[x, y] == Humidity.DRY:
                    if (world[x1, y] == Humidity.WET or world[x2, y] == Humidity.WET or world[x, y1] == Humidity.WET or world[
                        x, y2] == Humidity.WET) or (world[x1, y] == Humidity.HUMID or world[x2, y] == Humidity.HUMID or world[x, y1] == Humidity.HUMID or world[x, y2] == Humidity.HUMID):
                        world[x, y] = Humidity.MOIST
                if world[x, y] == Humidity.HUMID:
                    if (world[x1, y] == Humidity.DRY or world[x2, y] == Humidity.DRY or world[x, y1] == Humidity.DRY or world[
                        x, y2] == Humidity.DRY) or (world[x1, y] == Humidity.MOIST or world[x2, y] == Humidity.MOIST or world[x, y1] == Humidity.MOIST or world[x, y2] == Humidity.MOIST):
                        world[x, y] = Humidity.WET
    # remove the weird values to leave the biomes we want
    for y in range(0, height):
        for x in range(0, width):
            thisValue = humid_layer[x, y] + world[x, y]
            random.seed(seed)
            if thisValue == 12:
                choice = [11, 22]
                thisValue = sample(choice, 1)[0]
            elif thisValue == 13:
                thisValue = 22
            elif thisValue == 14:
                thisValue = 22
            elif thisValue == 15:
                thisValue = 33
            elif thisValue == 23:
                choice = [22, 33, 32]
                thisValue = sample(choice, 1)[0]
            elif thisValue == 24:
                thisValue = 33
            elif thisValue == 25:
                choice = [33, 44]
                thisValue = sample(choice, 1)[0]
            elif thisValue == 34:
                choice = [33, 43, 44]
                thisValue = sample(choice, 1)[0]
            elif thisValue == 35:
                thisValue = 44
            elif thisValue == 45:
                choice = [44, 54, 55]
                thisValue = sample(choice, 1)[0]
            world[x, y] = thisValue
    return

def add_water(world: np.array, seed: int):
    # set the seed
    simplex.seed(seed)
    #variables
    width = world.shape[0]
    height = world.shape[1]
    # generate the water
    for y in range(0, height):
        for x in range(0, width):
            value1 = 1 * simplex.noise2(x / 16, y / 16)
            value2 = 0.5 * simplex.noise2(x / 8, y / 8)
            value3 = 0.25 * simplex.noise2(x / 4, y / 4)
            value4 = 0.125 * simplex.noise2(x / 2, y / 2)
            value5 = 0.0625 * simplex.noise2(x / 1, y / 1)
            thisValue = (value1 + value2 + value3 + value4 + value5 + 1) / 2
            # see if we have water
            if thisValue <= 0.2:
            # we have water so find what temperature it is
                thisTemp = world[x, y] % 10
                world[x, y] = thisTemp
    return

def output_world_image(world, filename):
    #variables
    width = world.shape[0]
    height = world.shape[1]


    # colour image
    im = Image.new("RGB", (width, height))
    for y in range(0, height):
        for x in range(0, width):
            #im.putpixel((x, y), colour(int(world[x, y])))
            im.putpixel((x,y), val.map_colours[int(world[x, y])])
    im.save(filename)
    return

def colour(value):
    if value == 51:
        return Colours.HOT_ARID
    elif value == 41:
        return Colours.HOT_DRY
    elif value == 31:
        return Colours.HOT_MOIST
    elif value == 21:
        return Colours.HOT_WET
    elif value == 11:
        return Colours.HOT_HUMID
    elif value == 52:
        return Colours.WARM_ARID
    elif value == 42:
        return Colours.WARM_DRY
    elif value == 32:
        return Colours.WARM_MOIST
    elif value == 22:
        return Colours.WARM_WET
    elif value == 53:
        return Colours.TEMP_ARID
    elif value == 43:
        return Colours.TEMP_DRY
    elif value == 33:
        return Colours.TEMP_MOIST
    elif value == 54:
        return Colours.COLD_ARID
    elif value == 44:
        return Colours.COLD_DRY
    elif value == 55:
        return Colours.FREEZING_ARID
    elif value == 1:
        return Colours.HOT_WATER
    elif value == 2:
        return Colours.WARM_WATER
    elif value == 3:
        return Colours.TEMP_WATER
    elif value == 4:
        return Colours.COLD_WATER
    elif value == 5:
        return Colours.FREEZING_WATER
    else:
        print(value)
        return Colours.RED


