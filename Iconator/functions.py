def get_svg(svgName):
    with open("Iconator/" + "icons" + "/" + svgName + ".svg", 'r') as file:
        data = file.read()
        return data

