import os

def get_svg(svgName):
    rel_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(rel_path, "templatetags" +"/"+ "icons"+ "/" + svgName + ".svg")
    with open(path, 'r') as file:
        data = file.read()
        return data

