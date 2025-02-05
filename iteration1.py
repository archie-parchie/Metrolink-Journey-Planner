#modules
import pygame

pygame.init()

#classes
class Results():
    def __init__(self, width, height, x_pos, y_pos, light_mode_colour, dark_mode_colour):
        self.width = width #int
        self.height = height #int
        self.x_pos = x_pos #int
        self.y_pos = y_pos #int
        self.light_mode_colour = light_mode_colour #tuple
        self.dark_mode_colour = dark_mode_colour #tuple
        self.rectangle = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.mode = "default"

    def get_light_mode_colour(self):
        return self.light_mode_colour
    
    def get_dark_mode_colour(self):
        return self.dark_mode_colour

    def display(self, surface, colour):
        pygame.draw.rect(surface, colour, self.rectangle)
        if self.mode == "default":
            header = Text("Search Results", 47, True, (0, 0, 0), (255, 255, 255), (957,7))
            header.display(win, header.get_light_mode_colour()) #displays default title text
            text = "Results will appear here once a route has been searched for!"
            font = pygame.font.SysFont("calibri", 30)
            text_rect = pygame.Rect((955, 70, 336, 560))
            rendered_text = render_textrect(text, font, text_rect, (0, 0, 0), self.light_mode_colour)
            win.blit(rendered_text, text_rect.topleft) #displays default placeholder message
        
class Tram_Stop(): #creates and holds information about tram stops
    def __init__(self, name, lines, neighbours, parking, lift, transport_links, x_pos, y_pos):
        self.name = name #str
        self.lines = lines #list of Line objects
        self.neighbours = neighbours #dict
        self.parking = parking #int
        self.lift  = lift #str
        self.transport_links = transport_links #list
        self.x_pos = x_pos #int
        self.y_pos = y_pos #int
        self.light_mode_colour = (204, 205, 207)
        self.light_mode_text_colour = (0, 0, 0)

    def get_name(self):
        return self.name
    
    def get_lines(self):
        line_names = []
        for i in self.lines:
            line_names.append(i.get_name())
        return line_names
    
    def get_neighbours(self):
        return self.neighbours
    
    def get_parking(self):
        return self.parking
    
    def get_transport_links(self):
        return self.transport_links
    
    def display(self, surface, colour, label_colour): #displays the stop and its name
        pygame.draw.circle(surface, colour, (self.x_pos, self.y_pos), 3)
        font = pygame.font.SysFont("calibri", 10)
        label = font.render(self.name, True, label_colour)
        label_rect = label.get_rect(center=(self.x_pos, self.y_pos - 5))
        surface.blit(label, label_rect)
    
    #def approaching_trams(self): #shows next tram stops arriving at this stop

class Connector(): #creates the connectors between tram stops
    def __init__(self, x_pos, y_pos, width, height, line, stops):
        self.x_pos = x_pos #int
        self.y_pos = y_pos #int
        self.width = width #int
        self.height = height #int
        self.line = line #Line object
        self.stops = stops #list of Tram_Stop objects

    def get_line(self):
            return self.line.get_name()
        
    def get_stops(self):
        stop_names = []
        for i in self.stops:
            stop_names.append(i.get_name())
        return stop_names #returns the names as strings, not Tram_Stop objects
    
    def display(self, surface):
        colour = self.line.get_colour()
        pygame.draw.rect(surface, colour, pygame.Rect(self.x_pos, self.y_pos, self.width, self.height))

    #def highlight(): #highlights the connector when it is on a selected route

class Stop_Input(): #creates the user stop input boxes
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos #int
        self.y_pos = y_pos #int
        self.stored_stop =  ""
        self.light_mode_colour = (219, 219, 213)
        self.dark_mode_colour = (98, 97, 99)
    
    def get_stored_stop(self):
        return self.stored_stop
    
    def get_light_mode_colour(self):
        return self.light_mode_colour
    
    def get_dark_mode_colour(self):
        return self.dark_mode_colour
    
    #def set_stored_stop #makes the rectangle into a functioning user input box and stores the input.

    def display(self, surface, colour):
        pygame.draw.rect(surface, colour, pygame.Rect(self.x_pos, self.y_pos, 130, 40), 0, 7)
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(self.x_pos-1.5, self.y_pos-1.5, 133, 43), 2, 7)

class Line(): #holds information about each Metrolink line
    def __init__(self, name, stops, colour):
        self.name = name #str
        self.stops = stops #list of Tram_Stop objects
        self.colour = colour #tuple of RGB values
    
    def get_name(self):
        return self.name
    
    def get_stops(self):
        stop_names = []
        for i in self.stops:
            stop_names.append(i.get_name())
        return stop_names #returns the names as strings, not Tram_Stop objects
    
    def get_colour(self):
        return self.colour

class Info(): #creates the information icon
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos #int
        self.y_pos = y_pos #int
        self.light_mode_colour = (0, 0, 0)
        self.dark_mode_colour = (255, 255, 255)
    
    def get_light_mode_colour(self):
        return self.light_mode_colour
    
    def get_dark_mode_colour(self):
        return self.dark_mode_colour

    def display(self, surface, colour):
        pygame.draw.circle(surface, colour, (self.x_pos, self.y_pos), 10, width = 3)
        font = pygame.font.SysFont("calibri", 10, bold = True)
        label = font.render("i", True, colour)
        label_rect = label.get_rect(center = (self.x_pos, self.y_pos))
        surface.blit(label, label_rect)

class Colour_Toggle():
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos #int
        self.y_pos = y_pos #int
        self.colour_mode = "light"
    
    def get_colour_mode(self):
        return self.colour_mode

    #def change_mode(self) #if toggle selected, change the value of colour_mode

    #def display(self) #creates and displays the toggle

class Text():
    def __init__(self, text, size, bold, light_mode_colour, dark_mode_colour, coords):
        self.text = text #str
        self.size = size #int
        self.bold = bold #bool
        self.light_mode_colour = light_mode_colour #tuple
        self.dark_mode_colour = dark_mode_colour #tuple
        self.coords = coords #tuple
    
    def get_light_mode_colour(self):
        return self.light_mode_colour
    
    def get_dark_mode_colour(self):
        return self.dark_mode_colour

    def display(self, surface, colour):
        font = pygame.font.SysFont("calibri", self.size, bold = self.bold)
        to_render = font.render(self.text, True, colour)
        surface.blit(to_render, self.coords)

class TextRectException:
    def __init__(self, message = None):
        self.message = message
    def __str__(self):
        return self.message
#constants

#functions
def main():
    running = True
    instantiation()
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                running=False

def render_textrect(string, font, rect, text_color, background_color, justification=0): #displays texts in paragraphs - code from https://www.pygame.org/pcr/text_rect/index.php
    final_lines = []
    requested_lines = string.splitlines()

    # Create a series of lines that will fit on the provided rectangle.
    for requested_line in requested_lines:
        if font.size(requested_line)[0] > rect.width:
            words = requested_line.split(' ')
            # if any of our words are too long to fit, return.
            for word in words:
                if font.size(word)[0] >= rect.width:
                    raise TextRectException("The word " + word + " is too long to fit in the rect passed.")
            # Start a new line
            accumulated_line = ""
            for word in words:
                test_line = accumulated_line + word + " "
                # Build the line while the words fit.    
                if font.size(test_line)[0] < rect.width:
                    accumulated_line = test_line 
                else: 
                    final_lines.append(accumulated_line) 
                    accumulated_line = word + " " 
            final_lines.append(accumulated_line)
        else: 
            final_lines.append(requested_line) 

    # Let's try to write the text out on the surface.
    surface = pygame.Surface(rect.size) 
    surface.fill(background_color) 

    accumulated_height = 0 
    for line in final_lines: 
        if accumulated_height + font.size(line)[1] >= rect.height:
            raise TextRectException("Once word-wrapped, the text string was too tall to fit in the rect.")
        if line != "":
            tempsurface = font.render(line, 1, text_color)
            if justification == 0:
                surface.blit(tempsurface, (0, accumulated_height))
            elif justification == 1:
                surface.blit(tempsurface, ((rect.width - tempsurface.get_width()) / 2, accumulated_height))
            elif justification == 2:
                surface.blit(tempsurface, (rect.width - tempsurface.get_width(), accumulated_height))
            else:
                raise TextRectException("Invalid justification argument: " + str(justification))
        accumulated_height += font.size(line)[1]

    return surface


def instantiation(): #instantiates all the objects required
    global win
    win = pygame.display.set_mode((1250, 630))
    pygame.display.set_caption("Metrolink Journey Planner")
    objects = []

    #creating all objects and appending them to a list to be displayed at once
    colour_switch = Colour_Toggle(1000, 20)
    info = Info(20, 610)
    objects.append(info)
    heading = Text("Metrolink Journey Planner", 60, True, (0, 0, 0), (255, 255, 255), (7, 7))
    objects.append(heading)
    results_section = Results(350, 630, 950, 0, (201, 201, 191), (98, 97, 99))
    objects.append(results_section)
    start_stop_text = Text("Start Stop", 35, False, (0, 0, 0), (255, 255, 255), (7, 80))
    objects.append(start_stop_text)
    start_stop_input = Stop_Input(153, 80)
    objects.append(start_stop_input)
    end_stop_text = Text("End Stop", 35, False, (0, 0, 0), (255, 255, 255), (330, 80))
    objects.append(end_stop_text)
    end_stop_input = Stop_Input(460, 80)
    objects.append(end_stop_input)
    
    #drawing all objects
    light_or_dark = colour_switch.get_colour_mode()
    if light_or_dark == "light":
        win.fill((255, 244, 135))
        for i in objects:
            i.display(win, i.get_light_mode_colour())
    else:
        win.fill((28, 28, 27))
        for i in objects:
            i.display(win, i.get_dark_mode_colour())
    pygame.display.update()
    
    #if colour mode light, then .display() with object.light_mode_colour passed as colour

main()
