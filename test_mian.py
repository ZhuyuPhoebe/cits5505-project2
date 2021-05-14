import unittest
from main import app
import json

class TestMain(unittest.TestCase):
    """defined"""
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_empty_name_password(self):
        """Test simulation scenario, user name or password is incomplete"""
        response = self.client.post("/api/login", data={})

        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)

        # error code 400
        code = resp_dict.get("code")
        self.assertEqual(code, 400)

        # just name
        response = self.client.post("/api/login", data={"username": "admin"})

        # response.data is response
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)

        # code 400
        code = resp_dict.get("code")
        self.assertEqual(code, 400)

        # return information
        msg = resp_dict.get('msg')
        self.assertEqual(msg, "error")

    def test_wrong_name_password(self):
        """test user name or password"""
        response = self.client.post("/api/login", data={"username": "admin", "password": "123456789"})

        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        self.assertEqual(code, 400)

        # return information
        msg = resp_dict.get('msg')
        self.assertEqual(msg, "error")

    def test_register(self):
        """test register when user name has exist"""
        response = self.client.post("/api/register", data={"username": "root", "password": "123456789"})

        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        self.assertEqual(code, 400)

        # return information
        msg = resp_dict.get('msg')
        self.assertEqual(msg, "username has exist")

    def test_register_empty(self):
        """test password is empty"""
        response = self.client.post("/api/register", data={"username": "root"})

        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        self.assertEqual(code, 400)

        # return information
        msg = resp_dict.get('msg')
        self.assertEqual(msg, "error")

    def test_units(self):
        """test units"""
        response = self.client.get("/api/units")

        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        self.assertEqual(code, 200)

        # return information
        data = resp_dict.get('data')
        self.assertEqual(len(data), 3)

    def test_units_by_id(self):
        """test units by id"""
        response = self.client.get("/api/unitsById?id=1")

        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        self.assertEqual(code, 200)

        # return information
        data = resp_dict.get('data')
        self.assertEqual(data[0], 1)

    def test_chapters(self):
        """test chapters where units id is 1"""
        response = self.client.get("/api/chapters?id=1")

        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        self.assertEqual(code, 200)

        # return information
        data = resp_dict.get('data')
        self.assertEqual(len(data), 3)

    def test_sections(self):
        """test sections where chapter id is 1"""
        response = self.client.get("/api/sections?id=1")

        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        self.assertEqual(code, 200)

        # return information
        data = resp_dict.get('data')
        self.assertEqual(len(data), 2)

    def test_quiz(self):
        """test quiz where units id is 1"""
        response = self.client.get("/api/quiz?id=1")

        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        self.assertEqual(code, 200)

        # return information
        data = resp_dict.get('data')
        self.assertEqual(data[0], 1)

    def test_questions(self):
        """test questions where quiz id is 1"""
        response = self.client.get("/api/questions?id=1")

        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        self.assertEqual(code, 200)

        # return information
        data = resp_dict.get('data')
        self.assertEqual(len(data), 9)

    def test_userLearn(self):
        """test user has learned chapters"""
        response = self.client.get("/api/userLearn?username=root&unitId=1")

        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        self.assertEqual(code, 200)

        # return information
        data = resp_dict.get('data')
        self.assertEqual(data, 1)

    def test_save_userLearn(self):
        """test save user has learned chapters"""
        response = self.client.post("/api/userLearn", data={"username": "root", "unitId": 2, "chapterId": 5})

        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        self.assertEqual(code, 200)

        # return information
        msg = resp_dict.get('msg')
        self.assertEqual(msg, 'success')

    def test_top_5_chapters(self):
        """test top 5 chapters"""
        response = self.client.get("/api/hot-chapters")

        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        self.assertEqual(code, 200)

        # return information
        data = resp_dict.get('data')
        self.assertEqual(len(data), 2)

    def test_userLearn_after_save(self):
        """test user has learned chapters after save"""
        response = self.client.get("/api/userLearn?username=root&unitId=2")

        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        self.assertEqual(code, 200)

        # return information
        data = resp_dict.get('data')
        self.assertEqual(data, 5)

    def test_user_quiz(self):
        """test user score"""
        response = self.client.get("/api/userQuiz?username=root&unitId=1")

        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        self.assertEqual(code, 200)

        # return information
        data = resp_dict.get('data')
        self.assertEqual(len(data), 0)

    def test_save_user_quiz(self):
        """test user score"""
        response = self.client.post("/api/userQuiz", data={"username": "root", "unitId": 2, "score": "100"})

        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        self.assertEqual(code, 200)

        # return information
        msg = resp_dict.get('msg')
        self.assertEqual(msg, 'success')

    def test_user_quiz_after_save(self):
        """test user score"""
        response = self.client.get("/api/userQuiz?username=root&unitId=2")

        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        self.assertEqual(code, 200)

        # return information
        data = resp_dict.get('data')
        self.assertEqual(len(data), 1)

if __name__ == '__main__':
    unittest.main()