from app import app
import unittest
import tests


class BaseClass(unittest.TestCase): 
	 # @classmethod
  #   def setUpClass(cls):
  #       pass 

  #   @classmethod
  #   def tearDownClass(cls):
  #       pass 

     def setUp(self):

  #       # creates a test client
        app.testing=True
        self.client = app.test_client()   
  #      print("the app isd ", self.app)
     def tearDown(self):
        pass 

     # Ensure login behaves correctly with correct credentials
     def test_correct_login(self):
        #with self.client:
        response = self.client.post('/login',
        	data=dict(username="amit", password="akm0107"),
        	follow_redirects=True
        )
        self.assertIn(b'You are now logged in', response.data)


     # Ensure login behaves correctly with incorrect credentials
     def test_incorrect_login(self):
        response = self.client.post(
            '/login',
            data=dict(username="wrong", password="wrong"),
            follow_redirects=True
        )
        self.assertIn(b'Username not found', response.data)



        # Ensure logout behaves correctly
     def test_logout(self):
        #with self.client:
            self.client.post(
                '/login',
                data=dict(username="amit", password="akm0107"),
                follow_redirects=True
            )
            response = self.client.get('/logout', follow_redirects=True)
            self.assertIn(b'You are now logged out', response.data)
            #self.assertFalse(current_user.is_active())

        # Ensure that logout page requires user login
     def test_logout_route_requires_login(self):
        response = self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'Login', response.data)


        # Ensure that the login page loads correctly
     def test_login_page_loads(self):
        response = self.client.get('/login')
        self.assertIn(b'Login', response.data)

        # Ensure that Flask was set up correctly
     def test_index(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)



   

