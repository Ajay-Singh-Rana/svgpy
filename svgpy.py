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
    def path(self, d : str, stroke = "Black", fill = "Red", stroke_width = "2px"):
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
        
        self.svg_string += f'<path d="{d}" stroke="{stroke}" '\
                           f'stroke-width="{stroke_width}" fill="{fill}"/>\n'

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

    # start a path
    def start_path(self, point : Point = None):
        """This function is used to start a new path in the Image.
        
        Parameters
        ----------
        point : Point
            The point to start from, None by default.
        """

        if(point):
            self.svg_string += f'<path d="M {point.x}, {point.y} '
        else:
            self.svg_string += '<path d="'

    # function to move the cursor to a point without drawing anything
    def move_to(self,point : Point):
        """This function is path specific (Will not work without starting a path).
        This function moves the pen to the
        given point without drawing anything in the path.

        Parameters
        ----------
        point : Point(int, int)
            The (x, y) co-ordinates to move to
        """

        self.svg_string += f'M {point.x}, {point.y} '

    # a function to move the current point by shifting
    def move_by(self, point : Point):
        """This function is path specific (Will not work without starting a path). 
        This function shifts the current point
        by shifting the last known position by point.x along x-axis
        and by point.y along the y-axis.

        Parameters
        ----------
        point : Point(int, int)
            The (x, y) amount to be shifted by
        """

        self.svg_string += f'm {point.x}, {point.y} '
    
    # a function to draw a line from the current point to the given point
    def line_to(self, point : Point):
        """ This function is path specific (Will not work without starting a path).
        This function draws a line from the current position to the given point.

        Parameters
        ----------
        point : Point(int, int)
            The (x, y) co-ordinates of the end point 
        """

        self.svg_string += f'L {point.x}, {point.y} '
    
    # a function to draw a line by shifting the current position
    def line_by(self, point : Point):
        """This function is path specific (Will not work without starting a path).
        This function draws a line from the
        current point to the end point, which is the current point 
        shifted by point.x and point.y 
        amount on x-axis and y-axis respectively.
        
        Parameters
        ----------
        point : Point(int, int)
            The (x, y) co-ordinates to be shifted by
        """

        self.svg_string += f'l {point.x}, {point.y} '
    
    # function to draw a horizontal line from current point to the end point
    def hline_to(self, x : int):
        """This function is path specific (Will not work without starting a path).
        It draws a horizontal line from the current point to the end point
        which is specified by the x parameter and the current point's y 
        co-ordinate.

        Parameters
        ----------
        x : int
            The x co-ordinate of the end point
        """
        
        self.svg_string += f'H {x} '
    
    # function to draw a horizontal line from current point by shifting
    def hline_by(self, x : int):
        """This function is path specific (Will not work without starting a path).
        It draws a horizontal line from the current point to the end point
        which is specified by the current point shifted by x parameter along
        the x-axis and the current point's y co-ordinate.

        Parameters
        ----------
        x : int
            The amount by which to shift the x co-ordinate
        """
        
        self.svg_string += f'h {x} '

    # function to draw a vertical line from current point to the end point
    def vline_to(self, y : int):
        """This function is path specific (Will not work without starting a path) (Will not work without starting a path).
        It draws a vertical line from the current point to the end point
        which is specified by the y parameter and the current point's x
        co-ordinate.

        Parameters
        ----------
        y : int
            The y co-ordinate of the end point
        """
        
        self.svg_string += f'V {y} '
    
    # function to draw a vertical line from current point by shifting
    def vline_by(self, y : int):
        """This is a path specific function (Will not work without starting a path).
        It draws a horizontal line from the current point to the end point
        which is specified by the current point shifted by y parameter along
        the y-axis and the current point's x co-ordinate.

        Parameters
        ----------
        y : int
            The amount by which to shift the x co-ordinate
        """
        
        self.svg_string += f'v {y} '

    # a function to draw cubic Bezier Curve
    def bezier(self, point : Point, control_points : list):
        """This function is path specific (Will not work without starting a path).
        This function draws a cubic Bezier curve from the current
        point to the end point specified by point. The start control
        point is the first point in the control_points list and the 
        end control point is the second point in the list.

        Parameters
        ----------
        point : Point(int, int)
            The point to draw the Bezier curve to
        control_points : list(Point, Point)
            The set of start and end control points
        """

        self.svg_string += f'C {point.x}, {point.y} '\
                           f'{control_points[0].x}, {control_points[0].y} '\
                           f'{control_points[1].x}, '\
                           f'{control_points[1].y} '
    
    # a function to draw a Bezier curve by shifting
    def shift_bezier(self, point: Point, control_points : list):
        """This function is path specific (Will not work without starting a path).
        This function draws a cubic Bezier curve from the current
        point to the end point, which is the current point shifted by point.x
        along x-axis and point.y along y-axis. The start control
        point is the current point shifted by first point in the control_points
        list and the end control point is the current point shifted by
        the second point in the list.

        Parameters
        ----------
        point : Point(int, int)
            The point by which to shift the current point
        control_points : list(Point, Point)
            The set of start and end control point shifts
        """

        self.svg_string += f'c {point.x}, {point.y} '\
                           f'{control_points[0].x}, {control_points[0].y} '\
                           f'{control_points[1].x}, '\
                           f'{control_points[1].y} '
    
    # a function to draw smooth cubic Bezier Curve
    def smooth_bezier(self, point : Point, control_point : Point):
        """This function is path specific (Will not work without starting a path).
        This function draws a smooth cubic Bezier curve from the current
        point to the end point specified by point. The end control point is
        specified by control_point. The start control point is the reflection
        of the end control point of the previous curve command about the
        current point. If the previous command wasn't a cubic Bézier curve, 
        the start control point is the same as the curve starting point
        (current point).

        Parameters
        ----------
        point : Point(int, int)
            The point to draw the Bezier curve to
        control_points : Point(int, int)
            The end control point
        """

        self.svg_string += f'S {point.x}, {point.y} '\
                           f'{control_point.x}, {control_point.y} '
    
    # a function to draw a smooth cubic Bezier curve by shifting
    def shift_smooth_bezier(self, point: Point, control_point : Point):
        """This function is path specific (Will not work without starting a path).
        This function draws a smooth cubic Bezier curve from the current
        point to the end point, which is the current point shifted by point.x
        along x-axis and point.y along y-axis. The end control point is
        specified by the current point shifted by control_point.x along x-axis
        and control_point.y along y-axis. The start control point is the
        reflection of the end control point of the previous curve command about
        the current point. If the previous command wasn't a cubic Bézier curve, 
        the start control point is the same as the curve starting point
        (current point).

        Parameters
        ----------
        point : Point(int, int)
            The point by which to shift the current point
        control_points : Point(int, int)
            The end control point shift
        """

        self.svg_string += f's {point.x}, {point.y} '\
                           f'{control_point.x}, {control_point.y} '

    # a function to draw Quadratic Bezier Curve
    def qudratic_bezier(self, point : Point, control_point : Point):
        """This function is path specific (Will not work without starting a path).
        This function draws a Quadratic Bezier Curve from the current
        point to the end point specified by point and the control point being
        specified by control_point.

        Parameters
        ----------
        point : Point(int, int)
            The point upto which the quadratic curve is to be drawn
        control_point : Point(int, int)
            The control point for the quadratic curve
        """

        self.svg_string += f'Q {point.x}, {point.y} '\
                           f'{control_point.x}, {control_point.y} '

    # a function to draw a Quadratic Bezier Curve by shifting
    def shift_quadratic_bezier(self, point : Point, control_point : Point):
        """This function is path specific (Will not work without starting a path).
        This function draws a quadratic Bezier curve from the current
        point to the end point, which is the current point shifted by point.x
        along x-axis and point.y along y-axis. The control point is
        specified by the current point shifted by control_point.x along x-axis
        and control_point.y along y-axis.

        Parameters
        ----------
        point : Point(int, int)
            The point by which to shift the current point
        control_points : Point(int, int)
            The control point shift
        """

        self.svg_string += f'q {point.x}, {point.y} '\
                           f'{control_point.x}, {control_point.y} '
    
    # a function to draw smooth Quadratic Bezier Curve
    def smooth_quadratic_bezier(self,point : Point):
        """This function is path specific (Will not work without starting a path).
        Draws a smooth quadratic Bézier curve from the 
        current point to the end point specified by point. 
        The control point is the reflection of the control 
        point of the previous curve command about the current
        point. If the previous command wasn't a quadratic Bézier
        curve, the control point is the same as the current point. 
        
        Parameters
        ----------
        point : Point(int, int)
            The point to specify the end point
        """

        self.svg_string += f'T {point.x}, {point.y} '
    
    # a function to draw smooth Quadratic Bezier Curve by shifting
    def smooth_quadratic_bezier(self,point : Point):
        """This function is path specific (Will not work without starting a path).
        Draws a smooth quadratic Bézier curve from the 
        current point to the end point which is specified by the
        current point shifted by point.x along x-axis and point.y along
        y-axis. 
        The control point is the reflection of the control 
        point of the previous curve command about the current
        point. If the previous command wasn't a quadratic Bézier
        curve, the control point is the same as the current point. 
        
        Parameters
        ----------
        point : Point(int, int)
            The point to specify the end point
        """

        self.svg_string += f't {point.x}, {point.y} '

    # a function to close the current subpath
    def end_path(self, close_path = False):
        """This function is path specific (Will not work without starting a path).
        This function is used to close the current subpath by 
        connecting the last point of the path with its initial point.

        Parameters
        ----------
        close_path : Bool, default = False
            Whether or not to close the path
        """

        if(close_path):
            self.svg_string += 'z" />\n'
        else:
            self.svg_string += '" />\n'

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

# obj.point((50,50))
# obj.rect((10,30),(100,200), fill="red", stroke_width = 10,stroke = rgb(28,29,150))
# obj.circle(center = (40,50), fill = rgb(123,224,200),radius = 150,stroke_width=1)
# obj.ellipse(center =(50,60), radii = (40,60), stroke_width = 8, fill = 'crimson')
# obj.line((80,90),(200,400),stroke=rgb(19,18,159),stroke_width = 10)
# obj.polyline([(12,13),(140,150),(170,90),(90,17)],fill = "#2a8bdc",stroke="crimson")

# obj.polygon([(20,30),(150,320),(320,150),(40,50),(10,50)], fill = "crimson")
# obj.text(Point(0,90),text = "Hi there..!",fill=rgb(110,230,245))
# obj.link_text(Point(90,90),text ="Url herererwrwerwrw",url = "https://www.github.com/Ajay-Singh-Rana",fill = rgb(45,46,230))
obj.start_path(Point(45,45))
# obj.move_to(Point(10,10))
obj.line_to(Point(25,25))
obj.line_to(Point(280,396))
obj.end_path(True)
# obj.path(d = "M 30,30 L 25, 25 L 280, 396 Z")
obj.write()

