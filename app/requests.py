import urllib.request,json
from .models import Article, Source,News

api_key = None
source_url = None
everything_url = None

search_url = None
headlines_url = None


def configure_request(app):
    global api_key,headlines_url,everything_url,source_url
    api_key = app.config['API_KEY']
    source_url = app.config['EVERYTHING_URL']
    everything_url = app.config['EVERYTHING_URL']

    headlines_url = app.config['HEADLINES_URL']

def get_articles(id):
    """
	Function that gets the json response to our headlines url request
	"""
    get_headline_url = headlines_url.format(id,api_key)

    with urllib.request.urlopen(get_headline_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        articles_results = None

        if get_headlines_response['articles']:
            headlines_result_list=get_headlines_response['articles']
            articles_results = process_articles(headlines_result_list)
            print(articles_results)
    return articles_results

def process_articles(article_list):
    """
    	Function  that processes the headlines result and transform them to a list of Objects
    	Args:
        	headlines_list: A list of dictionaries that contain news headlines
    	Returns :
        	headlines_results: A list of news headlines objects
	"""
    articles_results = []

    for headline in article_list or []:
        id = headline.get('id')
        title = headline.get('title')
        name = headline.get('source.name')
        description = headline.get('description')
        url = headline.get('url')
        urlToImage = headline.get('urlToImage')
        publishedAt = headline.get('publishedAt')
        author = headline.get('author')

        article_object = Article(id,title,name,url,urlToImage,publishedAt,description,author)
        articles_results.append(article_object)

    return articles_results

def get_news_sources(category):
    """
    Function that get json response from the api soures endpoint
    """
    get_sources_url = source_url.format(category,api_key)
    print('*********get_sources_url***********')
    print(get_sources_url)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_result_list = get_sources_response['sources']
            sources_results = process_sources(sources_result_list)

    return sources_results

def process_sources(sources_list):
    """
    Function that processes the sources result and transform them to a list of Objects
    Args:
        sources_list: A list of dictionaries that contains sources
    Returns:
        sources_results: A list of news sources Objects
    """
    sources_results = []
    for source in sources_list :
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        country = source.get('country')     

        source_object = Source(id,name,description,category,url,country)
        sources_results.append(source_object)
    return sources_results


def get_all_source_result(source):
    """
    Function that returns all news from a particular source
    """
    get_sources_url = everything_url.format(source,api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        news_results = None
        if get_sources_response['articles']:
            sources_result_list = get_sources_response['articles']
            news_results = process_news(sources_result_list)
    return news_results
    
def process_news(news_list):
    news_results = []
    for news in news_list:
        name = news.get('name')
        description =news.get('description')
        url = news.get('url')

        news_object = News(name,description,url)
        news_results.append(news_object)
    return news_results