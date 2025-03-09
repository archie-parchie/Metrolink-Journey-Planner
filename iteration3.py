#modules
import pygame, string, requests, time, datetime, json

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
    
    def set_mode(self, inp):
        self.mode = inp

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
        else:
            header = Text("Search Results", 47, True, (0, 0, 0), (255, 255, 255), (957,7))
            header.display(text_colour) #displays default title text
        
class Tram_Stop(): #creates and holds information about tram stops
    def __init__(self, name, stop_lines, neighbours, parking, lift, transport_links, zones):
        self.name = name #str
        self.stop_lines = stop_lines #list of line names (strings)
        self.neighbours = neighbours #dict
        self.parking = parking #int
        self.lift  = lift #str
        self.transport_links = transport_links #list
        #self.x_pos = x_pos #int
        #self.y_pos = y_pos #int
        self.light_mode_colour = (204, 205, 207)
        self.light_mode_text_colour = (0, 0, 0)
        self.dark_mode_colour = (102, 105, 110)
        self.dark_mode_text_colour = (255, 255, 255)
        self.zones = zones #list of strings e.g ["Zone 1", "Zone 2"]

    def get_name(self):
        return self.name
    
    def get_lines(self):
        return self.stop_lines
    
    def get_neighbours(self):
        return self.neighbours
    
    def get_parking(self):
        return self.parking
    
    def get_transport_links(self):
        return self.transport_links
    
    def get_zones(self):
        return self.zones
    
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
                self.active = not self.active
                objects[11].set_active(False) #removing current calculation message
                draw() #redraws objects to cover potential error message
                action = True
            if self.active == True and action == True: #executing code only if a click to active has just occured
                self.inputted_text = "" #resetting initial conditions
                self.on_screen = ""
                self.stored_stop = ""
                if objects[10].get_colour_mode() == True:
                    self.display((196, 196, 192)) #changing colour of the box to indicate active to user
                else:
                    self.display((140, 139, 139))
                if obj == objects[4]: #checking if the start or stop input is currently being operated on
                    if objects[6].get_active() == True:
                        objects[6].set_active()
                        draw()
                else:
                    if objects[4].get_active() == True:
                        objects[4].set_active()
                        draw()
                if objects[13].get_time_active() == True:
                    objects[13].set_time_active()
                    draw()
                if objects[12].get_active() == True:
                    objects[12].set_active()
                    draw()
                if objects[13].get_age_active() == True:
                    objects[13].set_age_active()
                    draw()
            elif self.active == False and action == True:
                self.inputted_text = "" #resetting initial conditions
                self.on_screen = ""
                self.stored_stop = ""
                draw()
                
    def text_input(self, event, colour_mode): #takes in text input and displays it in the input box
        if event.key == pygame.K_BACKSPACE:
            self.inputted_text = self.inputted_text[:-1] #keeps all but the last letter inputted
            self.on_screen = self.on_screen[:-1]
        elif event.key == pygame.K_RETURN: #considering the text input as a whole once enter has been pressed
            correct_input = False
            self.active = False
            translator = str.maketrans('', '', string.punctuation) #removes punctuation
            for i in tram_stops: #checks if the inputted text matches a tram stop
                checking = i.get_name().replace(" ", "") #cleaning the tram stop name
                checking = checking.lower()
                checking = checking.translate(translator)
                to_check = self.inputted_text.replace(" ", "") #cleaning the user input
                to_check = to_check.lower()
                to_check = to_check.translate(translator)
                if checking == to_check:
                    self.stored_stop = i
                    correct_input = True
                    self.on_screen = i.get_name()
            if correct_input == False: #displaying a message if a tram stop is not inputted
                self.inputted_text = ""
                self.on_screen = ""
                if objects[10].get_colour_mode() == True:
                    text_colour = (0, 0, 0)
                else:
                    text_colour = (255, 255, 255)
                incorrect_message = pygame.font.SysFont("calibri", 15, bold = False)
                incorrect_text = incorrect_message.render("Invalid Input! Please try again.", True, text_colour)
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
    def __init__(self, name, stops, light_mode_colour, dark_mode_colour):
        self.name = name #str
        self.stops = stops #list of tram stop names
        self.light_mode_colour = light_mode_colour #tuple of RGB values
        self.dark_mode_colour = dark_mode_colour
    
    def get_name(self):
        return self.name
    
    def get_stops(self):
        return self.stops
    
    def get_light_mode_colour(self):
        return self.light_mode_colour
    
    def get_dark_mode_colour(self):
        return self.dark_mode_colour

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
                     

    def display(self):
        if objects[10].get_colour_mode() == True:
            colour = self.light_mode_colour
        else:
            colour = self.dark_mode_colour
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
        self.time_box = False
        self.time_input = ""
    
    def get_light_mode_colour(self):
        return self.light_mode_colour
    
    def get_dark_mode_colour(self):
        return self.dark_mode_colour
    
    def get_time_box(self):
        return self.time_box
    
    def get_mode(self):
        return self.mode
    
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
        
        if self.active == True: #keeping the drop down box displayed if True and draw() is called elsewhere
            if objects[10].get_colour_mode() == True:
                box_colour = self.light_mode_colour
                text_colour = (0, 0, 0)
            else:
                box_colour = self.dark_mode_colour
                text_colour = (255, 255, 255) #checks if box currently needs to be displayed
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
        if self.active == True: #checks if box currently needs to be displayed
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
                    self.time_box = False #no user time input required
                    objects[11].set_stored_trams([])
                    objects[2].set_mode("default")
                    draw() #removing the drop-down box
            elif self.rect2.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]: 
                    self.mode = "Depart at"
                    self.display(box_colour)
                    self.active = False
                    self.time_box = True #user time input required
                    objects[11].set_stored_trams([])
                    objects[2].set_mode("default")
                    draw()
            elif self.rect3.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]: 
                    self.mode = "Arrive by"
                    self.display(box_colour)
                    self.active = False
                    self.time_box = True #user time input required
                    objects[11].set_stored_trams([])
                    objects[2].set_mode("default")
                    draw()

class Time_Box():
    def __init__(self):
        self.x_pos = 648
        self.y_pos = 130
        self.width = 70
        self.height = 30
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.light_mode_colour = (219, 219, 213)
        self.dark_mode_colour = (107, 107, 107)
        self.active = False
        self.inputted_text = "" 
        self.on_screen = ""
        self.stored_time = ""

    def get_active(self):
        return self.active
    
    def get_stored_time(self):
        return self.stored_time
    
    def set_active(self):
        self.active = not self.active

    def display(self):
        if objects[9].get_time_box() == True: #only displays if depart at or arrive by
            if objects[10].get_colour_mode() == True:
                if self.active == True:
                    box_colour = (196, 196, 192)
                else:
                    box_colour = self.light_mode_colour
                text_colour = (0, 0, 0)
            else:
                if self.active == True:
                    box_colour = (140, 139, 139)
                else:
                    box_colour = self.dark_mode_colour
                text_colour = (255, 255, 255)
            font = pygame.font.SysFont("calibri", 18, bold = False)
            if self.on_screen == "" and self.active == False: #if no time currently stored
                text = font.render("hh:mm", True, text_colour) #indicating the format of the time to the user
                pygame.draw.rect(win, box_colour, self.rect, 0, 7) #displaying the box
                text_rect = text.get_rect(center = self.rect.center)
                win.blit(text, text_rect) #displaying the text
            else:
                pygame.draw.rect(win, box_colour, self.rect, 0, 7)
                if self.stored_time != "":
                    text = font.render(self.on_screen, True, text_colour) #diplaying the inputted time
                    pygame.draw.rect(win, box_colour, self.rect, 0, 7) #displaying the box
                    win.blit(text, (self.rect.x+13, self.rect.y+6)) #displaying the text
            

    def pressed(self): #checks if the box has been pressed
        pos = pygame.mouse.get_pos()
        action = False
        if self.rect.collidepoint(pos): #checks if the mouse is over the rect
            if pygame.mouse.get_pressed()[0]: #checks if a left click has occured
                self.active = not self.active
                objects[11].set_active(False) #removing current calculation message
                draw() #redraws objects to cover potential error message
                action = True
            if action == True: #executing code only if a click to active has just occured
                self.inputted_text = "" #resetting initial conditions
                self.on_screen = ""
                self.stored_time = ""
                objects[2].set_mode("default")
                objects[11].set_stored_trams([])
                draw()
                if self.active == True:
                    if objects[4].get_active() == True:
                        objects[4].set_active()
                        draw()
                    if objects[6].get_active() == True:
                        objects[6].set_active()
                        draw()
                    if objects[13].get_time_active() == True:
                        objects[13].set_time_active()
                        draw()
                    if objects[13].get_age_active() == True:
                        objects[13].set_age_active()
                        draw()

    def text_input(self, event, colour_mode): #takes in text input and displays it in the input box
        if colour_mode == True: #displaying the text in light mode
            text_colour = (0, 0, 0)
        else: #displaying the text in dark mode
            text_colour = (255, 255, 255)
        if event.key == pygame.K_BACKSPACE:
            self.inputted_text = self.inputted_text[:-1] #keeps all but the last letter inputted
            self.on_screen = self.on_screen[:-1]
        elif event.key == pygame.K_RETURN: #considering the text input as a whole once enter has been pressed
            correct_input = True
            self.active = False
            to_check = self.inputted_text.replace(" ", "") #cleaning the user input
            to_check = to_check.lower()
            try:
                if int(to_check[0:2]) > 23 or int(to_check[0:2]) < 0: #if invalid hour
                    correct_input = False
                elif to_check[2] != ":": #if no colon separating the hours and minutes
                    correct_input = False
                elif int(to_check[3:]) > 59 or int(to_check[3:]) < 0:
                    correct_input = False
            except: #for when conversion to integers fails
                correct_input = False
            if correct_input == False: #displaying a message if a valid time is not inputted
                self.inputted_text = ""
                self.on_screen = ""
                incorrect_message = pygame.font.SysFont("calibri", 15, bold = False)
                incorrect_text = incorrect_message.render("Invalid Input! Please try again.", True, text_colour)
                win.blit(incorrect_text, (self.x_pos, self.y_pos + 45))
            else:
                self.stored_time = to_check
                self.display()
 
        else:
            self.inputted_text += event.unicode #concatenates the last letter inputted to the string
            self.on_screen += event.unicode

        font = pygame.font.SysFont("calibri", 18, bold = False)
        display_text = font.render(self.on_screen, True, (text_colour))

        while self.rect.w - 4 < display_text.get_width() + 13: #scrolls along the text if there's too much to display
            self.on_screen = self.on_screen[1:]
            display_text = font.render(self.on_screen, True, (text_colour))

        self.display() #redraws the box to cover up previously typed letters
        if self.stored_time == "": #avoids drawing a correct input twice
            win.blit(display_text, (self.rect.x+13, self.rect.y+6))            


class Calculate():
    def __init__(self):
        self.x_pos = 756
        self.y_pos = 80
        self.width = 77
        self.height = 40
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.light_mode_colour = (219, 219, 213)
        self.dark_mode_colour = (107, 107, 107)
        self.active = False
        self.stored_route = [] #list of stops on a route
        self.stored_trams = [] #list of trams needed to be taken to complete a route
    
    def get_stored_route(self):
        return self.stored_route
    
    def get_stored_trams(self):
        return self.stored_trams
    
    def set_active(self, new):
        self.active = new
    
    def set_stored_trams(self, new):
        self.stored_trams = new

    def pressed(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos): #checks if the mouse is over the rect
            if pygame.mouse.get_pressed()[0]: #checks if the mouse has left clicked
                self.active = not self.active
                action = True
        if action == True: #checks if button has been pressed
            if objects[10].get_colour_mode() == True: #checking for light mode
                text_colour = (0, 0, 0)
            else:
                text_colour = (255, 255, 255)
            if self.active == True: #checks if a message needs to be shown
                successful = True
                if objects[9].get_mode() != "Leave now":
                    if objects[4].get_stored_stop() == "" or objects[6].get_stored_stop() == "" or objects[12].get_stored_time() == "":
                        font = pygame.font.SysFont("calibri", 20, bold = False)
                        no_stops1 = font.render("Please enter a start", True, text_colour)
                        no_stops2 = font.render("and end stop/time.", True, text_colour) #message split across two lines
                        win.blit(no_stops1, (self.x_pos, self.y_pos + 50))
                        win.blit(no_stops2, (self.x_pos, self.y_pos + 68))
                        successful = False
                elif objects[9].get_mode() == "Leave now":
                    if objects[4].get_stored_stop() == "" or objects[6].get_stored_stop() == "":
                        font = pygame.font.SysFont("calibri", 20, bold = False)
                        no_stops1 = font.render("Please enter a start", True, text_colour)
                        no_stops2 = font.render("and end stop.", True, text_colour) #message split across two lines
                        win.blit(no_stops1, (self.x_pos, self.y_pos + 50))
                        win.blit(no_stops2, (self.x_pos, self.y_pos + 68))
                        successful = False
                if successful == True:
                    font = pygame.font.SysFont("calibri", 20, bold = False)
                    success = font.render("Calculating...", True, text_colour)
                    win.blit(success, (self.x_pos, self.y_pos + 50))
                    objects[2].set_mode("False") #removing initial text
                    route, distance = shortest_route(objects[4].get_stored_stop(), objects[6].get_stored_stop())
                    print([i.get_name() for i in route], distance)
                    self.stored_route = route
                    changes = line_changes(route)
                    print(changes)
                    try:
                        wait_route, tram_wait = final_time(changes)
                        self.stored_trams = wait_route
                        print(wait_route)
                        print("Total time is", tram_wait+distance)
                        objects[13].set_time(wait_route[0][-1])
                        objects[13].set_zones(find_zones(route))
                    except:
                        self.stored_trams = ""
                        print("There is currently a major delay on the network, or works are taking place. Please check tfgm.com for more details")
                    draw()
            else:
                draw() #removing the message when clicked again

    def display(self):
        if objects[10].get_colour_mode() == True: #checking current colour mode
            box_colour = self.light_mode_colour
            border_colour = (0, 0, 0)
            text_colour = (0, 0, 0)
        else:
            box_colour = self.dark_mode_colour
            border_colour = (255, 255, 0)
            text_colour = (255, 255, 255)
        font = pygame.font.SysFont("calibri", 18, bold = False)
        pygame.draw.rect(win, box_colour, self.rect, 0, 7) #drawing the button
        pygame.draw.rect(win, border_colour, self.rect, 2, 7) #drawing the outline
        text = font.render("Calculate", True, text_colour)
        text_rect = text.get_rect(center = self.rect.center)
        win.blit(text, text_rect) #displaying text

        if self.active == True:
            if objects[10].get_colour_mode() == True:
                text_colour = (0, 0, 0)
            else:
                text_colour = (255, 255, 255)
            if objects[4].get_stored_stop() == "" or objects[6].get_stored_stop() == "":
                font = pygame.font.SysFont("calibri", 20, bold = False)
                no_stops1 = font.render("Please enter a start", True, text_colour)
                no_stops2 = font.render("and end stop.", True, text_colour)
                win.blit(no_stops1, (self.x_pos, self.y_pos + 50))
                win.blit(no_stops2, (self.x_pos, self.y_pos + 65))
            else:
                font = pygame.font.SysFont("calibri", 20, bold = False)
                success = font.render("Calculating...", True, text_colour)
                win.blit(success, (self.x_pos, self.y_pos + 50))
                objects[2].set_mode("False") #removing initial text

class Prices:
    def __init__(self):
        self.rect = pygame.Rect(955, 444, 290, 171) #main calculator rect object
        self.inputted_time = "" #pre validation user inputted time
        self.time_on_screen = "" #the text to be shown on screen
        self.stored_time = "" #post validation stored time
        self.time_active = False #whether the box has just been clicked
        self.time_rect = pygame.Rect(1180, 482, 60, 30) #the time input box rect object
        self.stored_zones = "" #currently chosen option from the drop down menu
        self.zones_active = False
        self.zones_rect = pygame.Rect(1012, 482, 85, 30)
        self.inputted_age = "" #pre validation age
        self.age_on_screen = ""
        self.stored_age = "" #post validation stored age
        self.age_active = False
        self.age_rect = pygame.Rect(1012, 530, 50, 30)
        self.stored_duration = "" #currently chosen option from the drop down menu
        self.duration_active = False
        self.duration_rect = pygame.Rect(1173, 530, 67, 30)
        self.stored_price = "" #last calculated price
        self.price_rect = pygame.Rect(1012, 578, 70, 30)

    def get_time_active(self):
        return self.time_active

    def get_age_active(self):
        return self.age_active
    
    def set_age_active(self):
        self.age_active = not self.age_active

    def set_time_active(self):
        self.time_active = not self.time_active

    def set_zones(self, found_zones):
        self.stored_zones = found_zones
    
    def set_time(self, time):
        self.stored_time = time

    def display(self):
        if objects[10].get_colour_mode() == True: #setting the colours for the box and its buttons
            bg_colour = (255, 244, 135)
            text_colour = (0, 0, 0)
            box_colour = (219, 219, 213)
            active_box_colour = (196, 196, 192)
            outline = (0, 0, 0)
        else:
            bg_colour = (28, 28, 27)
            text_colour = (255, 255, 255)
            box_colour = (107, 107, 107)
            active_box_colour = (140, 139, 139)
            outline = (255, 255, 0)
        pygame.draw.rect(win, bg_colour, self.rect, 0, 7) #displaying the box
        pygame.draw.rect(win, outline, self.rect, 2, 7) #displaying the outline

        font1 = pygame.font.SysFont("calibri", 20, bold = False) #creating and displaying all the text
        text1 = font1.render("Zones", True, text_colour)
        win.blit(text1, (962, 487))
        font2 = pygame.font.SysFont("calibri", 20, bold = False)
        text2 = font2.render("Depart at", True, text_colour)
        win.blit(text2, (1101, 487))
        font3 = pygame.font.SysFont("calibri", 20, bold = False)
        text3 = font3.render("Age", True, text_colour)
        win.blit(text3, (962, 535))
        font4 = pygame.font.SysFont("calibri", 20, bold = False)
        text4 = font4.render("Duration", True, text_colour)
        win.blit(text4, (1101, 535))
        font5 = pygame.font.SysFont("calibri", 20, bold = False)
        text5 = font5.render("Price", True, text_colour)
        win.blit(text5, (962, 583))
        font6 = pygame.font.SysFont("calibri", 30, bold = True)
        text6 = font6.render("Ticket Price Calculator", True, text_colour)
        win.blit(text6, (962, 448))

        pygame.draw.rect(win, box_colour, self.zones_rect, 0, 7) #creating and displaying the buttons
        pygame.draw.rect(win, outline, self.zones_rect, 2, 7)
        if self.time_active == True:
            pygame.draw.rect(win, active_box_colour, self.time_rect, 0, 7)
        else:
            pygame.draw.rect(win, box_colour, self.time_rect, 0, 7)
        pygame.draw.rect(win, outline, self.time_rect, 2, 7)
        if self.age_active == True:
            pygame.draw.rect(win, active_box_colour, self.age_rect, 0, 7)
        else:
            pygame.draw.rect(win, box_colour, self.age_rect, 0, 7)
        pygame.draw.rect(win, outline, self.age_rect, 2, 7)
        pygame.draw.rect(win, box_colour, self.duration_rect, 0, 7)
        pygame.draw.rect(win, outline, self.duration_rect, 2, 7)
        pygame.draw.rect(win, box_colour, self.price_rect)

        if self.stored_time != "":
            font7 = pygame.font.SysFont("calibri", 20, bold = False)
            text7 = font7.render(self.stored_time, True, text_colour)
            text_rect = text7.get_rect(center = self.time_rect.center)
            win.blit(text7, text_rect)
        elif self.stored_time == "" and self.time_active == False:
            font7 = pygame.font.SysFont("calibri", 18, bold = False)
            text7 = font7.render("hh:mm", True, text_colour)
            text_rect = text7.get_rect(center = self.time_rect.center)
            win.blit(text7, text_rect)
        if self.stored_zones != "":
            font8 = pygame.font.SysFont("calibri", 20, bold = False)
            text8 = font8.render(self.stored_zones, True, text_colour)
            text_rect = text8.get_rect(center = self.zones_rect.center)
            win.blit(text8, text_rect)
        if self.stored_age != "":
            font9 = pygame.font.SysFont("calibri", 20, bold = False)
            text9 = font9.render(self.stored_age, True, text_colour)
            text_rect = text9.get_rect(center = self.age_rect.center)
            win.blit(text9, text_rect)
        if self.stored_duration != "":
            font10 = pygame.font.SysFont("calibri", 20, bold = False)
            text10 = font10.render(self.stored_duration, True, text_colour)
            text_rect = text8.get_rect(center = self.duration_rect.center)
            win.blit(text10, text_rect)
    
          
        
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

def find_zones(route):
    zones = []
    if len(route[0].get_zones()) == 1: #appending the zone for the first stop
        zones.append(int(route[0].get_zones()[0][-1]))
    else:
        next_zone = route[1].get_zones()[0]
        for j in route[0].get_zones():
            if j == next_zone:
                zones.append(int(j[-1])) #only appending the zone shared with the next stop
    for i in range(1, len(route)):
        current_zones = route[i].get_zones()
        if len(current_zones) == 1:
            if int(current_zones[0][-1]) not in zones:
                zones.append(int(current_zones[0][-1])) #if a zone is passed through that hasn't been yet, append
    if 1 in zones and 2 in zones and 3 in zones and 4 in zones:
        return "1+2+3+4"
    elif 1 in zones and 2 in zones and 3 in zones:
        return "1+2+3"
    elif 2 in zones and 3 in zones and 4 in zones:
        return "2+3+4"
    elif 1 in zones and 2 in zones:
        return "1+2"
    elif 2 in zones and 3 in zones:
        return "2+3"
    elif 3 in zones and 4 in zones:
        return "3+4"
    elif 1 in zones:
        return "1"
    elif 2 in zones:
        return "2"
    elif 3 in zones:
        return "3"
    else:
        return "4"

def shortest_route(start_stop, end_stop):
    if objects[9].get_mode() != "Leave now":
        current_time = [0, 0, 0, int(objects[12].get_stored_time()[0:2]), int(objects[12].get_stored_time()[3:])]
        reset_lines(current_time, datetime.datetime.today().weekday())
    else:   
        reset_lines(time.localtime(), datetime.datetime.today().weekday())
    priority_queue = [[start_stop, 0, start_stop]] #stops not in visited but do have a distance stored
    visited = [] #stops that have been visited
    while len(priority_queue) != 0: #repeat until all stops visisted
        current_node = priority_queue[0] #visit node with the current shortest distance
        neighbours = current_node[0].get_neighbours()
        for neighbour in neighbours: #visiting all the neighbours of the current tram stop
            obj_neighbour = find_object(neighbour)
            if check_list(visited, obj_neighbour) == True: #checks if the neighbour is already in visited
                pass
            elif check_list(priority_queue, obj_neighbour) == True: #checks if the neighbour is in the priority queue
                distance = neighbours[neighbour] + current_node[1] #adding the weight to the already existing distance
                neighbour_index = find_in_list(priority_queue, obj_neighbour) #finds the index of the neighbour in the priority queue
                if distance < priority_queue[neighbour_index][1]:
                    priority_queue[neighbour_index][1] = distance #updates the distance if this route is shorter
            else:
                distance = neighbours[neighbour] + current_node[1]
                priority_queue.append([obj_neighbour, distance, current_node[0]]) #adding the neighbour to the priority queue
        visited.append(current_node) #once all neighbours have been checked, the current node is fully visited 
        priority_queue.pop(0) #removing the current node from the priority queue
        priority_queue.sort(key = current_distance) #sorting the priority queue by shortest current distance
    route_stops = [end_stop] #creating the list of stops on the shortest route, starting with the last stop
    while route_stops[-1] != start_stop: #repeat until starting node reached
        previous_node = route_stops[-1]
        next_node = visited[find_in_list(visited, previous_node)][2] #finding the previous stop visited
        route_stops.append(next_node)
    route_stops.reverse() #switching from last to first stop to first to last
    total_distance = visited[find_in_list(visited, end_stop)][1] #finding the distance to the last stop
    return route_stops, total_distance

def line_changes(stops_list):
    lines_taken = [] #holds possible routes when taking different starting lines from the startstop
    start_lines = stops_list[0].get_lines()
    for line in start_lines: #finds a route for every possible line taken from the start stop
        taken_lines = [] #holds the lines taken on a route given a starting line
        current_line = find_line_object(line) #getting the object of the line name
        line_start = stops_list[0] #holds from which stop a line should be taken
        until_end = False
        for stop in range(0, len(stops_list)-1):
            if until_end == True: #breaks the loop if multiple lines are available until the end stop
                taken_lines.append([line_start.get_name(), stops_list[-1].get_name(), [i.get_name() for i in current_line]])
                break
            elif stops_list[stop+1].get_name() not in current_line.get_stops():
                next_lines = search_lines(stops_list[stop], stops_list[stop+1]) #finding all the lines the stops share
                offset = 1 #moving along the list of stops
                while len(next_lines) > 1 and stop+offset+1 < len(stops_list): #possible next lines narrowed down until only 1 remains
                    possible_lines = search_lines(stops_list[stop+offset], stops_list[stop+offset+1])
                    new_lines_list = []
                    for i in range(len(possible_lines)):
                        if possible_lines[i] in next_lines:
                            new_lines_list.append(possible_lines[i]) #only keeps lines that have all the stops from 'stop' to the furthest offsetted stop
                    next_lines = new_lines_list
                    offset += 1
                if len(next_lines) == 0: #accounts for the exchange square-victoria line switch
                    taken_lines.append([line_start.get_name(), stops_list[stop].get_name(), current_line.get_name()])
                    next_lines = search_lines(stops_list[stop+1], stops_list[stop+2])
                elif len(next_lines) > 1 and stop+offset+1 == len(stops_list): #accounts for if the final stop is reached but there are still multiple possible lines remaining
                    taken_lines.append([line_start.get_name(), stops_list[stop].get_name(), current_line.get_name()])
                    current_line = next_lines
                    until_end = True
                else:
                    taken_lines.append([line_start.get_name(), stops_list[stop].get_name(), current_line.get_name()])
                line_start = stops_list[stop]
                if not until_end:
                    current_line = next_lines[0]
            if stop == len(stops_list)-2: #storing the line taken to the last stop if not already stored
                if type(current_line) == Line:
                    taken_lines.append([line_start.get_name(), stops_list[-1].get_name(), current_line.get_name()])
                else:
                    taken_lines.append([line_start.get_name(), stops_list[-1].get_name(), [i.get_name() for i in current_line]])
        lines_taken.append(taken_lines)
    return lines_taken

def search_lines(stop1, stop2): #finds lines which visit two adjacent stops
    shared_lines = []
    for i in lines:
        if stop1.get_name() in i.get_stops() and stop2.get_name() in i.get_stops():
            shared_lines.append(i)
    return shared_lines

def current_distance(list): #returns the current distance to a stop - used to sort the priority queue
    return list[1]

def check_list(list, stop): #checks if a stop is in priority queue/visited
    in_list = False
    for i in list:
        if i[0] == stop:
            in_list = True
    return in_list

def find_in_list(list, stop): #finds a sublist in priorty queue/visited
    for i in range(len(list)):
        if list[i][0].get_name() == stop.get_name():
            return i

def find_object(stop_name): #finds the Tram_Stop object corresponding to a stop name
    for i in tram_stops:
        if i.get_name() == stop_name:
            return i

def find_line_object(line_name): #finds the Line object corresponding to a line name
    for i in lines:
        if i.get_name() == line_name:
            return i

def final_time(changes):
    if objects[9].get_mode() == "Leave now":
        current_data = get_pids()
        lengths = [len(i) for i in changes]
        min_length = min(lengths) #finding lowest number of changes
        to_check = []
        for i in changes:
            if len(i) == min_length:
                to_check.append(i)
        lowest_waiting = 10000 #arbritrarily large starting value
        lowest_journey = []
        if min_length == 1:
            for i in to_check: #for every route with no changes
                found = True #avoiding empty lists and 0 wait times when pid not found
                waiting_time = 0 #total time spent waiting
                waiting = [] #contains sublists containing stop, wait, and tram destination
                try:
                    pid, ind = find_pid(i[0], current_data)
                    if type(pid) == dict: #if pid successfully found
                        now = time.localtime()
                        hour = now[3]
                        mins = now[4]
                        ind = ind[-1]
                        if int(pid["Wait"+ind]) + mins < 60:
                            mins += int(pid["Wait"+ind])
                        else:
                            hour = hour + ((mins + int(pid["Wait"+ind]))//60)
                            mins = (mins + int(pid["Wait"+ind]))%60
                        if mins < 10:
                            mins = "0"+str(mins)
                        waiting_time += int(pid["Wait"+ind])
                        waiting.append([i[0][0], pid["Dest"+ind], int(pid["Wait"+ind]), i[0][2], str(hour)+":"+str(mins)])
                except:
                        found = False
                if waiting_time < lowest_waiting and found == True: 
                    lowest_waiting = waiting_time
                    lowest_journey = waiting
        else:
            lowest_waiting = 10000 #arbritrarily large starting value
            lowest_journey = []
            initial_time = time.localtime()
            hour = initial_time[3]
            mins = initial_time[4]
            for i in to_check: #for each route with at least one change
                found = True #avoiding empty lists and 0 wait times when pid not found
                waiting_time = 0 #total time spent waiting
                waiting = [] #contains sublists containing stop, wait, and tram destination
                try: #using live data for the first tram
                    pid, ind = find_pid(i[0], current_data)
                    if type(pid) == dict: #if pid successfully found
                        now = time.localtime()
                        hour2 = now[3]
                        mins2 = now[4]
                        ind = ind[-1]
                        if int(pid["Wait"+ind]) + mins2 < 60:
                            mins2 += int(pid["Wait"+ind])
                        else:
                            hour2 = hour2 + ((mins2 + int(pid["Wait"+ind]))//60)
                            mins2 = (mins2 + int(pid["Wait"+ind]))%60
                        if mins2 < 10:
                            mins2 = "0"+str(mins2)
                        waiting_time += int(pid["Wait"+ind])
                        waiting.append([i[0][0], pid["Dest"+ind], int(pid["Wait"+ind]), i[0][2], str(hour2)+":"+str(mins2)])
                except:
                    found = False
                route_covered = 0
                for j in range(1, len(i)): #looping through all but the first tram to take
                    stops, route_time = shortest_route(find_object(i[j-1][0]), find_object(i[j][0])) #finding the Tram_Stop objects then the time between them
                    route_covered += route_time
                    if waiting_time + mins + route_covered < 60: #setting the current time to pass to the find_next_tram function
                        new_mins = waiting_time + mins + route_covered
                        if new_mins < 10:
                            to_convert = str(hour) + ":" + "0" + str(new_mins)
                        else:    
                            to_convert = str(hour) + ":" + str(new_mins)
                    else:
                        new_hour = hour + ((waiting_time + mins + route_covered)//60)
                        new_mins = (waiting_time + mins + route_covered)%60
                        if new_mins < 10:
                            to_convert = str(new_hour) + ":" + "0" + str(new_mins)
                        else:    
                            to_convert = str(new_hour) + ":" + str(new_mins)
                    print(to_convert)
                    current_time = datetime.datetime.strptime(to_convert,'%H:%M') #the time after waiting for and taking the first tram
                    if type(i[j][2]) == str:
                        try:
                            wait, dest, tram_time = find_next_tram(current_time, i[j])
                            waiting_time += wait
                            tram_time = tram_time.strftime("%H:%M")
                            waiting.append([i[j][0], dest, wait, i[j][2], tram_time])
                        except:
                            found = False
                    else: #if a list of lines need to be checked
                        lowest_waiting2 = 10000 #arbritrarily large starting value
                        lowest_journey2 = []
                        for k in i[j][2]: #looping through the possible lines for this section of the route
                            found2 = True
                            waiting_time2 = 0
                            waiting2 = []
                            try:
                                wait, dest, tram_time = find_next_tram(current_time, [i[j][0], i[j][1], k]) #finding the next tram on that line
                                waiting_time2 += wait
                                tram_time = tram_time.strftime("%H:%M")
                                waiting2.append([i[j][0], dest, wait, k, tram_time])
                            except:
                                found2 = False
                            if waiting_time2 < lowest_waiting2 and found2 == True:
                                lowest_waiting2 = waiting_time2
                                lowest_journey2 = waiting2
                        waiting_time += lowest_waiting2
                        waiting.append(lowest_journey2) #adding that section of the route back to the main route
                if waiting_time < lowest_waiting and found == True: #if the route just found is currently the shortest
                    lowest_waiting = waiting_time
                    lowest_journey = waiting
    elif objects[9].get_mode() == "Depart at":
        lengths = [len(i) for i in changes]
        min_length = min(lengths) #finding lowest number of changes
        to_check = []
        for i in changes:
            if len(i) == min_length:
                to_check.append(i)
        lowest_waiting = 10000 #arbritrarily large starting value
        lowest_journey = []
        initial_time = objects[12].get_stored_time() #getting user inputted time
        hour = int(initial_time[0:2])
        mins = int(initial_time[3:])
        for i in to_check:
            found = True #avoiding empty lists and 0 wait times when pid not found
            waiting_time = 0 #total time spent waiting
            waiting = [] #contains sublists containing stop, wait, and tram destination
            route_covered = 0
            for j in range(0, len(i)):
                if j > 0:
                    stops, route_time = shortest_route(find_object(i[j-1][0]), find_object(i[j][0])) #finding the Tram_Stop objects then the time between them
                else:
                    route_time = 0
                route_covered += route_time
                if waiting_time + mins + route_covered < 60: #setting the current time to pass to the find_next_tram function
                    new_mins = waiting_time + mins + route_covered
                    to_convert = str(hour) + ":" + str(new_mins)
                else:
                    new_hour = hour + ((waiting_time + mins + route_covered)//60)
                    new_mins = (waiting_time + mins + route_covered)%60
                    to_convert = str(new_hour) + ":" + str(new_mins)
                current_time = datetime.datetime.strptime(to_convert,'%H:%M') #the time after waiting for and taking the previous trams
                if type(i[j][2]) == str:
                    try:
                        wait, dest, tram_time = find_next_tram(current_time, i[j])
                        waiting_time += wait
                        tram_time = tram_time.strftime("%H:%M")
                        waiting.append([i[j][0], dest, wait, i[j][2], tram_time])
                    except:
                        found = False
                else: #if a list of lines need to be checked
                    lowest_waiting2 = 10000 #arbritrarily large starting value
                    lowest_journey2 = []
                    for k in i[j][2]: #looping through the possible lines for this section of the route
                        found2 = True
                        waiting_time2 = 0
                        waiting2 = []
                        try:
                            wait, dest, tram_time = find_next_tram(current_time, [i[j][0], i[j][1], k]) #finding the next tram on that line
                            waiting_time2 += wait
                            tram_time = tram_time.strftime("%H:%M")
                            waiting2.append([i[j][0], dest, wait, k, tram_time])
                        except:
                            found2 = False
                        if waiting_time2 < lowest_waiting2 and found2 == True:
                            lowest_waiting2 = waiting_time2
                            lowest_journey2 = waiting2
                    waiting_time += lowest_waiting2
                    waiting.append(lowest_journey2) #adding that section of the route back to the main route
            if waiting_time < lowest_waiting and found == True: #if the route just found is currently the shortest
                lowest_waiting = waiting_time
                lowest_journey = waiting
    else:
        lengths = [len(i) for i in changes]
        min_length = min(lengths) #finding lowest number of changes
        to_check = []
        for i in changes:
            if len(i) == min_length:
                to_check.append(i)
        stops, sub = shortest_route(find_object(changes[0][0][0]), find_object(changes[-1][-1][1]))
        initial_time = objects[12].get_stored_time() #getting user inputted time
        end_time = datetime.datetime.strptime(initial_time,'%H:%M')
        length = datetime.timedelta(minutes=sub) #time the journey without changes or waiting takes
        subtraction = datetime.timedelta(minutes=sub) 
        addition = datetime.timedelta(minutes=1000) #arbritrarily large starting value, will later hold tram waiting times
        while (end_time - subtraction + addition + length) > end_time:
            lowest_waiting = 10000 #arbritrarily large starting value
            lowest_journey = []
            start_time = end_time - subtraction #setting the current starting time
            start_time = start_time.strftime("%H:%M")
            hour = int(start_time[0:2])
            mins = int(start_time[3:])
            for i in to_check:
                found = True #avoiding empty lists and 0 wait times when pid not found
                waiting_time = 0 #total time spent waiting
                waiting = [] #contains sublists containing stop, wait, and tram destination
                route_covered = 0
                for j in range(0, len(i)):
                    if j > 0:
                        stops, route_time = shortest_route(find_object(i[j-1][0]), find_object(i[j][0])) #finding the Tram_Stop objects then the time between them
                    else:
                        route_time = 0
                    route_covered += route_time
                    if waiting_time + mins + route_covered < 60: #setting the current time to pass to the find_next_tram function
                        new_mins = waiting_time + mins + route_covered
                        to_convert = str(hour) + ":" + str(new_mins)
                    else:
                        new_hour = hour + ((waiting_time + mins + route_covered)//60)
                        new_mins = (waiting_time + mins + route_covered)%60
                        to_convert = str(new_hour) + ":" + str(new_mins)
                    current_time = datetime.datetime.strptime(to_convert,'%H:%M') #the time after waiting for and taking the previous trams
                    if type(i[j][2]) == str:
                        try:
                            wait, dest, tram_time = find_next_tram(current_time, i[j])
                            waiting_time += wait
                            tram_time = tram_time.strftime("%H:%M")
                            waiting.append([i[j][0], dest, wait, i[j][2], tram_time])
                        except:
                            found = False
                    else: #if a list of lines need to be checked
                        lowest_waiting2 = 10000 #arbritrarily large starting value
                        lowest_journey2 = []
                        for k in i[j][2]: #looping through the possible lines for this section of the route
                            found2 = True
                            waiting_time2 = 0
                            waiting2 = []
                            try:
                                wait, dest, tram_time = find_next_tram(current_time, [i[j][0], i[j][1], k]) #finding the next tram on that line
                                waiting_time2 += wait
                                tram_time = tram_time.strftime("%H:%M")
                                waiting2.append([i[j][0], dest, wait, k, tram_time])
                            except:
                                found2 = False
                            if waiting_time2 < lowest_waiting2 and found2 == True:
                                lowest_waiting2 = waiting_time2
                                lowest_journey2 = waiting2
                        waiting_time += lowest_waiting2
                        waiting.append(lowest_journey2) #adding that section of the route back to the main route
                if waiting_time < lowest_waiting and found == True: #if the route just found is currently the shortest
                    lowest_waiting = waiting_time
                    lowest_journey = waiting
                    addition = datetime.timedelta(minutes=waiting_time)
            if (end_time - subtraction + addition + length) > end_time: #if arriving later than arrive by time
                sub+=1 #try starting one minute earlier
                subtraction = datetime.timedelta(minutes=sub)
    if len(lowest_journey) != min_length:
        return False
    else:
        return lowest_journey, lowest_waiting

        
def find_next_tram(time, section): #finds the next tram on the right line arriving at a stop, takes the current time and route section as inputs
    f = open("first_trams.txt", "r") #opening file
    read = f.read()
    contents = json.loads(read) #making the file into a list
    f.close()
    line = find_line_object(section[2])
    ind1 = line.get_stops().index(section[0])
    ind2 = line.get_stops().index(section[1])
    if ind1 < ind2:
        target = line.get_stops()[-1] #what the direction of the tram should be
        opposite = line.get_stops()[0] #where the tram is coming from
    else:
        target = line.get_stops()[0]
        opposite = line.get_stops()[-1] #where the tram is coming from
    day = datetime.datetime.today().weekday()
    if day == 6:
        interval = 15 #setting the time between each tram on a line
    else:
        interval = 12
    for i in contents:
        if section[2] == i[1] and opposite == i[0]:
            changeover = i
    if day < 5:
        start_time = datetime.datetime.strptime(changeover[2][0],'%H:%M')
    elif day == 5:
        start_time = datetime.datetime.strptime(changeover[2][1],'%H:%M')
    else:
        start_time = datetime.datetime.strptime(changeover[2][2],'%H:%M')
    if start_time == "": #accounts for lines that don't run on Sundays
        return False
    route, time_to_stop = shortest_route(find_object(opposite), find_object(section[0])) #time from depot stop to current stop
    time_to = datetime.timedelta(minutes=time_to_stop)
    next_tram = start_time + time_to #will hold the time of the next tram, currently holds first tram of the day arriving at that stop
    while next_tram < time:
        time_change = datetime.timedelta(minutes=interval) 
        next_tram = next_tram + time_change
    wait_time = next_tram - time
    if len(changeover) == 4: #if using a line that only runs part of the time, check that this line is currently running
        if day < 5:
            end_time = datetime.datetime.strptime(changeover[3][0],'%H:%M')
        elif day == 5:
            end_time = datetime.datetime.strptime(changeover[3][1],'%H:%M')
        else:
            end_time = datetime.datetime.strptime(changeover[3][2],'%H:%M')
        tram = next_tram - time_to #finding when the tram leaves from the depot stop
        if tram > end_time:
            return False
        else:
            int_time = wait_time.seconds//60 #returning the minutes of the timedelta object
            return int_time, target, next_tram
    else:
        int_time = wait_time.seconds//60 #returning the minutes of the timedelta object
        return int_time, target, next_tram

def find_pid(section, data):
    line = find_line_object(section[2])
    ind1 = line.get_stops().index(section[0])
    ind2 = line.get_stops().index(section[1])
    if ind1 < ind2:
        target = line.get_stops()[-1] #what the direction of the tram should be
    else:
        target = line.get_stops()[0]
    for i in data:
        if i["StationLocation"] == section[0]: #checking for if the PID is for the right station
            if target in i["Dest0"]: #checking for if any of the trams on the PID are going the right way
                tram = "Dest0"
                return i, tram
            elif target in i["Dest1"]:
                tram = "Dest1"
                return i, tram
            elif target in i["Dest2"]:
                tram = "Dest2"
                return i, tram
            elif target in i["Dest3"]:
                tram = "Dest3"
                return i, tram
    return False

def reset_lines(current_time, day): #accounts for stops that are only on lines some of the time
    #need to update harbour city and broadway
    need_updating = []
    if day <= 4:
        if current_time[3] >= 20:
            purple_line = Line("Purple Line", ["Altrincham", "Navigation Road", "Timperley", "Brooklands", "Sale", "Dane Road", "Stretford",
                                               "Old Trafford", "Trafford Bar", "Cornbrook", "Deansgate-Castlefield", "St Peter's Square",
                                               "Piccadilly Gardens", "Piccadilly", "New Islington", "Holt Town", "Etihad Campus"], (142,72,153),
                                               (217, 106, 235))
            new_islington = Tram_Stop("New Islington", ["Orange Line", "Blue Line", "Purple Line"], {"Piccadilly":3, "Holt Town":2}, 0, "Not required", ["N/A"], ["Zone 1"])
            need_updating.append(new_islington)
            holt_town = Tram_Stop("Holt Town", ["Orange Line", "Blue Line", "Purple Line"], {"Etihad Campus":1, "New Islington":2}, 0, "Not required", ["N/A"], ["Zone 2"])
            need_updating.append(holt_town)
            etihad_campus = Tram_Stop("Etihad Campus", ["Blue Line", "Orange Line", "Purple Line"], {"Holt Town":2, "Velopark":3}, 0, "Yes",["N/A"], ["Zone 2"])
            need_updating.append(etihad_campus)
        elif current_time[3] >= 19 and current_time[4] >= 53:
            purple_line = Line("Purple Line", ["Altrincham", "Navigation Road", "Timperley", "Brooklands", "Sale", "Dane Road", "Stretford",
                                               "Old Trafford", "Trafford Bar", "Cornbrook", "Deansgate-Castlefield", "St Peter's Square",
                                               "Piccadilly Gardens", "Piccadilly", "New Islington", "Holt Town", "Etihad Campus"], (142,72,153),
                                               (217, 106, 235))
            new_islington = Tram_Stop("New Islington", ["Orange Line", "Blue Line", "Purple Line"], {"Piccadilly":3, "Holt Town":2}, 0, "Not required", ["N/A"], ["Zone 1"])
            need_updating.append(new_islington)
            holt_town = Tram_Stop("Holt Town", ["Orange Line", "Blue Line", "Purple Line"], {"Etihad Campus":1, "New Islington":2}, 0, "Not required", ["N/A"], ["Zone 2"])
            need_updating.append(holt_town)
            etihad_campus = Tram_Stop("Etihad Campus", ["Blue Line", "Orange Line", "Purple Line"], {"Holt Town":2, "Velopark":3}, 0, "Yes",["N/A"], ["Zone 2"])
            need_updating.append(etihad_campus)
        else:
            purple_line = Line("Purple Line", ["Altrincham", "Navigation Road", "Timperley", "Brooklands", "Sale", "Dane Road", "Stretford",
                                               "Old Trafford", "Trafford Bar", "Cornbrook", "Deansgate-Castlefield", "St Peter's Square",
                                               "Piccadilly Gardens", "Piccadilly"], (142,72,153), (217, 106, 235))
            new_islington = Tram_Stop("New Islington", ["Orange Line", "Blue Line"], {"Piccadilly":3, "Holt Town":2}, 0, "Not required", ["N/A"], ["Zone 1"])
            need_updating.append(new_islington)
            holt_town = Tram_Stop("Holt Town", ["Orange Line", "Blue Line"], {"Etihad Campus":1, "New Islington":2}, 0, "Not required", ["N/A"], ["Zone 2"])
            need_updating.append(holt_town)
            etihad_campus = Tram_Stop("Etihad Campus", ["Blue Line", "Orange Line"], {"Holt Town":2, "Velopark":3}, 0, "Yes",["N/A"], ["Zone 2"])
            need_updating.append(etihad_campus)
        if current_time[3] < 7 or current_time[3] >= 20:
            blue_line = Line("Blue Line", ["Eccles", "Ladywell", "Weaste", "Langworthy", "Broadway", "Harbour City", "MediaCityUK", "Anchorage", "Salford Quays",
                                           "Exchange Quay", "Pomona", "Cornbrook", "Deansgate-Castlefield", "St Peter's Square",
                                           "Piccadilly Gardens", "Piccadilly", "New Islington", "Holt Town", "Etihad Campus", "Velopark",
                                           "Clayton Hall", "Edge Lane", "Cemetery Road", "Droylsden", "Audenshaw", "Ashton Moss", "Ashton West",
                                           "Ashton-under-Lyne"], (62, 108, 133), (148, 212, 247))
            mediacityuk = Tram_Stop("MediaCityUK", ["Orange Line", "Blue Line"], {"Harbour City":2, "Broadway":2}, 0, "Not required", ["N/A"], ["Zone 2"])
            need_updating.append(mediacityuk)
            harbour_city = Tram_Stop("Harbour City", ["Orange Line", "Blue Line"], {"MediaCityUK":2, "Anchorage":1}, 0, "Not Required", ["N/A"], ["Zone 2"])
            need_updating.append(harbour_city)
            broadway = Tram_Stop("Broadway", ["Blue Line"], {"Langworthy":2, "MediaCityUK":2}, 0, "Not required", ["N/A"], ["Zone 2"])
            need_updating.append(broadway)
        else:
            blue_line = Line("Blue Line", ["Eccles", "Ladywell", "Weaste", "Langworthy", "Broadway", "Harbour City", "Anchorage", "Salford Quays",
                                           "Exchange Quay", "Pomona", "Cornbrook", "Deansgate-Castlefield", "St Peter's Square",
                                           "Piccadilly Gardens", "Piccadilly", "New Islington", "Holt Town", "Etihad Campus", "Velopark",
                                           "Clayton Hall", "Edge Lane", "Cemetery Road", "Droylsden", "Audenshaw", "Ashton Moss", "Ashton West",
                                           "Ashton-under-Lyne"], (62, 108, 133), (148, 212, 247))
            mediacityuk = Tram_Stop("MediaCityUK", ["Orange Line"], {"Harbour City":2}, 0, "Not required", ["N/A"], ["Zone 2"])
            need_updating.append(mediacityuk)
            harbour_city = Tram_Stop("Harbour City", ["Orange Line", "Blue Line"], {"MediaCityUK":2, "Anchorage":1, "Broadway":2}, 0, "Not Required", ["N/A"], ["Zone 2"])
            need_updating.append(harbour_city)
            broadway = Tram_Stop("Broadway", ["Blue Line"], {"Langworthy":2, "Harbour City":2}, 0, "Not required", ["N/A"], ["Zone 2"])
            need_updating.append(broadway)
    elif day == 5:
        if current_time[3] >= 19:
            purple_line = Line("Purple Line", ["Altrincham", "Navigation Road", "Timperley", "Brooklands", "Sale", "Dane Road", "Stretford",
                                               "Old Trafford", "Trafford Bar", "Cornbrook", "Deansgate-Castlefield", "St Peter's Square",
                                               "Piccadilly Gardens", "Piccadilly", "New Islington", "Holt Town", "Etihad Campus"], (142,72,153),
                                               (217, 106, 235))
            new_islington = Tram_Stop("New Islington", ["Orange Line", "Blue Line", "Purple Line"], {"Piccadilly":3, "Holt Town":2}, 0, "Not required", ["N/A"], ["Zone 1"])
            need_updating.append(new_islington)
            holt_town = Tram_Stop("Holt Town", ["Orange Line", "Blue Line", "Purple Line"], {"Etihad Campus":1, "New Islington":2}, 0, "Not required", ["N/A"], ["Zone 2"])
            need_updating.append(holt_town)
            etihad_campus = Tram_Stop("Etihad Campus", ["Blue Line", "Orange Line", "Purple Line"], {"Holt Town":2, "Velopark":3}, 0, "Yes",["N/A"], ["Zone 2"])
            need_updating.append(etihad_campus)
        elif current_time[3] >= 18 and current_time[4] >= 24:
            purple_line = Line("Purple Line", ["Altrincham", "Navigation Road", "Timperley", "Brooklands", "Sale", "Dane Road", "Stretford",
                                               "Old Trafford", "Trafford Bar", "Cornbrook", "Deansgate-Castlefield", "St Peter's Square",
                                               "Piccadilly Gardens", "Piccadilly", "New Islington", "Holt Town", "Etihad Campus"], (142,72,153), 
                                               (217, 106, 235))
            new_islington = Tram_Stop("New Islington", ["Orange Line", "Blue Line", "Purple Line"], {"Piccadilly":3, "Holt Town":2}, 0, "Not required", ["N/A"], ["Zone 1"])
            need_updating.append(new_islington)
            holt_town = Tram_Stop("Holt Town", ["Orange Line", "Blue Line", "Purple Line"], {"Etihad Campus":1, "New Islington":2}, 0, "Not required", ["N/A"], ["Zone 2"])
            need_updating.append(holt_town)
            etihad_campus = Tram_Stop("Etihad Campus", ["Blue Line", "Orange Line", "Purple Line"], {"Holt Town":2, "Velopark":3}, 0, "Yes",["N/A"], ["Zone 2"])
            need_updating.append(etihad_campus)
        else:
            purple_line = Line("Purple Line", ["Altrincham", "Navigation Road", "Timperley", "Brooklands", "Sale", "Dane Road", "Stretford",
                                               "Old Trafford", "Trafford Bar", "Cornbrook", "Deansgate-Castlefield", "St Peter's Square",
                                               "Piccadilly Gardens", "Piccadilly"], (142,72,153), (217, 106, 235))
            new_islington = Tram_Stop("New Islington", ["Orange Line", "Blue Line"], {"Piccadilly":3, "Holt Town":2}, 0, "Not required", ["N/A"], ["Zone 1"])
            need_updating.append(new_islington)
            holt_town = Tram_Stop("Holt Town", ["Orange Line", "Blue Line"], {"Etihad Campus":1, "New Islington":2}, 0, "Not required", ["N/A"], ["Zone 2"])
            need_updating.append(holt_town)
            etihad_campus = Tram_Stop("Etihad Campus", ["Blue Line", "Orange Line"], {"Holt Town":2, "Velopark":3}, 0, "Yes",["N/A"], ["Zone 2"])
            need_updating.append(etihad_campus)
        if current_time[3] < 9 or current_time[3] >= 19:
            blue_line = Line("Blue Line", ["Eccles", "Ladywell", "Weaste", "Langworthy", "Broadway", "Harbour City", "MediaCityUK", "Anchorage", "Salford Quays",
                                           "Exchange Quay", "Pomona", "Cornbrook", "Deansgate-Castlefield", "St Peter's Square",
                                           "Piccadilly Gardens", "Piccadilly", "New Islington", "Holt Town", "Etihad Campus", "Velopark",
                                           "Clayton Hall", "Edge Lane", "Cemetery Road", "Droylsden", "Audenshaw", "Ashton Moss", "Ashton West",
                                           "Ashton-under-Lyne"], (62, 108, 133), (148, 212, 247))
            mediacityuk = Tram_Stop("MediaCityUK", ["Orange Line", "Blue Line"], {"Harbour City":2, "Broadway":2}, 0, "Not required", ["N/A"], ["Zone 2"])
            need_updating.append(mediacityuk)
            harbour_city = Tram_Stop("Harbour City", ["Orange Line", "Blue Line"], {"MediaCityUK":2, "Anchorage":1}, 0, "Not Required", ["N/A"], ["Zone 2"])
            need_updating.append(harbour_city)
            broadway = Tram_Stop("Broadway", ["Blue Line"], {"Langworthy":2, "MediaCityUK":2}, 0, "Not required", ["N/A"], ["Zone 2"])
            need_updating.append(broadway)
        elif current_time[3] >= 18 and current_time[4] > 30:
            blue_line = Line("Blue Line", ["Eccles", "Ladywell", "Weaste", "Langworthy", "Broadway", "Harbour City", "MediaCityUK", "Anchorage", "Salford Quays",
                                           "Exchange Quay", "Pomona", "Cornbrook", "Deansgate-Castlefield", "St Peter's Square",
                                           "Piccadilly Gardens", "Piccadilly", "New Islington", "Holt Town", "Etihad Campus", "Velopark",
                                           "Clayton Hall", "Edge Lane", "Cemetery Road", "Droylsden", "Audenshaw", "Ashton Moss", "Ashton West",
                                           "Ashton-under-Lyne"], (62, 108, 133), (148, 212, 247))
            mediacityuk = Tram_Stop("MediaCityUK", ["Orange Line", "Blue Line"], {"Harbour City":2, "Broadway":2}, 0, "Not required", ["N/A"], ["Zone 2"])
            need_updating.append(mediacityuk)
            harbour_city = Tram_Stop("Harbour City", ["Orange Line", "Blue Line"], {"MediaCityUK":2, "Anchorage":1}, 0, "Not Required", ["N/A"], ["Zone 2"])
            need_updating.append(harbour_city)
            broadway = Tram_Stop("Broadway", ["Blue Line"], {"Langworthy":2, "MediaCityUK":2}, 0, "Not required", ["N/A"], ["Zone 2"])
            need_updating.append(broadway)
        else:
            blue_line = Line("Blue Line", ["Eccles", "Ladywell", "Weaste", "Langworthy", "Broadway", "Harbour City", "Anchorage", "Salford Quays",
                                           "Exchange Quay", "Pomona", "Cornbrook", "Deansgate-Castlefield", "St Peter's Square",
                                           "Piccadilly Gardens", "Piccadilly", "New Islington", "Holt Town", "Etihad Campus", "Velopark",
                                           "Clayton Hall", "Edge Lane", "Cemetery Road", "Droylsden", "Audenshaw", "Ashton Moss", "Ashton West",
                                           "Ashton-under-Lyne"], (62, 108, 133), (148, 212, 247))
            mediacityuk = Tram_Stop("MediaCityUK", ["Orange Line"], {"Harbour City":2}, 0, "Not required", ["N/A"], ["Zone 2"])
            need_updating.append(mediacityuk)
            harbour_city = Tram_Stop("Harbour City", ["Orange Line", "Blue Line"], {"MediaCityUK":2, "Anchorage":1, "Broadway":2}, 0, "Not Required", ["N/A"], ["Zone 2"])
            need_updating.append(harbour_city)
            broadway = Tram_Stop("Broadway", ["Blue Line"], {"Langworthy":2, "Harbour City":2}, 0, "Not required", ["N/A"], ["Zone 2"])
            need_updating.append(broadway)
    else:
        purple_line = Line("Purple Line", ["Altrincham", "Navigation Road", "Timperley", "Brooklands", "Sale", "Dane Road", "Stretford",
                                            "Old Trafford", "Trafford Bar", "Cornbrook", "Deansgate-Castlefield", "St Peter's Square",
                                            "Piccadilly Gardens", "Piccadilly", "New Islington", "Holt Town", "Etihad Campus"], (142,72,153),
                                            (217, 106, 235))
        new_islington = Tram_Stop("New Islington", ["Orange Line", "Blue Line", "Purple Line"], {"Piccadilly":3, "Holt Town":2}, 0, "Not required", ["N/A"], ["Zone 1"])
        need_updating.append(new_islington)
        holt_town = Tram_Stop("Holt Town", ["Orange Line", "Blue Line", "Purple Line"], {"Etihad Campus":1, "New Islington":2}, 0, "Not required", ["N/A"], ["Zone 2"])
        need_updating.append(holt_town)
        etihad_campus = Tram_Stop("Etihad Campus", ["Blue Line", "Orange Line", "Purple Line"], {"Holt Town":2, "Velopark":3}, 0, "Yes",["N/A"], ["Zone 2"])
        need_updating.append(etihad_campus)
        blue_line = Line("Blue Line", ["Eccles", "Ladywell", "Weaste", "Langworthy", "Broadway", "Harbour City", "MediaCityUK", "Anchorage", "Salford Quays",
                                        "Exchange Quay", "Pomona", "Cornbrook", "Deansgate-Castlefield", "St Peter's Square",
                                        "Piccadilly Gardens", "Piccadilly", "New Islington", "Holt Town", "Etihad Campus", "Velopark",
                                        "Clayton Hall", "Edge Lane", "Cemetery Road", "Droylsden", "Audenshaw", "Ashton Moss", "Ashton West",
                                        "Ashton-under-Lyne"], (62, 108, 133), (148, 212, 247))
        mediacityuk = Tram_Stop("MediaCityUK", ["Orange Line", "Blue Line"], {"Harbour City":2, "Broadway":2}, 0, "Not required", ["N/A"], ["Zone 2"])
        need_updating.append(mediacityuk)
        harbour_city = Tram_Stop("Harbour City", ["Orange Line", "Blue Line"], {"MediaCityUK":2, "Anchorage":1}, 0, "Not Required", ["N/A"], ["Zone 2"])
        need_updating.append(harbour_city)
        broadway = Tram_Stop("Broadway", ["Blue Line"], {"Langworthy":2, "MediaCityUK":2}, 0, "Not required", ["N/A"], ["Zone 2"])
        need_updating.append(broadway)
    for i in range(0,len(lines)): #inserting the updated lines into the lines list
        if lines[i].get_name() == "Purple Line":
            lines[i] = purple_line
        elif lines[i].get_name() == "Blue Line":
            lines[i] = blue_line
    for i in need_updating: #inserting the updated tram stops into the tram_stops list
        for j in range(0, len(tram_stops)):
            if tram_stops[j].get_name() == i.get_name():
                tram_stops[j] = i

def get_pids():
    api_key = "Enter your key here"
    api_url = "https://api.tfgm.com/odata/Metrolinks"
    headers = {"Ocp-Apim-Subscription-Key" : api_key}
    response = requests.get(api_url, headers = headers)
    data = response.json()
    items = list(data.items())[1][1]
    return items

def show_results(route, trams):
    if trams == "": #displaying the error message
        if objects[10].get_colour_mode() == True: #setting box and text colours
            text_colour = (0, 0, 0)
            box_colour = (219, 219, 213)
        else:
            text_colour = (255, 255, 255)
            box_colour = (107, 107, 107)
        text = "There is currently a major delay on the network, or tram works are taking place. Please check tfgm.com for more details."
        font = pygame.font.SysFont("calibri", 19)
        rect = pygame.Rect((955, 70, 290, 77))
        rendered_text = render_textrect(text, font, rect, text_colour, box_colour) #word wrapping the text in the box
        win.blit(rendered_text, rect)
    elif trams == []:
        pass #the user is yet to enter a route
    else: #display the found route to the user
        if objects[10].get_colour_mode() == True: #setting box and text colours
            text_colour = (0, 0, 0)
            box_colour = (219, 219, 213)
        else:
            text_colour = (255, 255, 255)
            box_colour = (107, 107, 107)
        y_offset = 0 #setting how far down each box should be from the last
        for i in range(0, len(trams)):
            if type(trams[i][0]) == list:
                trams[i] = [k for k in trams[i][0]]
        for i in range(0, len(trams)):
            line1 = trams[i][0] + " " + trams[i][-1] #setting the first line of the text output - the starting stop and time
            try:
                stops, time = shortest_route(find_object(trams[i][0]), find_object(trams[i+1][0]))
            except:
                stops, time = shortest_route(find_object(trams[i][0]), route[-1])
            middle_stops = stops[1:-1]
            line2 = ""
            for j in range(0,len(middle_stops)-1): #setting the second line of the text output - all of the stops visited on that tram
                line2 = line2 + middle_stops[j].get_name() + ", "
            if len(middle_stops) > 0:
                line2 = line2 + middle_stops[-1].get_name()
            line3 = trams[i][1] + "  - " + trams[i][3] #setting the third line of the text output - the tram destination and line
            leaving = datetime.datetime.strptime(trams[i][-1],'%H:%M')
            delta = datetime.timedelta(minutes=time)
            arriving = leaving + delta
            arriving = arriving.strftime("%H:%M")
            try: #setting the fourth line of the text output - how far that tram is taken and the time the final stop is reached
                line4 = trams[i+1][0] + " " + arriving
            except:
                line4 = route[-1].get_name() + " " + arriving
            height1 = 20 #setting the heights of the rectangles that will hold the text
            height2 = 1
            height3 = 20
            height4 = 25
            rect1 = pygame.Rect((955, 70+y_offset, 290, height1))
            font1 = pygame.font.SysFont("calibri", 19)
            text1 = font1.render(line1, True, text_colour)
            pygame.draw.rect(win, box_colour, rect1)
            win.blit(text1, rect1) #displaying the first line
            font2 = pygame.font.SysFont("calibri", 15)
            size_found = False
            while size_found == False:
                rect2 = pygame.Rect((955, 70+y_offset+height1, 290, height2))
                try:
                    rendered_text = render_textrect(line2, font2, rect2, text_colour, box_colour)
                    size_found = True
                except:
                    height2 += 1 #increasing height of the rect until the stops fit
            win.blit(rendered_text, rect2) #displaying the second line
            if objects[10].get_colour_mode() == True:
                colour = find_line_object(trams[i][3]).get_light_mode_colour() #finding the colour of the line and using that colour for the font
                
            else:
                colour = find_line_object(trams[i][3]).get_dark_mode_colour()
            rect3 = pygame.Rect((955, 70+height1+height2+y_offset, 290, height3))
            font3 = pygame.font.SysFont("calibri", 19)
            text3 = font3.render(line3, True, colour)t
            pygame.draw.rect(win, box_colour, rect3)
            win.blit(text3, rect3) #displaying the third line
            rect4 = pygame.Rect((955, 70+height1+height2+height3+y_offset, 290, height4))
            font4 = pygame.font.SysFont("calibri", 19)
            text4 = font4.render(line4, True, text_colour)
            pygame.draw.rect(win, box_colour, rect4)
            win.blit(text4, rect4) #displaying the fourth line
            y_offset = y_offset + height1 + height2 + height3 + height4 + 5 #ensuring the next box is shifted below the current one


def main():
    global win
    
    win = pygame.display.set_mode((1250, 630))
    pygame.display.set_caption("Metrolink Journey Planner")

    running = True
    instantiation()
    draw()

    while running:

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running=False

            if event.type == pygame.KEYDOWN:
                if objects[4].get_active() == True: #checks if start stop input pressed
                    objects[4].text_input(event, objects[10].get_colour_mode())
                if objects[6].get_active() == True: #checks if end stop input pressed
                    objects[6].text_input(event, objects[10].get_colour_mode())
                if objects[12].get_active() == True:
                    objects[12].text_input(event, objects[10].get_colour_mode())

            if objects[10].change_mode() == True: #checks if the colour toggle has been pressed
                draw()
            
            objects[4].pressed(objects[4]) #checking if start input pressed
            objects[6].pressed(objects[6]) #checked if end input pressed
            objects[0].pressed() #checking if info icon pressed
            objects[9].pressed() #checking if calculation mode selection pressed
            objects[9].hover(objects[10]) #checking if any mode options hovered over
            objects[9].option_click() #checking if any mode options pressed
            objects[11].pressed()
            objects[12].pressed()

        pygame.display.flip()        
    pygame.quit()

def instantiation(): #instantiates all the objects required
    global objects, tram_stops, lines
    objects = [] #holds all objects that require drawing
    tram_stops = [] #holds all Tram_Stop objects
    lines = [] #holds all Line objects

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
    start_calculation = Calculate()
    objects.append(start_calculation)
    time_input = Time_Box()
    objects.append(time_input)
    price_calculation = Prices()
    objects.append(price_calculation)

    navy_line = Line("Navy Line", ["Manchester Airport", "Shadowmoss", "Peel Hall", "Robinswood Road", "Wythenshawe Town Centre",
                                    "Crossacres", "Benchill", "Martinscroft", "Roundthorn", "Baguley", "Moor Road","Wythenshawe Park",
                                    "Northern Moor", "Sale Water Park", "Barlow Moor Road", "St Werburgh's Road", "Chorlton", "Firswood",
                                    "Trafford Bar", "Cornbrook", "Deansgate-Castlefield", "St Peter's Square", "Market Street",
                                    "Shudehill", "Victoria"], (49, 97, 148), (91, 163, 240))
    lines.append(navy_line)
    purple_line = Line("Purple Line", ["Altrincham", "Navigation Road", "Timperley", "Brooklands", "Sale", "Dane Road", "Stretford",
                                       "Old Trafford", "Trafford Bar", "Cornbrook", "Deansgate-Castlefield", "St Peter's Square",
                                       "Piccadilly Gardens", "Piccadilly"], (142,72,153), (217, 106, 235))
    lines.append(purple_line)
    green_line = Line("Green Line", ["Altrincham", "Navigation Road", "Timperley", "Brooklands", "Sale", "Dane Road", "Stretford",
                                     "Old Trafford", "Trafford Bar", "Cornbrook", "Deansgate-Castlefield", "St Peter's Square",
                                     "Market Street", "Shudehill", "Victoria", "Queens Road", "Abraham Moss", "Crumpsall", "Bowker Vale",
                                     "Heaton Park", "Prestwich", "Besses o' th' Barn", "Whitefield", "Radcliffe", "Bury"], (75, 128, 55), (129,178,111))
    lines.append(green_line)
    grey_line = Line("Grey Line", ["East Didsbury", "Didsbury Village", "West Didsbury", "Burton Road", "Withington", "St Werburgh's Road",
                                   "Chorlton", "Firswood", "Trafford Bar", "Cornbrook", "Deansgate-Castlefield", "St Peter's Square",
                                   "Exchange Square", "Victoria", "Monsall", "Central Park", "Newton Heath and Moston", "Failsworth",
                                   "Hollinwood", "South Chadderton", "Freehold", "Westwood", "Oldham King Street", "Oldham Central",
                                   "Oldham Mumps", "Derker", "Shaw and Crompton"], (102, 95, 86), (181, 179, 176))
    lines.append(grey_line)
    pink_line = Line("Pink Line", ["East Didsbury", "Didsbury Village", "West Didsbury", "Burton Road", "Withington", "St Werburgh's Road",
                                   "Chorlton", "Firswood", "Trafford Bar", "Cornbrook", "Deansgate-Castlefield", "St Peter's Square",
                                   "Exchange Square", "Victoria", "Monsall", "Central Park", "Newton Heath and Moston", "Failsworth",
                                   "Hollinwood", "South Chadderton", "Freehold", "Westwood", "Oldham King Street", "Oldham Central",
                                   "Oldham Mumps", "Derker", "Shaw and Crompton", "Newhey", "Milnrow", "Kingsway Business Park", "Newbold",
                                   "Rochdale Railway Station", "Rochdale Town Centre"], (230, 50, 134), (233, 160, 194))
    lines.append(pink_line)
    red_line = Line("Red Line", ["The Trafford Centre", "Barton Dock Road", "Parkway", "Village", "Imperial War Museum", "Wharfside",
                                 "Pomona", "Cornbrook", "Deansgate-Castlefield"], (221, 41, 42), (219, 92, 93))
    lines.append(red_line)
    blue_line = Line("Blue Line", ["Eccles", "Ladywell", "Weaste", "Langworthy", "Broadway", "Harbour City", "Anchorage", "Salford Quays",
                                   "Exchange Quay", "Pomona", "Cornbrook", "Deansgate-Castlefield", "St Peter's Square",
                                   "Piccadilly Gardens", "Piccadilly", "New Islington", "Holt Town", "Etihad Campus", "Velopark",
                                   "Clayton Hall", "Edge Lane", "Cemetery Road", "Droylsden", "Audenshaw", "Ashton Moss", "Ashton West",
                                   "Ashton-under-Lyne"], (62, 108, 133), (148, 212, 247))
    lines.append(blue_line)
    orange_line = Line("Orange Line", ["MediaCityUK", "Harbour City", "Anchorage", "Salford Quays", "Exchange Quay", "Pomona", "Cornbrook",
                                       "Deansgate-Castlefield", "St Peter's Square", "Piccadilly Gardens", "Piccadilly", "New Islington",
                                       "Holt Town", "Etihad Campus"], (191, 109, 2), (237, 157, 51))
    lines.append(orange_line)
    yellow_line = Line("Yellow Line", ["Piccadilly", "Piccadilly Gardens", "Market Street", "Shudehill", "Victoria", "Queens Road",
                                       "Abraham Moss", "Crumpsall", "Bowker Vale", "Heaton Park", "Prestwich", "Besses o' th' Barn",
                                       "Whitefield", "Radcliffe", "Bury"], (194, 158, 17), (239, 206, 76))
    lines.append(yellow_line)
    
    abraham_moss = Tram_Stop("Abraham Moss", ["Green Line", "Yellow Line"], {"Queens Road":3, "Crumpsall":2}, 0, "Not required", ["N/A"], ["Zone 2"])
    tram_stops.append(abraham_moss)
    altrincham = Tram_Stop("Altrincham", ["Purple Line", "Green Line"], {"Navigation Road":3}, 0, "Not required", ["Bus Interchange", "Rail"], ["Zone 4"])
    tram_stops.append(altrincham)
    anchorage = Tram_Stop("Anchorage", ["Blue Line", "Orange Line"], {"Harbour City":1, "Salford Quays":2}, 0, "Not required", ["N/A"], ["Zone 2"])
    tram_stops.append(anchorage)
    ashton_moss = Tram_Stop("Ashton Moss", ["Blue Line"], {"Ashton West":3, "Audenshaw":2}, 199, "Not required", ["N/A"], ["Zone 3"])
    tram_stops.append(ashton_moss)
    ashton_west = Tram_Stop("Ashton West", ["Blue Line"], {"Ashton Moss":3, "Ashton-under-Lyne":3}, 195, "Not required", ["N/A"], ["Zone 3"])
    tram_stops.append(ashton_west)
    ashton_under_lyne = Tram_Stop("Ashton-under-Lyne", ["Blue Line"], {"Ashton West":3}, 0, "Not required", ["Bus interchange", "Rail"], ["Zone 3"])
    tram_stops.append(ashton_under_lyne)
    audenshaw = Tram_Stop("Audenshaw", ["Blue Line"], {"Ashton Moss":2, "Droylsden":3}, 0, "Not required", ["N/A"], ["Zone 3"])
    tram_stops.append(audenshaw)
    baguley = Tram_Stop("Baguley", ["Navy Line"], {"Roundthorn":2, "Moor Road":3}, 0, "Not required", ["N/A"], ["Zone 3"])
    tram_stops.append(baguley)
    barlow_moor_road = Tram_Stop("Barlow Moor Road", ["Navy Line"], {"Sale Water Park":3, "St Werburgh's Road":2}, 0, "Not required", ["N/A"], ["Zone 2", "Zone 3"])
    tram_stops.append(barlow_moor_road)
    barton_dock_road = Tram_Stop("Barton Dock Road", ["Red Line"], {"The Trafford Centre":1, "Parkway":3}, 0, "Not required", ["N/A"], ["Zone 3"])
    tram_stops.append(barton_dock_road)
    benchill = Tram_Stop("Benchill", ["Navy Line"], {"Crossacres":2, "Martinscroft":4}, 0, "Not required", ["N/A"], ["Zone 4"])
    tram_stops.append(benchill)
    besses_o_th_barn = Tram_Stop("Besses o' th' Barn", ["Yellow Line", "Green Line"], {"Prestwich":2, "Whitefield":3}, 9, "Currently unavailable", ["N/A"], ["Zone 3"])
    tram_stops.append(besses_o_th_barn)
    bowker_vale = Tram_Stop("Bowker Vale", ["Yellow Line", "Green Line"], {"Crumpsall":1, "Heaton Park":2}, 0, "Not required", ["N/A"], ["Zone 2", "Zone 3"])
    tram_stops.append(bowker_vale)
    broadway = Tram_Stop("Broadway", ["Blue Line"], {"Langworthy":2, "Harbour City":2}, 0, "Not required", ["N/A"], ["Zone 2"])
    tram_stops.append(broadway)
    brooklands = Tram_Stop("Brooklands", ["Green Line", "Purple Line"], {"Timperley":2, "Sale":2}, 84, "Yes", ["N/A"], ["Zone 3", "Zone 4"])
    tram_stops.append(brooklands)
    burton_road = Tram_Stop("Burton Road", ["Grey Line", "Pink Line"], {"West Didsbury":1, "Withington":2}, 0, "Yes", ["N/A"], ["Zone 3"])
    tram_stops.append(burton_road)
    bury = Tram_Stop("Bury", ["Yellow Line", "Green Line"], {"Radcliffe":6}, 100, "Yes", ["Bus interchange"], ["Zone 4"])
    tram_stops.append(bury)
    cemetery_road = Tram_Stop("Cemetery Road", ["Blue Line"], {"Edge Lane":2, "Droylsden":2}, 0, "Not required", ["N/A"], ["Zone 3"])
    tram_stops.append(cemetery_road)
    central_park = Tram_Stop("Central Park", ["Grey Line", "Pink Line"], {"Monsall":2, "Newton Heath and Moston":3}, 0, "Currently unavailable", ["N/A"], ["Zone 2"])
    tram_stops.append(central_park)
    chorlton = Tram_Stop("Chorlton", ["Grey Line", "Pink Line", "Navy Line"], {"St Werburgh's Road":2, "Firswood":1}, 0, "Yes", ["N/A"], ["Zone 2"])
    tram_stops.append(chorlton)
    clayton_hall = Tram_Stop("Clayton Hall", ["Blue Line"], {"Velopark":3, "Edge Lane":2}, 0, "Not required", ["N/A"], ["Zone 2"])
    tram_stops.append(clayton_hall)
    cornbrook = Tram_Stop("Cornbrook", ["Grey Line", "Pink Line", "Navy Line", "Green Line", "Purple Line", "Blue Line", "Orange Line", "Red Line"], {"Pomona":3, "Trafford Bar":2, "Deansgate-Castlefield":4}, 0, "Currently unavailable", ["N/A"], ["Zone 1", "Zone 2"])
    tram_stops.append(cornbrook)
    crossacres = Tram_Stop("Crossacres", ["Navy Line"], {"Wythenshawe Town Centre":2, "Benchill":1}, 0, "Not required", ["N/A"], ["Zone 4"])
    tram_stops.append(crossacres)
    crumpsall = Tram_Stop("Crumpsall", ["Yellow Line", "Green Line"], {"Abraham Moss":2, "Bowker Vale":2}, 43, "Not required", ["N/A"], ["Zone 2"])
    tram_stops.append(crumpsall)
    dane_road = Tram_Stop("Dane Road", ["Purple Line", "Green Line"], {"Sale":1, "Stretford":2}, 0, "Yes", ["N/A"], ["Zone 3"])
    tram_stops.append(dane_road)
    deansgate_castlefield = Tram_Stop("Deansgate-Castlefield", ["Grey Line", "Pink Line", "Navy Line", "Green Line", "Purple Line", "Blue Line", "Orange Line", "Red Line"], {"Cornbrook":4, "St Peter's Square":3}, 0,"Yes", ["Rail"], ["Zone 1"])
    tram_stops.append(deansgate_castlefield)
    derker = Tram_Stop("Derker", ["Pink Line", "Grey Line"], {"Oldham Mumps":2, "Shaw and Crompton":5}, 254, "Yes", ["N/A"], ["Zone 3"])
    tram_stops.append(derker)
    didsbury_village = Tram_Stop("Didsbury Village", ["Grey Line", "Pink Line"], {"East Didsbury":2, "West Didsbury":2}, 0, "Not required", ["N/A"], ["Zone 3"])
    tram_stops.append(didsbury_village)
    droylsden = Tram_Stop("Droylsden", ["Blue Line"], {"Cemetery Road":2, "Audenshaw":3}, 0, "Not required", ["N/A"], ["Zone 3"])
    tram_stops.append(droylsden)
    east_didsbury = Tram_Stop("East Didsbury", ["Grey Line", "Pink Line"], {"Didsbury Village":2}, 302, "Yes", ["Rail"], ["Zone 3"])
    tram_stops.append(east_didsbury)
    eccles = Tram_Stop("Eccles", ["Blue Line"], {"Ladywell":1}, 0, "Not required", ["Bus interchange", "Rail"], ["Zone 2"])
    tram_stops.append(eccles)
    edge_lane = Tram_Stop("Edge Lane", ["Blue Line"], {"Clayton Hall":2, "Cemetery Road":3}, 0, "Not required", ["N/A"], ["Zone 2", "Zone 3"])
    tram_stops.append(edge_lane)
    etihad_campus = Tram_Stop("Etihad Campus", ["Blue Line", "Orange Line"], {"Holt Town":2, "Velopark":3}, 0, "Yes",["N/A"], ["Zone 2"])
    tram_stops.append(etihad_campus)
    exchange_quay = Tram_Stop("Exchange Quay", ["Blue Line", "Orange Line"], {"Salford Quays":2, "Pomona":2}, 0, "Not required", ["N/A"], ["Zone 2"])
    tram_stops.append(exchange_quay)
    exchange_square = Tram_Stop("Exchange Square", ["Grey Line", "Pink Line"], {"St Peter's Square":3, "Victoria":3}, 0, "Not required", ["N/A"], ["Zone 1"])
    tram_stops.append(exchange_square)
    failsworth = Tram_Stop("Failsworth", ["Grey Line", "Pink Line"], {"Newton Heath and Moston":3, "Hollinwood":3}, 0, "Currently Unavailable", ["N/A"], ["Zone 3"])
    tram_stops.append(failsworth)
    firswood = Tram_Stop("Firswood", ["Grey Line", "Pink Line", "Navy Line"], {"Chorlton":2, "Trafford Bar":3}, 0, "Yes", ["N/A"], ["Zone 2"])
    tram_stops.append(firswood)
    freehold = Tram_Stop("Freehold", ["Grey Line", "Pink Line"], {"South Chadderton":2, "Westwood":3}, 3, "Currently unavailable", ["N/A"], ["Zone 3"])
    tram_stops.append(freehold)
    harbour_city = Tram_Stop("Harbour City", ["Orange Line", "Blue Line"], {"MediaCityUK":2, "Broadway":2, "Anchorage":1}, 0, "Not Required", ["N/A"], ["Zone 2"])
    tram_stops.append(harbour_city)
    heaton_park = Tram_Stop("Heaton Park", ["Green Line", "Yellow Line"], {"Bowker Vale":2, "Prestwich":2}, 9, "Yes", ["N/A"], ["Zone 3"])
    tram_stops.append(heaton_park)
    hollinwood = Tram_Stop("Hollinwood", ["Grey Line", "Pink Line"], {"Failsworth":3, "South Chadderton":1}, 192, "Currently unavailable", ["N/A"], ["Zone 3"])
    tram_stops.append(hollinwood)
    holt_town = Tram_Stop("Holt Town", ["Orange Line", "Blue Line"], {"Etihad Campus":1, "New Islington":2}, 0, "Not required", ["N/A"], ["Zone 2"])
    tram_stops.append(holt_town)
    imperial_war_museum = Tram_Stop("Imperial War Museum", ["Red Line"], {"Village":3, "Wharfside":2}, 0, "Not required", ["N/A"], ["Zone 2"])
    tram_stops.append(imperial_war_museum)
    kingsway_business_park = Tram_Stop("Kingsway Business Park", ["Pink Line"], {"Milnrow":1, "Newbold":2}, 0, "Not required", ["N/A"], ["Zone 4"])
    tram_stops.append(kingsway_business_park)
    ladywell = Tram_Stop("Ladywell", ["Blue Line"], {"Eccles":1, "Weaste":3}, 454, "Mot required", ["N/A"], ["Zone 2"])
    tram_stops.append(ladywell)
    langworthy = Tram_Stop("Langworthy", ["Blue Line"], {"Weaste":2, "Broadway":2}, 0, "Not required", ["N/A"], ["Zone 2"])
    tram_stops.append(langworthy)
    manchester_airport = Tram_Stop("Manchester Airport", ["Navy Line"], {"Shadowmoss":3}, 0, "Yes", ["Flights", "Rail", "Bus Interchange"], ["Zone 4"])
    tram_stops.append(manchester_airport)
    market_street = Tram_Stop("Market Street", ["Navy Line", "Green Line", "Yellow Line"], {"St Peter's Square":3, "Piccadilly Gardens":2, "Shudehill":1}, 0, "Not required", ["N/A"], ["Zone 1"])
    tram_stops.append(market_street)
    martinscroft = Tram_Stop("Martinscroft", ["Navy Line"], {"Benchill":3, "Roundthorn":2}, 0, "Not required", ["N/A"], ["Zone 4"])
    tram_stops.append(martinscroft)
    mediacityuk = Tram_Stop("MediaCityUK", ["Orange Line"], {"Harbour City":2}, 0, "Not required", ["N/A"], ["Zone 2"])
    tram_stops.append(mediacityuk)
    milnrow = Tram_Stop("Milnrow", ["Pink Line"], {"Newhey":3, "Kingsway Business Park":2}, 16, "Not required", ["N/A"], ["Zone 4"])
    tram_stops.append(milnrow)
    monsall = Tram_Stop("Monsall", ["Grey Line", "Pink Line"], {"Victoria":6, "Central Park":2}, 0, "Yes", ["N/A"], ["Zone 2"])
    tram_stops.append(monsall)
    moor_road = Tram_Stop("Moor Road", ["Navy Line"], {"Baguley":2, "Wythenshawe Park":2}, 0, "Not required", ["N/A"], ["Zone 3"])
    tram_stops.append(moor_road)
    navigation_road = Tram_Stop("Navigation Road", ["Purple Line", "Green Line"], {"Altrincham":2, "Timperley":2}, 71, "No lifts or ramps", ["Rail"], ["Zone 4"])
    tram_stops.append(navigation_road)
    new_islington = Tram_Stop("New Islington", ["Orange Line", "Blue Line"], {"Piccadilly":3, "Holt Town":2}, 0, "Not required", ["N/A"], ["Zone 1"])
    tram_stops.append(new_islington)
    newbold = Tram_Stop("Newbold", ["Pink Line"], {"Kingsway Business Park":2, "Rochdale Railway Station":4}, 0, "Not required", ["N/A"], ["Zone 4"])
    tram_stops.append(newbold)
    newhey = Tram_Stop("Newhey", ["Pink Line"], {"Shaw and Crompton":4, "Milnrow":2},  0, "Not required", ["N/A"], ["Zone 4"])
    tram_stops.append(newhey)
    newton_heath_and_moston = Tram_Stop("Newton Heath and Moston", ["Grey Line", "Pink Line"], {"Central Park":2, "Failsworth":2}, 0, "Not required", ["N/A"], ["Zone 2", "Zone 3"])
    tram_stops.append(newton_heath_and_moston)
    northern_moor = Tram_Stop("Northern Moor", ["Navy Line"], {"Wythenshawe Park":3, "Sale Water Park":4}, 0, "Not required", ["N/A"], ["Zone 3"])
    tram_stops.append(northern_moor)
    old_trafford = Tram_Stop("Old Trafford", ["Green Line", "Purple Line"], {"Stretford":2, "Trafford Bar":2}, 0, "Not required", ["N/A"], ["Zone 2"])
    tram_stops.append(old_trafford)
    oldham_central = Tram_Stop("Oldham Central", ["Grey Line", "Pink Line"], {"Oldham King Street":2, "Oldham Mumps":3}, 0, "Not required", ["N/A"], ["Zone 3"])
    tram_stops.append(oldham_central)
    oldham_king_street = Tram_Stop("Oldham King Street", ["Grey Line", "Pink Line"], {"Oldham Central":2, "Westwood":2}, 0, "Not required", ["N/A"], ["Zone 3"])
    tram_stops.append(oldham_king_street)
    oldham_mumps = Tram_Stop("Oldham Mumps", ["Grey Line", "Pink Line"], {"Oldham Central":3, "Derker":2}, 258, "Not required", ["Bus Interchange"], ["Zone 3"])
    tram_stops.append(oldham_mumps)
    parkway = Tram_Stop("Parkway", ["Red Line"], {"Barton Dock Road":4, "Village":3}, 360, "Not required", ["N/A"], ["Zone 2", "Zone 3"])
    tram_stops.append(parkway)
    peel_hall = Tram_Stop("Peel Hall", ["Navy Line"], {"Shadowmoss":2, "Robinswood Road":2}, 0, "Not required", ["N/A"], ["Zone 4"])
    tram_stops.append(peel_hall)
    piccadilly_gardens = Tram_Stop("Piccadilly Gardens", ["Orange Line", "Blue Line", "Purple Line", "Yellow Line"], {"St Peter's Square":3, "Market Street":2, "Piccadilly":3}, 0, "Not required", ["Bus interchange"], ["Zone 1"])
    tram_stops.append(piccadilly_gardens)
    piccadilly = Tram_Stop("Piccadilly", ["Purple Line", "Yellow Line", "Orange Line", "Blue Line"], {"Piccadilly Gardens":3, "New Islington":3}, 0, "Yes", ["Rail"], ["Zone 1"])
    tram_stops.append(piccadilly)
    pomona = Tram_Stop("Pomona", ["Red Line", "Orange Line", "Blue Line"], {"Exchange Quay":3, "Wharfside":2, "Cornbrook":3}, 0, "Yes", ["N/A"], ["Zone 2"])
    tram_stops.append(pomona)
    prestwich = Tram_Stop("Prestwich", ["Green Line", "Yellow Line"], {"Besses o' th' Barn":2, "Heaton Park":2}, 33, "Not required", ["N/A"], ["Zone 3"])
    tram_stops.append(prestwich)
    queens_road = Tram_Stop("Queens Road", ["Green Line", "Yellow Line"], {"Victoria":5, "Abraham Moss":3}, 0, "Yes", ["N/A"], ["Zone 2"])
    tram_stops.append(queens_road)
    radcliffe = Tram_Stop("Radcliffe", ["Yellow Line", "Green Line"], {"Whitefield":3, "Bury":6}, 369, "Not required", ["N/A"], ["Zone 4"])
    tram_stops.append(radcliffe)
    robinswood_road = Tram_Stop("Robinswood Road", ["Navy Line"], {"Peel Hall":1, "Wythenshawe Town Centre":2}, 0, "Not required", ["N/A"], ["Zone 4"])
    tram_stops.append(robinswood_road)
    rochdale_railway_station = Tram_Stop("Rochdale Railway Station", ["Pink Line"], {"Rochdale Town Centre":3, "Newbold":3}, 219, "Not required", ["Rail"], ["Zone 4"])
    tram_stops.append(rochdale_railway_station)
    rochdale_town_centre = Tram_Stop("Rochdale Town Centre", ["Pink Line"], {"Rochdale Railway Station":3}, 0, "Not required", ["Bus interchange"], ["Zone 4"])
    tram_stops.append(rochdale_town_centre)
    roundthorn = Tram_Stop("Roundthorn", ["Navy Line"], {"Martinscroft":2, "Baguley":1}, 0, "Not required", ["N/A"], ["Zone 3", "Zone 4"])
    tram_stops.append(roundthorn)
    sale_water_park = Tram_Stop("Sale Water Park", ["Navy Line"], {"Northern Moor":4, "Barlow Moor Road":3}, 301, "Not required", ["N/A"], ["Zone 3"])
    tram_stops.append(sale_water_park)
    sale = Tram_Stop("Sale", ["Purple Line", "Green Line"], {"Brooklands":2, "Dane Road":1}, 30, "Yes", ["N/A"], ["Zone 3"])
    tram_stops.append(sale)
    salford_quays = Tram_Stop("Salford Quays", ["Orange Line", "Blue Line"], {"Exchange Quay":2, "Anchorage":2}, 0, "No lifts or ramps", ["N/A"], ["Zone 2"])
    tram_stops.append(salford_quays)
    shadowmoss = Tram_Stop("Shadowmoss", ["Navy Line"], {"Manchester Airport":4, "Peel Hall":2}, 0, "Not required", ["N/A"], ["Zone 4"])
    tram_stops.append(shadowmoss)
    shaw_and_crompton = Tram_Stop("Shaw and Crompton", ["Grey Line", "Pink Line"], {"Derker":4, "Newhey":3}, 93, "Not required", ["N/A"], ["Zone 4"])
    tram_stops.append(shaw_and_crompton)
    shudehill = Tram_Stop("Shudehill", ["Navy Line", "Green Line", "Yellow Line"], {"Market Street":1, "Victoria":2}, 0, "Not required", ["Bus interchange"], ["Zone 1"])
    tram_stops.append(shudehill)
    south_chadderton = Tram_Stop("South Chadderton", ["Grey Line", "Pink Line"], {"Hollinwood":2, "Freehold":2}, 0, "Not required", ["N/A"], ["Zone 3"])
    tram_stops.append(south_chadderton)
    st_peters_square = Tram_Stop("St Peter's Square", ["Grey Line", "Pink Line", "Navy Line", "Green Line", "Purple Line", "Blue Line", "Orange Line"], {"Deansgate-Castlefield":3, "Market Street":3, "Exchange Square":3, "Piccadilly Gardens":3}, 0, "Not required", ["N/A"], ["Zone 1"])
    tram_stops.append(st_peters_square)
    st_werburghs_road = Tram_Stop("St Werburgh's Road", ["Grey Line", "Pink Line", "Navy Line"], {"Withington":2, "Barlow Moor Road":2, "Chorlton":2}, 0, "Yes", ["N/A"], ["Zone 2", "Zone 3"])
    tram_stops.append(st_werburghs_road)
    stretford = Tram_Stop("Stretford", ["Purple Line", "Green Line"], {"Dane Road":3, "Old Trafford":3}, 37, "Not required", ["N/A"], ["Zone 2", "Zone 3"])
    tram_stops.append(stretford)
    the_trafford_centre = Tram_Stop("The Trafford Centre", ["Red Line"], {"Barton Dock Road":2}, 0, "Not required", ["N/A"], ["Zone 3"])
    tram_stops.append(the_trafford_centre)
    timperley = Tram_Stop("Timperley", ["Green Line", "Purple Line"], {"Brooklands":2, "Navigation Road":3}, 0, "Currently unavailable", ["N/A"], ["Zone 4"])
    tram_stops.append(timperley)
    trafford_bar = Tram_Stop("Trafford Bar", ["Grey Line", "Pink Line", "Navy Line", "Green Line", "Purple Line"], {"Old Trafford":3, "Firswood":3, "Cornbrook":3}, 0, "Not required", ["N/A"], ["Zone 2"])
    tram_stops.append(trafford_bar)
    velopark = Tram_Stop("Velopark", ["Blue Line"], {"Etihad Campus":2, "Clayton Hall":3}, 0, "Not required", ["N/A"], ["Zone 2"])
    tram_stops.append(velopark)
    victoria = Tram_Stop("Victoria", ["Navy Line", "Green Line", "Yellow Line", "Grey Line", "Pink Line"], {"Shudehill":2, "Exchange Square":3, "Queens Road":4, "Monsall":6}, 0, "Not required", ["Rail"], ["Zone 1"])
    tram_stops.append(victoria)
    village = Tram_Stop("Village", ["Red Line"], {"Parkway":2, "Imperial War Museum":3}, 0, "Not required", ["N/A"], ["Zone 2"])
    tram_stops.append(village)
    weaste = Tram_Stop("Weaste", ["Blue Line"], {"Ladywell":3, "Langworthy":3}, 0, "Not required", ["N/A"], ["Zone 2"])
    tram_stops.append(weaste)
    west_didsbury = Tram_Stop("West Didsbury", ["Grey Line", "Pink Line"], {"Didsbury Village":2, "Burton Road":1}, 0, "Yes", ["N/A"], ["Zone 3"])
    tram_stops.append(west_didsbury)
    westwood = Tram_Stop("Westwood", ["Grey Line", "Pink Line"], {"Freehold":3, "Oldham King Street":3}, 0, "Yes", ["N/A"], ["Zone 3"])
    tram_stops.append(westwood)
    wharfside = Tram_Stop("Wharfside", ["Red Line"], {"Pomona":2, "Imperial War Museum":2}, 0, "Not required", ["N/A"], ["Zone 2"])
    tram_stops.append(wharfside)
    whitefield = Tram_Stop("Whitefield", ["Green Line", "Yellow Line"], {"Besses o' th' Barn":2, "Radcliffe":3}, 208, "Not required", ["N/A"], ["Zone 3", "Zone 4"])
    tram_stops.append(whitefield)
    withington = Tram_Stop("Withington", ["Grey Line", "Pink Line"], {"Burton Road":2, "St Werburgh's Road":2}, 0, "Yes", ["N/A"], ["Zone 3"])
    tram_stops.append(withington)
    wythenshawe_park = Tram_Stop("Wythenshawe Park", ["Navy Line"], {"Moor Road":1, "Northern Moor":2}, 0, "Not required", ["N/A"], ["Zone 3"])
    tram_stops.append(wythenshawe_park)
    wythenshawe_town_centre = Tram_Stop("Wythenshawe Town Centre", ["Navy Line"], {"Robinswood Road":3, "Crossacres":3}, 0, "Not required", ["Bus interchange"], ["Zone 4"])
    tram_stops.append(wythenshawe_town_centre)

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
    show_results(objects[11].get_stored_route(), objects[11].get_stored_trams())
    

main()
