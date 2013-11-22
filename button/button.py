import pygame as pg


class Button(object):
    """A fairly straight forward button class."""
    def __init__(self,rect,color,function,**kwargs):
        self.rect = pg.Rect(rect)
        self.color = color
        self.function = function
        self.clicked = False
        self.hover_text = None
        self.clicked_text = None
        self.process_kwargs(kwargs)
        self.render_text()

    def process_kwargs(self,kwargs):
        """Various optional customization you can change by passing kwargs."""
        settings = {"hover_color" : None,
                    "clicked_color" : None,
                    "on_release" : True,
                    "text" : None,
                    "font" : pg.font.Font(None,16),
                    "font_color" : pg.Color("white"),
                    "hover_font_color" : None,
                    "clicked_font_color" : None,}
        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("Button has no keyword: {}".format(kwarg))
        self.__dict__.update(settings)

    def render_text(self):
        """Pre render the button text."""
        if self.text:
            if self.hover_font_color:
                color = self.hover_font_color
                self.hover_text = self.font.render(self.text,True,color)
            if self.clicked_font_color:
                color = self.clicked_font_color
                self.clicked_text = self.font.render(self.text,True,color)
            self.text = self.font.render(self.text,True,self.font_color)

    def check_event(self,event):
        """The button needs to be passed events from your program event loop."""
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.clicked = True
                if not self.on_release:
                    self.function()
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            if self.clicked and self.on_release:
                self.function()
            self.clicked = False

    def update(self,surface):
        """Update needs to be called every frame in the main loop."""
        color = self.color
        text = self.text
        if self.clicked and self.clicked_color:
            color = self.clicked_color
            if self.clicked_font_color:
                text = self.clicked_text
        elif self.hover_color and self.rect.collidepoint(pg.mouse.get_pos()):
            color = self.hover_color
            if self.hover_font_color:
                text = self.hover_text
        surface.fill(pg.Color("black"),self.rect)
        surface.fill(color,self.rect.inflate(-4,-4))
        if self.text:
            text_rect = text.get_rect(center=self.rect.center)
            surface.blit(text,text_rect)
