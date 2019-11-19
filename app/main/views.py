from flask import render_template, redirect, url_for,request
from ..requests import get_news_sources,get_articles,get_all_source_result,get_articles
import json
from . import main
from ..models import Article



@main.route('/')
def index():
    """
	  View root page function that returns the index page and its data
	  """
    title = "NEWSFINDER"
    source_list = get_news_sources('general')
    sports_list = get_news_sources('sports')
    business_list = get_news_sources('business')
    entertainment_list = get_news_sources('entertainment')
    return render_template('index.html',title=title ,sources=source_list,sports = sports_list,entertainment = entertainment_list,business = business_list)

@main.route('/article/<id>')
def articles(id):
    """
	  View headlines page function that returns the article page and its data
	  """
    title = "headlines"
    article = get_articles(id)

    return render_template('article.html',title=title,article=article)

@main.route('/source/<link>')
def source(link):
    """
    View function to display the news of a particular clicked news source
    """
    link = link.replace(" ","+")
    source = get_all_source_result(link)
    return render_template('sources.html',sources=source)
