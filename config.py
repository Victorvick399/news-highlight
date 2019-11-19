import os

class Config:
	"""
	General configuration parent class
	"""
	API_KEY=os.environ.get('API_KEY')
	SOURCE_URL='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
	HEADLINES_SEARCH_URL='https://newsapi.org/v2/top-headlines?category={}&query={}&apiKey={}'
	HEADLINES_URL='https://newsapi.org/v2/everything?q={}&apiKey={}'
	EVERYTHING_URL='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
	

class ProdConfig(Config):
	"""
	Production configuration child class
	Args:
		Config:The parent configuration class with general configuration settings
	"""
	pass

class DevConfig(Config):
	"""
	Development configuration child class
	Args:
		Config: the parent configuration class with general configuration settings
	"""
	DEBUG= True

config_options  = {
'development':DevConfig,
'production':ProdConfig
}