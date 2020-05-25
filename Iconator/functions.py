def average(x, y):
    return (x + y) / 2


def power(x, y):
    return x ** y


def get_svg(svgName):
    with open("Iconator/" + "icons" + "/" + svgName + ".svg", 'r') as file:
        data = file.read()
        return data

