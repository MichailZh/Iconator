def average(x, y):
    return (x + y) / 2


def power(x, y):
    return x ** y


def get_svg(svgName):
    with open("Iconator/" + "icons" + "/" + svgName, 'r') as file:
        data = file.read()
        # print(data)
        return data

