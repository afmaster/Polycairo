import cairo
import math


class Polygon:
    def __init__(self, edge_numbers, canvas_size):
        self.edges = edge_numbers
        self.angle = 360/self.edges
        self.side = canvas_size
        self.radius = self.side/2
    
    def coordinates(self, slice_angle):
        slice_angle = slice_angle
        radius = self.radius
        real_angle = 360 - 1*slice_angle 
        seno_angle = round(math.sin(real_angle * math.pi/180), 2)
        cosseno_angle = round(math.cos(real_angle * math.pi/180),2)
        y = radius - seno_angle * radius 
        x = l - (radius - cosseno_angle * radius)
        return x, y
    
    def corner_coordinates(self, desired_angle, l):
        angle = desired_angle
        real_angle = 360 - 1 * angle 
        seno_angulo = round(math.sin(real_angle * math.pi/180), 2)
        cosseno_angulo = round(math.cos(real_angle * math.pi/180),2)
        radius = l/2
        y = radius - seno_angulo * radius 
        x = l - (radius - cosseno_angulo * radius)
        print("x", x)
        print("y", y)
        return x, y
    
    def construct_corners(self):
        if self.edges%2 != 0:
            corners = [(self.side, self.side/2)]
            
        else:
            corner_1 = self.corner_coordinates(self.angle/2, 270 - self.side)
            print("corner1", corner_1)
            corners = [(self.side, self.side/2)]
                
        for edge in range(1, (self.edges)):
            slice_angle = self.angle * (edge)
            next_corner = self.coordinates(slice_angle)
            corners.append(next_corner)
            print("corners", corners)
        return corners
    
    def construct_polygon(self):
        corners = self.construct_corners()
        ctx.move_to(corners[0][0], corners[0][1])
        for corner in corners:
            ctx.line_to(corner[0], corner[1])
            print("corner of the time", corner)
        ctx.close_path()
        ctx.set_source_rgba(0, 0, 0)
        ctx.set_line_width(2)
        ctx.stroke()


if __name__ == "__main__": 
    def draw_background(ctx, r, g, b, width, height):
        ctx.set_source_rgb(r, g, b)
        ctx.rectangle(0, 0, width, height)
        ctx.fill()

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 300, 300)
    ctx = cairo.Context(surface)
    draw_background(ctx, 0.5, 0.5, 0.5, 600, 600)
    figure = Polygon(8, 300)
    figure.construct_polygon()
    surface.write_to_png("polygon.png")
