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
                           f' height="1" stroke-width="1" stroke="{fill}" />\n'
  
    # function to draw a rectangle
    def rect(self, start, size, rx = 0, ry = 0, stroke = rgb(0, 0, 0), 
             fill = "transparent", stroke_width = 1):
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
            The width of the stroke i.e. border or pen-size
        """

        self.svg_string += f'<rect x="{start[0]}" y="{start[1]}"'\
                           f' width="{size[0]}" height = "{size[1]}"'\
                           f' rx="{rx}" ry="{ry}" stroke="{stroke}"' \
                           f' fill="{fill}" stroke-width="{stroke_width}" />\n'
    
    # function to draw a circle
    def circle(self, center, radius, stroke = rgb(0,0,0), 
               fill = "transparent", stroke_width = 1):
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
            The width of the stroke i.e. border or pen-size
        """

        self.svg_string += f'<circle cx="{center[0]}" cy="{center[1]}"'\
                           f' r="{radius}" stroke="{stroke}"'\
                           f' fill="{fill}" stroke-width="{stroke_width}" />\n'

    # function to draw an ellipse
    def ellipse(self, center, radii, stroke = rgb(0,0,0),
                fill = "transparent", stroke_width = 1):
        """Draws an ellipse in the SVG image

        Parameters
        ----------
        center : (int,int)
            The x,y co-ordinates for the center of the ellipse
        radii : (int,int)
            The radiuses of the ellipse along x-axis,y-axis
        stroke : rgb(red,green,blue)
            Sets the border color for the ellipse
        fill : rgb(red,green,blue)
            Sets the color to be filled inside the ellipse
        stroke_width : int
            The width of the stroke i.e. border or pen-size
        """

        self.svg_string += f'<ellipse cx="{center[0]}" cy="{center[1]}"'\
                           f' rx="{radii[0]}" ry="{radii[1]}"'\
                           f' stroke="{stroke}"'\
                           f' fill="{fill}" stroke-width="{stroke_width}" /> \n'

    # function to draw a line
    def line(self, start, end, stroke = rgb(0,0,0), stroke_width = 1):
        """Draws a line in the SVG image

        Parameters
        ----------
        start : (int,int)
            The co-ordinates x,y for the initial point
        end : (int,int)
            The co-ordinates x,y for the end point
        stroke : rgb(red,green,blue)
            Sets the line color
        stroke_width : int
            The width of the line or pen-size
        """
        
        self.svg_string += f'<line x1="{start[0]}" y1="{start[1]}"'\
                           f' x2="{end[0]}" y2="{end[1]}" stroke="{stroke}"'\
                           f' stroke-width="{stroke_width}" />\n'

    # function to draw a polyling
    def polyline(self, points, stroke = rgb(0,0,0), fill = 'transparent',
                 stroke_width = 1):
        """Draws a line connecting several points/line segments

        Parameters
        ----------
        points : [(int,int),(int,int),(int,int),(int,int),...]
            List of tuples of co-ordinates (x,y)
        stroke : rgb(red,green,blue)
            Sets the line color
        fill : rgb(red,green,blue)
            Sets the fill color for the polyline
        stroke_width : int
            Sets the width of the line i.e. pen-size
        """

        points_string = ""
        for i in points:
            points_string += f" {i[0]}, {i[1]}"
        points_string = points_string.strip()
        self.svg_string += f'<polyline points="{points_string}"'\
                           f' stroke="{stroke}" stroke-width='\
                           f'"{stroke_width}" fill="{fill}" />\n'

    # function to draw a polygon
    def polygon(self, points, stroke = rgb(0,0,0), fill = 'transparent',
                stroke_width = 1):
        """Draws a closed shape with atleast 3 sides
        
        Parameters
        ----------
        points : [(int,int),(int,int),(int,int),...]
            List of tuples of co-ordinates (x,y)
        stroke : rgb(red,green,blue)
            Sets the border color for the shape
        fill : rgb(red,green,blue)
            Sets the color to be filled within the shape
        stroke_width : int
            Sets the width of the border i.e. pen-size
        """
        
        points_string = ""
        for i in points:
            points_string += f' {i[0]}, {i[1]}'
        self.svg_string += f'<polygon points="{points_string}"'\
                           f' stroke="{stroke}" fill="{fill}"'\
                           f' stroke-width="{stroke_width}" />\n'

    # functon to draw a path
    def path(self, d):
        """Draws a path formed with complex shapes
        
        Parameters
        ----------
        d : str
            This describes a path to be drawn it can include
            commands like:
                - L (line to)
                - M (move to)
                - H (horizontal line to)
                - V (vertical line to)
                - C (curve to)
                - S (smooth curve to)
                - Q (quadratic Bezier Curve)
                - T (smooth quadratic curve to)
                - A (elleptical arc)
                - Z (close path)
        stroke : rgb(red,green,blue)
            Sets the border color for the path drawn
        fill : rgb(red,green,blue)
            Sets the color to be filled in the path
        stroke_width : int
            Sets the width of the border
        """
        pass

    # function to finally write the svg file
    def write(self,save_as='test.svg'):
        self.svg_string += '</svg>\n'
        with open(save_as,'w') as file:
            file.write(self.svg_string)
    

# test code
obj = SVG(400,500)

obj.point((50,50))
obj.rect((10,30),(100,200), fill="red", stroke_width = 10,stroke = rgb(28,29,150))
obj.circle(center = (40,50), fill = rgb(123,224,200),radius = 150,stroke_width=1)
obj.ellipse(center =(50,60), radii = (40,60), stroke_width = 8, fill = 'crimson')
obj.line((80,90),(200,400),stroke=rgb(19,18,159),stroke_width = 10)
obj.polyline([(12,13),(140,150),(170,90),(90,17)],fill = "#2a8bdc",stroke="crimson")

obj.polygon([(20,30),(150,320),(320,150),(40,50),(10,50)], fill = "crimson")
obj.write()

