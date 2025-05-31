from flask import render_template, request, url_for, redirect, flash, session
from app import app
from models import URL, db
from datetime import datetime
import random
import validators

def generate_short_url():
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    short_url = ''.join(random.choices(characters, k=6))
    return short_url


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def index_post():
    url_input = request.form.get('urlTxt')
    custom_url = request.form.get('urlCustom')

    if not url_input:
        flash('Please enter a URL')
        return redirect(url_for('index'))
    
    if not url_input.startswith(('http://','https://')):
        flash('Please enter a valid URL')
        return redirect(url_for('index'))
    
    if not validators.url(url_input):
        flash('Please enter a valid URL')
        return redirect(url_for('index'))

    url = URL.query.filter_by(original_url=url_input).first()    

    if url:
        short_url = url.shorten_url
        return render_template("index.html", full_url=url_input, short_url=short_url)

    if custom_url:
        existing = URL.query.filter_by(shorten_url=custom_url).first()
        if existing:
            flash('Custom URL already exists. Please choose a different one.')
            return redirect(url_for('index'))
        
        shortened_url = URL(original_url=url_input, shorten_url=custom_url)
        db.session.add(shortened_url)   
        db.session.commit()
        return render_template("index.html", full_url=url_input, short_url=custom_url)

    while True:
        short_url = generate_short_url() 
        existing = URL.query.filter_by(shorten_url=short_url).first()

        if not existing:
            shortened_url = URL(original_url=url_input, shorten_url=short_url)
            db.session.add(shortened_url)   
            db.session.commit()
            return render_template("index.html", full_url=url_input, short_url=short_url)


@app.route('/<short_url>')
def get_url(short_url):
    url = URL.query.filter_by(shorten_url=short_url).first()
    if not url:
        flash('Please enter a valid URL')
        return redirect(url_for('index'))
    return redirect(url.original_url)


