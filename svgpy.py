# h3avren

class SVG:
    """This is the class which is used to write svg
    files. It provides us with functions to write svg's"""
    def __init__(self, width = 300, height = 150):
        self.width = width
        self.height = height
        self.svg_string = f'<svg width="{self.width}" height="{self.height}'\
                           '" xmlns="http://www.w3.org/2000/svg">\n'
    
    # function to draw a rectangle
    def rect(self, x = 0, y = 0, width = 200, height = 100, rx = 0, ry = 0):
        self.svg_string += f'<rect x="{x}" y="{y}" width="{width}"'\
                           f' height="{height}" rx="{rx}" ry="{ry}" />\n'
    
    # function to draw a circle
    def circle(self, cx = 50, cy = 50, r = 20):
        """cx: int
           cy: int
           r: int
           returns : None"""
        self.svg_string += f'<circle cx="{cx}" cy="{cy}" r="{r}" />\n'

    # function to draw an ellipse
    def ellipse(self, cx = 50, cy = 50, rx = 30, ry = 10):
        """This function will be used to draw an ellipse
            cx: int
            cy: int
            rx: int
            ry: int
            returns: None
        """
        self.svg_string += f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" />'

    # function to draw a line
    def line(self, x1 = 0, y1 = 0, x2 = None, y2 = None):
        """
        x1: int
        y1: int
        x2: int
        y2: int
        returns: None
        """
        if(x2 == None):
            x2 = self.width
        if(y2 == None):
            y2 = self.height
        
        self.svg_string += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" />\n'

    # function to draw a polyling
    def polyline(self, points = [(0,0),(10,10),(20,20)]):
        """
        points: list of tuples of points (x,y)
        returns: None
        """
        points_string = ""
        for i in points:
            points_string += f" {i[0]}, {i[1]}"
        points_string = points_string.strip()
        self.svg_string += f'<polyline points="{points_string}"/>\n'

    # function to draw a polygon
    def polygon(self):
        pass

    # functon to draw a path
    def path(self):
        pass

    # function to finally write the svg file
    def write(self,save_as='test.svg'):
        self.svg_string += '</svg>'
        with open(save_as,'w') as file:
            file.write(self.svg_string)
    

obj = SVG(400,500)
obj.rect(10,30,200)
obj.polyline([(10,20),(20,30),(30,30),(40,50)])
obj.write()

