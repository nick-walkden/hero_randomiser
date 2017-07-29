import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

from hero import *
import random
app = Flask(__name__)


@app.route('/')
def show_random():

    N,register,names = get_current_hero_register(app.root_path)


    new_hero = hero()
    ability_tags = ['lmb','rmb','q','e','r']

    for tag in ability_tags:
        n = random.randint(0,N-1)
        new_hero.setAbility(tag,register[names[n]].getAbility(tag))
    #return text.format(h=new_hero)
    return render_template('layout.html',hero=new_hero)

if __name__=='__main__':
    app.run()
    
    
    
