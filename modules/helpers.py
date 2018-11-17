from bge import logic

# just get stuff from the globalDict
def get_prop(key):
    return logic.globalDict.get(key)

def set_prop(key, value):
    logic.globalDict[key][value]


def clamp(value, min, max):
    """ Clamps the given value
    :param: value
    :param: min
    :param: max
    """
    if value > max:
        return max
    elif value < min:
        return min
    else:
        return value

def time_string(timefloat):
    """ Interprets a float as seconds and returns a formatted string """
    return str( int(timefloat/60) ) + ":" + str(int(timefloat) % 60) + ":" + str(timefloat - int(timefloat))[2:][:3]

def fatal_error(msg):
    print("Something went wrong:", msg)