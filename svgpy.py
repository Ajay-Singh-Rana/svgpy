# h3avren

# a function to handle rgb colors as a string
def rgb(red,green,blue):
    return f"rgb({red},{green},{blue})"


# a function to handle hsl colors as a string
def hsl(hue, saturation, light):
    return f'hsl({hue}, {saturation}, {light})'

# a class to handle points
class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def __repr__(self):
        return (self.x, self.y)

    def __str__(self):
        return f'(x = {self.x} , y = {self.y})'



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
                           '" xmlns="http://www.w3.org/2000/svg" '\
                           'xmlns:xlink="http://www.w3.org/1999/xlink">\n'
    
    # function to draw a point
    def point(self, point : Point, fill = rgb(0,0,0)):
        """Draws a point in the SVG image
        
        Parameters
        ----------
        point : Point(int,int)
            co-ordinates of the point
        fill : rgb(red, green, blue) / #rrggbb / hsl(hue, saturation, light)

            fill color of the point
        """

        self.svg_string += f'<rect x="{point.x}" y="{point.y}" width = "1"'\
                           f' height="1" stroke-width="1" stroke="{fill}" />\n'
  
    # function to draw a rectangle
    def rect(self, start : Point, size, rx = 0, ry = 0, stroke = rgb(0, 0, 0), 
             fill = "transparent", stroke_width = 1):
        """Draws a rectangle in the SVG image

        Parameters
        ----------
        start : Point(int, int)
            The x,y co-ordinates of the start/initial point
        size : (int, int)
            The width, height of the rectangle
            could also be considered as x2-x1,y2-y1
            i.e. difference of start and end points of rectangle
        rx : int
            The x radius of the corners of the rectangle
        ry : int
            The y radius of the corners of the rectangle
        stroke : rgb(red, green, blue) / #rrggbb / hsl(hue, saturation, light)
            Sets the border color for the rectangle
        fill : rgb(red, green, blue) / #rrggbb / hsl(hue, saturation, light)
            Sets the color to be filled inside the rectangle 
        stroke_width : int
            The width of the stroke i.e. border or pen-size
        """

        self.svg_string += f'<rect x="{start.x}" y="{start.y}"'\
                           f' width="{size[0]}" height = "{size[1]}"'\
                           f' rx="{rx}" ry="{ry}" stroke="{stroke}"' \
                           f' fill="{fill}" stroke-width="{stroke_width}" />\n'
    
    # function to draw a circle
    def circle(self, center : Point, radius, stroke = rgb(0,0,0), 
               fill = "transparent", stroke_width = 1):
        """Draws a circle in the SVG image

        Parameters
        ----------
        center : Point(int, int)
            The x,y co-ordinates for the center of the circle
        radius : int
            The radius of the circle
        stroke : rgb(red, green, blue) / #rrggbb / hsl(hue, saturation, light)
            Sets the border color for the circle
        fill : rgb(red, green, blue) / #rrggbb / hsl(hue, saturation, light)
            Sets the color to be filled inside the circle
        stroke_width : int
            The width of the stroke i.e. border or pen-size
        """

        self.svg_string += f'<circle cx="{center.x}" cy="{center.y}"'\
                           f' r="{radius}" stroke="{stroke}"'\
                           f' fill="{fill}" stroke-width="{stroke_width}" />\n'

    # function to draw an ellipse
    def ellipse(self, center : Point, radii, stroke = rgb(0,0,0),
                fill = "transparent", stroke_width = 1):
        """Draws an ellipse in the SVG image

        Parameters
        ----------
        center : Point(int,int)
            The x,y co-ordinates for the center of the ellipse
        radii : (int,int)
            The radiuses of the ellipse along x-axis,y-axis
        stroke : rgb(red, green, blue) / #rrggbb / hsl(hue, saturation, light)
            Sets the border color for the ellipse
        fill : rgb(red, green, blue) / #rrggbb / hsl(hue, saturation, light)
            Sets the color to be filled inside the ellipse
        stroke_width : int
            The width of the stroke i.e. border or pen-size
        """

        self.svg_string += f'<ellipse cx="{center.x}" cy="{center.y}"'\
                           f' rx="{radii[0]}" ry="{radii[1]}"'\
                           f' stroke="{stroke}"'\
                           f' fill="{fill}" stroke-width="{stroke_width}" /> \n'

    # function to draw a line
    def line(self, start : Point, end : Point, stroke = rgb(0,0,0), stroke_width = 1):
        """Draws a line in the SVG image

        Parameters
        ----------
        start : Point(int,int)
            The co-ordinates x,y for the initial point
        end : Point(int,int)
            The co-ordinates x,y for the end point
        stroke : rgb(red, green, blue) / #rrggbb / hsl(hue, saturation, light)
            Sets the line color
        stroke_width : int
            The width of the line or pen-size
        """
        
        self.svg_string += f'<line x1="{start.x}" y1="{start.y}"'\
                           f' x2="{end.x}" y2="{end.y}" stroke="{stroke}"'\
                           f' stroke-width="{stroke_width}" />\n'

    # function to draw a polyling
    def polyline(self, points, stroke = rgb(0,0,0), fill = 'transparent',
                 stroke_width = 1):
        """Draws a line connecting several points/line segments

        Parameters
        ----------
        points : [Point(int,int), Point(int,int), Point(int,int), ...]
            List of tuples of co-ordinates (x,y)
        stroke : rgb(red, green, blue) / #rrggbb / hsl(hue, saturation, light)
            Sets the line color
        fill : rgb(red, green, blue) / #rrggbb / hsl(hue, saturation, light)
            Sets the fill color for the polyline
        stroke_width : int
            Sets the width of the line i.e. pen-size
        """

        points_string = ""
        for point in points:
            points_string += f" {point.x}, {point.y}"
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
        points : [Point(int,int), Point(int,int), Point(int,int),...]
            List of tuples of co-ordinates (x,y)
        stroke : rgb(red, green, blue) / #rrggbb / hsl(hue, saturation, light)
            Sets the border color for the shape
        fill : rgb(red, green, blue) / #rrggbb / hsl(hue, saturation, light)
            Sets the color to be filled within the shape
        stroke_width : int
            Sets the width of the border i.e. pen-size
        """
        
        points_string = ""
        for point in points:
            points_string += f' {point.x}, {point.y}'
        self.svg_string += f'<polygon points="{points_string}"'\
                           f' stroke="{stroke}" fill="{fill}"'\
                           f' stroke-width="{stroke_width}" />\n'

    # function to draw a path
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
        stroke : rgb(red, green, blue) / #rrggbb / hsl(hue, saturation, light)
            The color name or code for the border
        fill : rbg(red, green, blue) / #rrggbb / hsl(hue, saturation, light)
            The color to be filled in the shape
        stroke_width : int
            Sets the width of the border
        """
        pass

    # function to finally write the svg file
    def write(self,save_as='test.svg'):
        """This function writes the final SVG file

        Parameters
        ----------
        save_as : str
            This is the name the file will be saved by
        """

        self.svg_string += '</svg>\n'
        with open(save_as,'w') as file:
            file.write(self.svg_string)

    # function to move the cursor to a point without drawing anything
    def move_to(self,point : Point):
        """This function moves the pen to the given point without
           drawing anything in the SVG.

        Parameters
        ----------
        point : Point(int, int)
            The (x, y) co-ordinates to move to
        """

        self.svg_string += f'<path d="M {point.x} {point.y}" />\n'

    # function to draw an arrow
    def arrow(self, point : Point, width = 25, length = 100, stroke = "#001122", 
              fill = "#F9F9F9", stroke_width = 1):
        """This function draws an arrow in the SVG

        Parameters
        ----------
        point : Point(int, int)
            The (x,y) co-ordinates to draw the arrow at
        width : int
            The width of the arrow
        length : int
            The length of the arrow tail
        stroke_width : int
            The width of the arrow borders
        stroke : rgb(red, green, blue) / #rrggbb / hsl(hue, saturation, light)
            The color name or code for the border
        fill : rbg(red, green, blue) / #rrggbb / hsl(hue, saturation, light)
            The color to be filled in the arrow
        """

        up = width + point.y
        forward = length + point.x
        arrow_head = up + (int(width * 0.5) if (width % 2 == 0) 
                           else (width//2 + 1))
        arrow_mid_x = forward + int(length * 0.2)
        arrow_mid_y = point.y + (width//2)
        arrow_bottom = point.y - (int(width * 0.5) if (width % 2 == 0)
                                   else (width//2 - 1))

        self.svg_string += f'<path d="M {point.x} {point.y}'\
                           f' V {up} H {forward} V {arrow_head}'\
                           f' L {arrow_mid_x} {arrow_mid_y}'\
                           f' L {forward} {arrow_bottom} V {point.y}'\
                           f' H {point.x}" stroke = "{stroke}"'\
                           f' fill = "{fill}"'\
                           f' stroke-width = "{stroke_width}" />\n'
        
    # function to add text to the svg
    def text(self, point : Point, text : str, fill = rgb(255, 255, 255),
             transform = "rotate(0,0,0)"):
        """This function writes text on to the SVG

        Parameters
        ----------

        point : Point(int, int)
            The (x,y) co-ordinates to write the text from
        text : str
            The text to be written on the image
        fill : rgb(red, green, blue) / #rrggbb / hsl(hue, saturation, light)
            The color for the text
        transform : rotate(180,180,32)
            The transformation to be applied 
        """

        text_string = f'<text x="{point.x}" y="{point.y}" '\
                      f'fill="{fill}" transform="{transform}">{text}'\
                      f'</text>\n'

        self.svg_string += text_string
        return text_string

    # adding text that serves as a link
    def link_text(self, point: Point, text : str, url : str,
                  fill = rgb(255, 255, 255)):
        """This function adds text to the image which acts a link

        Parameters
        ----------

        point : Point(int, int)
            The (x,y) co-ordinate to write the text from
        text : str
            The text to be written on the image
        url : str
            The link to redirect with the text to
        fill : rgb(red, green, blue) / #rrggbb / hsl(hue, saturation, light)
            The color for the text
        """

        self.svg_string += f'<a xlink:href="{url}" target="_blank">\n'\
                           f'{self.text(point, text, fill)}'\
                           f'</a>\n'


# test code
obj = SVG(400,500)

obj.point((50,50))
obj.rect((10,30),(100,200), fill="red", stroke_width = 10,stroke = rgb(28,29,150))
obj.circle(center = (40,50), fill = rgb(123,224,200),radius = 150,stroke_width=1)
obj.ellipse(center =(50,60), radii = (40,60), stroke_width = 8, fill = 'crimson')
obj.line((80,90),(200,400),stroke=rgb(19,18,159),stroke_width = 10)
obj.polyline([(12,13),(140,150),(170,90),(90,17)],fill = "#2a8bdc",stroke="crimson")

obj.polygon([(20,30),(150,320),(320,150),(40,50),(10,50)], fill = "crimson")
obj.text(Point(0,90),text = "Hi there..!",fill=rgb(110,230,245))
obj.link_text(Point(90,90),text ="Url herererwrwerwrw",url = "https://www.github.com/Ajay-Singh-Rana",fill = rgb(45,46,230))
obj.write()

