import unittest
from app.models import Article,Source

def ArticleTest(unittest.TestCase):
    '''
    It is used to test Article class.
    '''
    def setUp(self):
        '''
        It will set up an instance of Article which we will use in each test.
        '''
        self.new_Article = Article("the-verge","Trump stops flights from muslim countries","The Verge","Trump has banned all flights from the middle east in his bid to rid America of 'unwanted foreigners'....","www.the-verge.com","www.the-verge.com/trump",20:03:2018,"Ruth Mcdonald")
        self.new_Source=Source("the-verge","The Verge","Trump has banned all flights from the middle east in his bid to rid America of 'unwanted foreigners'....","general","www.the-verge.com","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_Article,Article))
        self.assertTrue(isinstance(self.new_Source,Source))


    
