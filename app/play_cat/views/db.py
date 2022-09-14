from random import randint
from django.core.handlers.wsgi import WSGIRequest

class Cat:
    def __init__(self, cat_name=None, action=None, state=None, image=None):
        self.cat_name = cat_name
        self.age = randint(1, 12)
        self.satiety = randint(20, 90)
        self.happiness = randint(20, 95)
        self.action = action
        self.state = state
        self.image = image

   