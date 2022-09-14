from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from random import randint

from play_cat.views.base import cat


def action_view(request):
    if request.POST.get('cat_name') is None:
        cat.cat_name = cat.cat_name
    else:
        cat.cat_name = request.POST.get('cat_name')
    cat.action = request.POST.get('action')
    cat.state = calculating_state_of_cat()
    cat.image = set_state_image()
    context = {
        'cat_name': cat.cat_name,
        'age': cat.age,
        'satiety': cat.satiety,
        'happiness': cat.happiness,
        'image': cat.image
    }
    return render(request, 'action_page.html', context)

def sleep_state():
    cat.state = 'sleep'
    return cat.state

def feed_state():
    if cat.state == 'sleep':
        return cat.state
    else:
        if cat.happiness == 100:
            cat.state = 'happy'
        if cat.satiety == 100:
            if cat.happiness - 30 < 0:
                cat.happiness = 0
                cat_state='angry'
            else:
                cat.happiness -= 30
            return cat.state
        if cat.satiety + 15 > 100:
            cat.happiness -= 30
            if cat.happiness < 0:
                cat.happiness = 0
            cat.satiety = 100
            cat.state = 'happy'
        else:
            cat.satiety += 15
            if cat.happiness + 5 > 100:
                cat.happiness = 100
            else:
                cat.happiness += 5
        cat.state == 'not_sleep'
    

def play_state():
    if cat.action == 'play with cat':
        if cat.state == 'sleep':
            cat.state = 'not_sleep'
            if cat.happiness - 5 > 0:
                cat.happiness -= 5
            else:
                cat.happiness = 0
        else:
            cat.state = 'play'
            angry_chance = randint(1, 3)
            if angry_chance == 3:
                cat.happiness = 0
                cat.state = 'angry'
            else:
                if cat.happiness + 15 > 100:
                    cat.happiness = 100
                    cat.state='happy'
                    if cat.satiety - 10 < 0:
                        cat.satiety = 0
                    else:
                        cat.satiety -= 10
                else:
                    cat.happiness += 15
                    cat.satiety -= 10
                    cat.state='happy'
    return cat.state

def calculating_state_of_cat():
    if cat.action == 'put cat to sleep':
        return sleep_state()
    elif cat.action == 'feed cat':
        return feed_state()
    else:
        return play_state()

def set_state_image():
    if cat.state=="happy":
        return 'img/happy.jpeg'
    elif cat.state == "angry":
        return 'img/angry.jpeg'
    elif cat.state =='sleep':
        return 'img/tired.jpeg'
    else:
        return 'img/day_mood.png'
    
    if 0<=cat.satiety<=30:
        return 'img/angry.jpeg'
    else: 
        return 'img/day_mood.png'





