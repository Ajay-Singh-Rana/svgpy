# h3avren

def rgb(red,green,blue):
    return f"rgb({red},{green},{blue})"

# class for handling SVG stuff
class SVG:
    """
    This class is used to write svg files.
    It provides us with functions to write svg's
    
    Attributes
    ----------
    width : int 
        The width of the SVG image
    height : int
        The height of the SVG image

    """

    def __init__(self, width = 300, height = 150):
        self.width = width
        self.height = height
        self.svg_string = f'<svg width="{self.width}" height="{self.height}'\
                           '" xmlns="http://www.w3.org/2000/svg">\n'
    
    # function to draw a point
    def point(self, point, fill = rgb(0,0,0)):
        """Draws a point in the SVG image
        
        Parameters
        ----------
        point : (int,int)
            co-ordinates of the point
        fill : rgb(red,green,blue)
            fill color of the point
        """

        self.svg_string += f'<rect x="{point[0]}" y="{point[1]}" width = "1"'\
                           f' height="1" stroke="{fill}" />\n'
  
    # function to draw a rectangle
    def rect(self, start, size, rx = 0, ry = 0, stroke = rgb(0, 0, 0), 
             fill = "transparent", stroke_width = 5):
        """Draws a rectangle in the SVG image

        Parameters
        ----------
        start : (int, int)
            The x,y co-ordinates of the start/initial point
        size : (int, int)
            The width, height of the rectangle
            could also be considered as x2-x1,y2-y1
            i.e. difference of start and end points of rectangle
        rx : int
            The x radius of the corners of the rectangle
        ry : int
            The y radius of the corners of the rectangle
        stroke : rgb(red,green,blue)
            Sets the border color for the rectangle
        fill : rgb(red,green,blue)
            Sets the color to be filled inside the rectangle 
        stroke_width : int
            The width of the stroke i.e. border
        """

        self.svg_string += f'<rect x="{start[0]}" y="{start[1]}"'\
                           f' width="{size[0]}" height = "{size[1]}"'\
                           f' rx="{rx}" ry="{ry}" stroke="{stroke}"' \
                           f' fill="{fill}" stroke-width="{stroke_width}" />\n'
    
    # function to draw a circle
    def circle(self, center, radius, stroke = rgb(0,0,0), 
               fill = "transparent", stroke_width = 5):
        """Draws a circle in the SVG image

        Parameters
        ----------
        center : (int, int)
            The x,y co-ordinates for the center of the circle
        radius : int
            The radius of the circle
        stroke : rgb(red,green,blue)
            Sets the border color for the circle
        fill : rgb(red,green,blue)
            Sets the color to be filled inside the circle
        stroke_width : int
            The width of the stroke i.e. border
        """

        self.svg_string += f'<circle cx="{center[0]}" cy="{center[1]}"'\
                           f' r="{radius}" stroke="{stroke}"'\
                           f' fill="{fill}" stroke-width="{stroke_width}" />\n'

    # function to draw an ellipse
    def ellipse(self, center, radii, stroke = rgb(0,0,0),
                fill = "transparent", stroke_width = 5):
        """This function will be used to draw an ellipse
            center : (int,int)
                The x,y co-ordinates for the center of the ellipse
            radii : (int,int)
                The radiuses of the ellipse along x-axis,y-axis
            stroke : rgb(red,green,blue)
                Sets the border color for the ellipse
            fill : rgb(red,green,blue)
                Sets the color to be filled inside the ellipse
            stroke_width : int
                The width of the stroke i.e. border
        """

        self.svg_string += f'<ellipse cx="{center[0]}" cy="c{enter[1]}"'\
                           f' rx="{radii[0]}" ry="{radii[1]}"'\
                           f' stroke="{stroke}"'\
                           f' fill="{fill}" stroke-width="{stroke_width}" /> \n'

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
obj.point((50,50))
# obj.rect(10,30,200, fill="red", stroke_width = 10,stroke = rgb(28,29,150))
# obj.polyline([(10,20),(20,30),(30,30),(40,50)])
# obj.circle(cx=4,cy=5,fill=rgb(123,224,200),r=15,stroke_width=10)
obj.write()

