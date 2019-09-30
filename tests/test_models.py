import unittest
from app.models import User,Posts,Comments,Subscribe

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'banana')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
        
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('banana'))

class PostsModelTest(unittest.TestCase):

    def setUp(self):

        self.new_post = Posts(title='Terabyte', body='This is a new post',category='Technology')

    def test_instance(self):
        '''
        Test case to check if new_post is an instance of Posts class
        '''
        self.assertTrue( isinstance( self.new_post, Posts) )

    def test_save_post(self):
        '''
        Test case to check if a post is saved to the database
        '''
        self.new_post.save_post()

        self.assertTrue( len(Posts.query.all()) > 0 )

class TestComments(unittest.TestCase):
    '''
    Test class to test behaviours of the Comments class
    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_comment = Comments(the_comment="This is a test comment")

    def test_instance(self):
        '''
        Test to check if new_comment is an instance of Comments
        '''

        self.assertTrue( isinstance( self.new_comment, Comments) )

    def test_save_comment(self):
        '''
        Test case to check if comment is saved to the database
        '''

        self.new_comment.save_comment()

        self.assertTrue( len(Comments.query.all()) > 0)



class TestSubscribe(unittest.TestCase):
    '''
    Test class to test behaviours of the Comments class
    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_subscriber = Subscribe(name="New Subscriber",email="newsubscriber@gmail.com")

    def test_instance(self):
        '''
        Test to check if new_comment is an instance of Comments
        '''

        self.assertTrue( isinstance( self.new_subscriber, Subscribe) )

    def test_save_subscriber(self):
        '''
        Test case to check if comment is saved to the database
        '''

        self.new_subscriber.save_subscriber()

        self.assertTrue( len(Subscribe.query.all()) > 0)


