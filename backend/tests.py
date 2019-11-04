import os
import unittest
from app import db, create_app


app = create_app()


#TEST_DB = 'test.db'


class BasicTests(unittest.TestCase):
    #def SetUp(self):
     #   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
      #      os.path.join(app.config['BASEDIR'], TEST_DB)
       # db.drop_all()
        #db.create_all()

    #def tearDown(self):
     #   pass

    def test_main_page(self):
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_feedback_page(self):
        self.app = app.test_client()
        response = self.app.get('/feedback', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_product_page(self):
        self.app = app.test_client()
        response = self.app.get('/products', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        self.app = app.test_client()
        response = self.app.get('/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_logout_page(self):
        self.app = app.test_client()
        response = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        self.app = app.test_client()
        response = self.app.get('/about', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    #def register(self, username, email, password, confirm):
     #   self.app = app.test_client()
      #  return self.app.post(
       #     '/register',
        #    data=dict(username=username, email=email, password=password, confirm=confirm),
         #   follow_redirects=True
        #)

    #def login(self, username, password):
     #   self.app = app.test_client()
      #  return self.app.post(
       #     '/login',
        #    data=dict(username=username, password=password),
         #   follow_redirects=True
        #)

    #def logout(self):
     #   self.app = app.test_client()
      #  return self.app.get(
       #     '/logout',
        #    follow_redirects=True
        #)

    #def test_valid_user_registration(self):
     #   response = self.register('newuser', 'newuser@lol.com', 'flask123', 'flask123')
      #  self.assertEqual(response.status_code, 200)
       # self.assertIn(b'Congratulations, you are now a registered user!', response.data)

    #def test_invalid_user_registration_different_passwords(self):
     #   response = self.register('newuser', 'newuser@lol.com', 'flask123', 'flask')
      #  self.assertIn(b'Field must be equal to password.',response.data)






if __name__ == "__main__":
    unittest.main()




