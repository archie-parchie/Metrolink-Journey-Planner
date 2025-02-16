#modules
import pygame

pygame.init()

#classes
class Results():
    def __init__(self):
        self.width = 350
        self.height = 630
        self.x_pos = 950
        self.y_pos = 0
        self.light_mode_colour = (201, 201, 191)
        self.dark_mode_colour = (88, 88, 88)
        self.rectangle = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.mode = "default"

    def get_light_mode_colour(self):
        return self.light_mode_colour
    
    def get_dark_mode_colour(self):
        return self.dark_mode_colour

    def display(self, colour):
        if colour == self.light_mode_colour:
            text_colour = (0, 0, 0)
            bg_colour = self.light_mode_colour
        else:
            text_colour = (255, 255, 255)
            bg_colour = self.dark_mode_colour
        pygame.draw.rect(win, colour, self.rectangle)
        if self.mode == "default":
            header = Text("Search Results", 47, True, (0, 0, 0), (255, 255, 255), (957,7))
            header.display(text_colour) #displays default title text
            text = "Results will appear here once a route has been searched for!"
            font = pygame.font.SysFont("calibri", 30)
            text_rect = pygame.Rect((955, 70, 336, 560))
            rendered_text = render_textrect(text, font, text_rect, text_colour, bg_colour)
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
    
    def display(self, colour, label_colour): #displays the stop and its name
        pygame.draw.circle(win, colour, (self.x_pos, self.y_pos), 3)
        font = pygame.font.SysFont("calibri", 10)
        label = font.render(self.name, True, label_colour)
        label_rect = label.get_rect(center=(self.x_pos, self.y_pos - 5))
        win.blit(label, label_rect)
    
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
    
    def display(self):
        colour = self.line.get_colour()
        pygame.draw.rect(win, colour, pygame.Rect(self.x_pos, self.y_pos, self.width, self.height))

    #def highlight(): #highlights the connector when it is on a selected route

class Stop_Input(): #creates the user stop input boxes
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos #int
        self.y_pos = y_pos #int
        self.stored_stop =  ""
        self.inputted_text = ""
        self.on_screen = ""
        self.light_mode_colour = (219, 219, 213)
        self.dark_mode_colour = (107, 107, 107)
        self.rect = pygame.Rect(self.x_pos, self.y_pos, 150, 40)
        self.active = False
    
    def get_stored_stop(self):
        return self.stored_stop
    
    def get_light_mode_colour(self):
        return self.light_mode_colour
    
    def get_dark_mode_colour(self):
        return self.dark_mode_colour
    
    def get_inputted_text(self):
        return self.inputted_text
    
    def get_active(self):
        return self.active
    
    def set_inputted_text(self, new):
        self.inputted_text = new
    
    def set_stored_stop(self, new):
        self.stored_stop = new
    
    def get_active(self):
        return self.active
    
    def set_active(self):
        self.active = not self.active
    
    def pressed(self, obj): #checks if the stop has been pressed
        pos = pygame.mouse.get_pos()
        action = False
        if self.rect.collidepoint(pos): #checks if the mouse is over the rect
            if pygame.mouse.get_pressed()[0]: #checks if a left click has occured
                draw() #redraws objects to cover potential error message
                self.active = not self.active
                action = True
            if self.active == True and action == True: #executing code only if a click to active has just occured
                self.inputted_text = "" #resetting initial conditions
                self.on_screen = ""
                if objects[10].get_colour_mode() == True:
                    self.display((196, 196, 192)) #changing colour of the box to indicate active to user
                else:
                    self.display((140, 139, 139))
                if obj == objects[4]: #checking if the start or stop input is currently being operated on
                    if objects[6].get_active() == True:
                        objects[6].set_active()
                else:
                    if objects[4].get_active() == True:
                        objects[4].set_active()
                
    def text_input(self, event, colour_mode, stops): #takes in text input and displays it in the input box
        if event.key == pygame.K_BACKSPACE:
            self.inputted_text = self.inputted_text[:-1] #keeps all but the last letter inputted
            self.on_screen = self.on_screen[:-1]
        elif event.key == pygame.K_RETURN: #considering the text input as a whole once enter has been pressed
            correct_input = False
            self.active = False
            for i in stops: #checks if the inputted text matches a tram stop
                if i.lower() == self.inputted_text.lower():
                    self.stored_stop = i
                    correct_input = True
            if correct_input == False: #displaying a message if a tram stop is not inputted
                self.inputted_text = ""
                self.on_screen = ""
                incorrect_message = pygame.font.SysFont("calibri", 20, bold = False)
                incorrect_text = incorrect_message.render("Invalid Input! Please try again.", True, (145, 7, 7))
                win.blit(incorrect_text, (self.x_pos, self.y_pos + 50))
        else:
            self.inputted_text += event.unicode #concatenates the last letter inputted to the string
            self.on_screen += event.unicode

        if colour_mode == True: #displaying the text in light mode
            text_colour = (0, 0, 0)
            if self.active == False:
                box_colour = self.light_mode_colour
            else:
                box_colour = (196, 196, 192)
        else: #displaying the text in dark mode
            text_colour = (255, 255, 255)
            if self.active == False:
                box_colour = self.dark_mode_colour
            else:
                box_colour = (140, 139, 139)

        font = pygame.font.SysFont("calibri", 30, bold = False)
        display_text = font.render(self.on_screen, True, (text_colour))

        while self.rect.w - 4 < display_text.get_width() + 4: #scrolls along the text if there's too much to display
            self.on_screen = self.on_screen[1:]
            display_text = font.render(self.on_screen, True, (text_colour))

        self.display(box_colour) #redraws the box to cover up previously typed letters
        win.blit(display_text, (self.rect.x + 4, self.rect.y + 4))            

    def display(self, colour): 
        if colour == self.light_mode_colour or colour == (196, 196, 192):
            if self.active == True: #checks if box needs to be drawn in active state
                colour = (196, 196, 192)
            outline_colour = (0, 0, 0)
            text_colour = (0, 0, 0)
        else:
            if self.active == True:
                colour = (140, 139, 139)
            outline_colour = (255, 255, 0)
            text_colour = (255, 255, 255)
        pygame.draw.rect(win, colour, self.rect, 0, 7)
        pygame.draw.rect(win, outline_colour, self.rect, 2, 7)
        font = pygame.font.SysFont("calibri", 30, bold = False)
        display_text = font.render(self.on_screen, True, (text_colour))
        win.blit(display_text, (self.rect.x + 4, self.rect.y + 4)) #drawing the current input text

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
    def __init__(self):
        self.x_pos = 20 #int
        self.y_pos = 610 #int
        self.light_mode_colour = (0, 0, 0)
        self.dark_mode_colour = (255, 255, 0)
        self.active = False
        self.rect = pygame.Rect(self.x_pos - 10, self.y_pos - 10, 20, 20)
        
    def get_light_mode_colour(self):
        return self.light_mode_colour
    
    def get_dark_mode_colour(self):
        return self.dark_mode_colour
    
    def pressed(self): #deals with clicks and displays the information box if self.active = True
        action = False #assumes the icon hasn't been pressed
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos): #checks if the mouse is over the rect
            if pygame.mouse.get_pressed()[0]: #checks if the mouse has left clicked
                self.active = not self.active
                action = True
        if self.active == True: #shows the message whenever "active" i.e. the button was pressed previously
            message_font = pygame.font.SysFont("calibri", 15)
            message_text = "Click on a box to input a stop. \nClick on the drop-down box to choose when to leave and press 'Find Route' to find the shortest route. \nThe price calculator will appear once a route is chosen. \nClick on a tram stop to see the next trams leaving from it."
            message_rect = pygame.Rect((16, 615, 250, 122))
            message_rect.bottomleft = (16, 615)
            padding_rect = pygame.Rect((16, 615, 260, 128)) #larger rect to add text padding
            padding_rect.center = message_rect.center
            outline_rect = pygame.Rect((16, 615, 260, 128)) #rect to add an outline
            outline_rect.center = message_rect.center
            if objects[10].get_colour_mode() == True: #checks colour mode to display the message correctly
                rendered_text = render_textrect(message_text, message_font, message_rect, (0, 0, 0), (219, 219, 213))
                pygame.draw.rect(win, (219, 219, 213), padding_rect, 0, 7) #drawing padding
                pygame.draw.rect(win, (0, 0, 0), outline_rect, 2, 7) #drawing outline
            else:
                rendered_text = render_textrect(message_text, message_font, message_rect, (255, 255, 255), (98, 97, 99))
                pygame.draw.rect(win, (98, 97, 99), padding_rect, 0, 7)
                pygame.draw.rect(win, (255, 255, 0), outline_rect, 2, 7)
            win.blit(rendered_text, message_rect)

        else:
            if action == True: #only runs if a click has actually occured
                draw() #redrawing all objects to remove the information box from the screen
                     

    def display(self, colour):
        pygame.draw.circle(win, colour, (self.x_pos, self.y_pos), 10, width = 3)
        font = pygame.font.SysFont("calibri", 10, bold = True)
        label = font.render("i", True, colour)
        label_rect = label.get_rect(center = (self.x_pos, self.y_pos))
        win.blit(label, label_rect)
        if self.active == True:
            self.pressed() #displays the information box immediately if appropriate


class Colour_Toggle(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self) #inheriting from the sprite inbuilt class
        self.light_mode_image = pygame.image.load("Light.png")
        self.dark_mode_image = pygame.image.load("Dark.png")
        self.scale = (40, 20) #sizing the image
        self.image = pygame.transform.scale(self.light_mode_image, self.scale)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos #int
        self.rect.y = y_pos #int
        self.colour_mode = True #initialises the program in light mode

    def get_colour_mode(self):
        return self.colour_mode

    def change_mode(self): #if toggle selected, change the value of colour_mode
        action = False #checks if a click has occured
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos): #checks if the mouse is over the rect
            if pygame.mouse.get_pressed()[0]: #checks if the mouse has left clicked
                if self.colour_mode == False: #checks current colour mode
                    self.colour_mode = True
                    self.image = pygame.transform.scale(self.light_mode_image, self.scale)
                else:
                    self.colour_mode = False
                    self.image = pygame.transform.scale(self.dark_mode_image, self.scale)
                action = True
        return action

    def display(self): #displays the toggle
        win.blit(self.image, self.rect)

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

    def display(self, colour):
        font = pygame.font.SysFont("calibri", self.size, bold = self.bold)
        to_render = font.render(self.text, True, colour)
        win.blit(to_render, self.coords)

class Login():
    def __init__(self):
        self.rect = pygame.Rect((900, 500, 50, 34))
        self.rect.bottomright = (812, 619) #setting the position just before the create account button
        self.light_mode_colour = (219, 219, 213)
        self.dark_mode_colour = (107, 107, 107)

    def get_light_mode_colour(self):
        return self.light_mode_colour
    
    def get_dark_mode_colour(self):
        return self.dark_mode_colour

    def display(self, colour):
        font = pygame.font.SysFont("calibri", 18, bold = False)
        if colour == self.light_mode_colour:
            text = font.render("Log In", True, (0, 0, 0)) #creating the text
            pygame.draw.rect(win, self.light_mode_colour, self.rect, 0, 7) #displaying the box
            pygame.draw.rect(win, (0, 0, 0), self.rect, 2, 7) #displaying the box outline
        else:
            text = font.render("Log In", True, (255, 255, 255))
            pygame.draw.rect(win, self.dark_mode_colour, self.rect, 0, 7)
            pygame.draw.rect(win, (255, 255, 0), self.rect, 2, 7)
        text_rect = text.get_rect(center = (787, 602))
        win.blit(text, text_rect) #displaying the text

class Create_Account():
    def __init__(self):
        self.rect = pygame.Rect((900, 500, 118, 34))
        self.rect.bottomright = (940, 619) #setting the position just before the results section
        self.light_mode_colour = (219, 219, 213)
        self.dark_mode_colour = (107, 107, 107)
    
    def get_light_mode_colour(self):
        return self.light_mode_colour
    
    def get_dark_mode_colour(self):
        return self.dark_mode_colour

    def display(self, colour):
        font = pygame.font.SysFont("calibri", 18, bold = False)
        pygame.draw.rect(win, colour, self.rect, 0, 7) #displaying the box
        if colour == self.light_mode_colour:
            text = font.render("Create Account", True, (0, 0, 0)) #creating the text
            pygame.draw.rect(win, (0, 0, 0), self.rect, 2, 7) #displaying the box outline
        else:
            text = font.render("Create Account", True, (255, 255, 255))
            pygame.draw.rect(win, (255, 255, 0), self.rect, 2, 7)
        text_rect = text.get_rect(center = (880, 602))
        win.blit(text, text_rect) #displaying the text

class Leaving_Time(): #drop down box to select calculation mode and corresponding time
    def __init__(self):
        self.x_pos = 640
        self.y_pos = 80
        self.width = 86
        self.height = 40
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.light_mode_colour = (219, 219, 213)
        self.dark_mode_colour = (107, 107, 107)
        self.mode = "Leave now"
        self.active = False #indicates if the drop-down menu should currently be shown
        self.time_active = False #indicates if a second input box for a time should currently be shown
        self.rect1 = pygame.Rect(self.x_pos, self.y_pos + 45, self.width, self.height)
        self.rect2 = pygame.Rect(self.x_pos, self.y_pos + 85, self.width, self.height)
        self.rect3 = pygame.Rect(self.x_pos, self.y_pos + 125, self.width, self.height)
    
    def get_light_mode_colour(self):
        return self.light_mode_colour
    
    def get_dark_mode_colour(self):
        return self.dark_mode_colour

    def display(self, colour):
        pygame.draw.rect(win, colour, self.rect, 0, 7) #drawing the main box
        font = pygame.font.SysFont("calibri", 18, bold = False)
        if colour == self.light_mode_colour:
            pygame.draw.rect(win, (0, 0, 0), self.rect, 2, 7) #drawing the outline
            text = font.render(self.mode, True, (0, 0, 0)) #creating the text
        else:
            pygame.draw.rect(win, (255, 255, 0), self.rect, 2, 7)
            text = font.render(self.mode, True, (255, 255, 255)) #creating the text
        text_rect = text.get_rect(center = self.rect.center)
        win.blit(text, text_rect)
    
    def pressed(self): #checking if the box has been clicked
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos): #checks if the mouse is over the rect
            if pygame.mouse.get_pressed()[0]: #checks if the mouse has left clicked
                self.active = not self.active
                action = True #stores if a click has happened
        font = pygame.font.SysFont("calibri", 18, bold = False)
        if objects[10].get_colour_mode() == True:
            box_colour = self.light_mode_colour
            text_colour = (0, 0, 0)
        else:
            box_colour = self.dark_mode_colour
            text_colour = (255, 255, 255)
        if self.active == True: #checks if box currently displayed
            text1 = font.render("Leave now", True, text_colour)
            pygame.draw.rect(win, box_colour, self.rect1) #displaying the box
            text_rect1 = text1.get_rect(center = self.rect1.center)
            win.blit(text1, text_rect1) #displaying the text

            text2 = font.render("Depart at", True, text_colour) #the above repeated with new text
            pygame.draw.rect(win, box_colour, self.rect2)
            text_rect2 = text2.get_rect(center = self.rect2.center)
            win.blit(text2, text_rect2)

            text3 = font.render("Arrive by", True, text_colour) #the same
            pygame.draw.rect(win, box_colour, self.rect3)
            text_rect3 = text3.get_rect(center = self.rect3.center)
            win.blit(text3, text_rect3)
        else:
            if action == True: #checking box has been clicked so not redrawing objects every time function called
                draw() #removing the drop-down menu

    def hover(self, colour):
        pos = pygame.mouse.get_pos()
        font = pygame.font.SysFont("calibri", 18, bold = False)
        if colour.get_colour_mode() == True:
            box_colour = (179, 179, 177) #setting a darker colour for the selected box in light mode
            text_colour = (0, 0, 0)
        else:
            box_colour = (140, 139, 139) #setting a lighter colour for the selected box in dark mode
            text_colour = (255, 255, 255)

        if self.active == True: #checking if the drop-down box is currently displayed
            if self.rect1.collidepoint(pos): #if the mouse is hovering over a box, redraw with the new colour
                text1 = font.render("Leave now", True, text_colour)
                pygame.draw.rect(win, box_colour, self.rect1) #displaying the box
                text_rect1 = text1.get_rect(center = self.rect1.center)
                win.blit(text1, text_rect1)
            elif self.rect2.collidepoint(pos):
                text2 = font.render("Depart at", True, text_colour)
                pygame.draw.rect(win, box_colour, self.rect2) #displaying the box
                text_rect2 = text2.get_rect(center = self.rect2.center)
                win.blit(text2, text_rect2)
            elif self.rect3.collidepoint(pos):
                text3 = font.render("Arrive by", True, text_colour)
                pygame.draw.rect(win, box_colour, self.rect3) #displaying the box
                text_rect3 = text3.get_rect(center = self.rect3.center)
                win.blit(text3, text_rect3)
    
    def option_click(self):
        pos = pygame.mouse.get_pos() #getting the mouse position
        if objects[10].get_colour_mode() == True:
            box_colour = self.light_mode_colour
        else:
            box_colour = self.dark_mode_colour
        if self.active == True:
            if self.rect1.collidepoint(pos): #checks if the mouse is over the first rect
                if pygame.mouse.get_pressed()[0]: #checks if the mouse has left clicked
                    self.mode = "Leave now" #setting the calculation mode to the input
                    self.display(box_colour) #redrawing main box - the user input will now be the text shown
                    self.active = False
                    draw() #removing the drop-down box
            elif self.rect2.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]: 
                    self.mode = "Depart at"
                    self.display(box_colour)
                    self.active = False
                    draw()
            elif self.rect3.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]: 
                    self.mode = "Arrive by"
                    self.display(box_colour)
                    self.active = False
                    draw()

class TextRectException:
    def __init__(self, message = None):
        self.message = message
    def __str__(self):
        return self.message

#functions
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

def main():
    global win

    win = pygame.display.set_mode((1250, 630))
    pygame.display.set_caption("Metrolink Journey Planner")

    list_tram_stops = ["Abraham Moss", "Altrincham", "Anchorage", "Ashton Moss", "Ashton West", "Ashton-under-Lyne", "Audenshaw", "Baguley",
                        "Barlow Moor Road", "Barton Dock Road", "Benchill", "Besses o' th' Barn", "Bowker Vale", "Broadway", "Brooklands",
                        "Burton Road", "Bury", "Cemetery Road", "Central Park", "Chorlton", "Clayton Hall", "Cornbrook", "Crossacres",
                        "Crumpsall", "Dane Road", "Deansgate-Castlefield", "Derker", "Didsbury", "Droylsden", "East Didsbury", "Eccles",
                        "Edge Lane", "Etihad Campus", "Exchange Quay", "Exchange Square", "Failsworth", "Firswood", "Freehold", "Harbour City",
                        "Heaton Park", "Hollinwood", "Holt Town", "Imperial War Museum", "Kingsway Business Park", "Ladywell", "Langworthy",
                        "Manchester Airport", "Market Street", "Martinscroft", "MediaCityUK", "Milnrow", "Monsall", "Moor Road", "Navigation Road",
                        "New Islington", "Newbold", "Newhey", "Newton Heath and Moston", "Northern Moor", "Old Trafford", "Oldham Central",
                        "Oldham King Street", "Oldham Mumps", "Parkway", "Peel Hall", "Piccadilly Gardens", "Piccadilly", "Pomona", "Prestwich",
                        "Queens Road", "Radcliffe", "Robinswood Road", "Rochdale Railway Station", "Rochdale Town Centre", "Roundthorn",
                        "Sale Water Park", "Sale", "Salford Quays", "Shadowmoss", "Shaw and Crompton", "Shudehill", "South Chadderton",
                        "St Peter's Square", "St Werburgh's Road", "Stretford", "The Trafford Centre", "Timperley", "Trafford Bar", "Velopark",
                        "Victoria", "Village", "Weaste", "West Didsbury", "Westwood", "Wharfside", "Whitefield", "Withington", "Wythenshawe Park",
                        "Wythenshawe Town Centre"]

    running = True
    instantiation()
    draw()

    while running:

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                running=False

            if event.type == pygame.KEYDOWN:
                if objects[4].get_active() == True: #checks if start stop input pressed
                    objects[4].text_input(event, objects[10].get_colour_mode(), list_tram_stops)
                if objects[6].get_active() == True: #checks if end stop input pressed
                    objects[6].text_input(event, objects[10].get_colour_mode(), list_tram_stops)


            if objects[10].change_mode() == True: #checks if the colour toggle has been pressed
                draw()
            
            objects[4].pressed(objects[4]) #checking if start input pressed
            objects[6].pressed(objects[6]) #checked if end input pressed
            objects[0].pressed() #checking if info icon pressed
            objects[9].pressed() #checking if calculation mode selection pressed
            objects[9].hover(objects[10]) #checking if any mode options hovered over
            objects[9].option_click() #checking if any mode options pressed

        pygame.display.flip()        

def instantiation(): #instantiates all the objects required
    global objects
    objects = []

    #creating all objects and appending them to a list to be displayed at once
    info = Info()
    objects.append(info)
    heading = Text("Metrolink Journey Planner", 60, True, (0, 0, 0), (255, 255, 255), (7, 7))
    objects.append(heading)
    results_section = Results()
    objects.append(results_section)
    start_stop_text = Text("Start Stop", 35, False, (0, 0, 0), (255, 255, 255), (7, 80))
    objects.append(start_stop_text)
    start_stop_input = Stop_Input(153, 80)
    objects.append(start_stop_input)
    end_stop_text = Text("End Stop", 35, False, (0, 0, 0), (255, 255, 255), (330, 80))
    objects.append(end_stop_text)
    end_stop_input = Stop_Input(460, 80)
    objects.append(end_stop_input)
    login_button = Login()
    objects.append(login_button)
    create_account = Create_Account()
    objects.append(create_account)
    mode_selector = Leaving_Time()
    objects.append(mode_selector)
    colour_switch = Colour_Toggle(900, 17)
    objects.append(colour_switch)


def draw():
    light_or_dark = objects[10].get_colour_mode()
    if light_or_dark == True:
        win.fill((255, 244, 135))
        for i in objects:
            try:
                i.display(i.get_light_mode_colour())
            except:
                i.display()
    else:
        win.fill((28, 28, 27))
        for i in objects:
            try:
                i.display(i.get_dark_mode_colour())
            except:
                i.display()
    

main()