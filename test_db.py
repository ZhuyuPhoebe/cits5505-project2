import unittest
from main import app
import json

import sqlite3

class TestMain(unittest.TestCase):
    """defined"""
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_user(self):
        """Test user schema"""
        conn = sqlite3.connect('cits.db')
        cursor = conn.execute("SELECT * FROM users LIMIT 1;")
        row = cursor.fetchall()[0]

        self.assertEqual(True, isinstance(row[0], str))
        self.assertEqual(True, isinstance(row[1], str))
        
        conn.close()
    
    def test_chapters(self):
        """Test chapters schema"""
        conn = sqlite3.connect('cits.db')
        cursor = conn.execute("SELECT * FROM chapters LIMIT 1;")
        row = cursor.fetchall()[0]

        self.assertEqual(True, isinstance(row[0], int))
        self.assertEqual(True, isinstance(row[1], str))
        self.assertEqual(True, isinstance(row[2], str))
        self.assertEqual(True, isinstance(row[3], int))
        
        conn.close()
    
    def test_questions(self):
        """Test questions schema"""
        conn = sqlite3.connect('cits.db')
        cursor = conn.execute("SELECT * FROM questions LIMIT 1;")
        row = cursor.fetchall()[0]

        self.assertEqual(True, isinstance(row[0], int))
        self.assertEqual(True, isinstance(row[1], str))
        self.assertEqual(True, isinstance(row[2], int))
        self.assertEqual(True, isinstance(row[3], int))
        
        conn.close()
    
    def test_quiz(self):
        """Test quiz schema"""
        conn = sqlite3.connect('cits.db')
        cursor = conn.execute("SELECT * FROM quiz LIMIT 1;")
        row = cursor.fetchall()[0]

        self.assertEqual(True, isinstance(row[0], int))
        self.assertEqual(True, isinstance(row[1], str))
        self.assertEqual(True, isinstance(row[2], int))
        
        conn.close()
    
    def test_quizanswers(self):
        """Test quizanswers schema"""
        conn = sqlite3.connect('cits.db')
        cursor = conn.execute("SELECT * FROM quizanswers LIMIT 1;")
        row = cursor.fetchall()[0]

        self.assertEqual(True, isinstance(row[0], int))
        self.assertEqual(True, isinstance(row[1], str))
        self.assertEqual(True, isinstance(row[2], int))
        self.assertEqual(True, isinstance(row[3], int))
        
        conn.close()
    
    def test_sections(self):
        """Test sections schema"""
        conn = sqlite3.connect('cits.db')
        cursor = conn.execute("SELECT * FROM sections LIMIT 1;")
        row = cursor.fetchall()[0]

        self.assertEqual(True, isinstance(row[0], int))
        self.assertEqual(True, isinstance(row[1], str))
        self.assertEqual(True, isinstance(row[2], str))
        self.assertEqual(True, isinstance(row[3], int))
        
        conn.close()
    
    def test_units(self):
        """Test units schema"""
        conn = sqlite3.connect('cits.db')
        cursor = conn.execute("SELECT * FROM units LIMIT 1;")
        row = cursor.fetchall()[0]

        self.assertEqual(True, isinstance(row[0], int))
        self.assertEqual(True, isinstance(row[1], str))
        self.assertEqual(True, isinstance(row[2], str))
        
        conn.close()
    
    def test_userLearn(self):
        """Test userLearn schema"""
        conn = sqlite3.connect('cits.db')
        cursor = conn.execute("SELECT * FROM userLearn LIMIT 1;")
        row = cursor.fetchall()[0]

        self.assertEqual(True, isinstance(row[0], str))
        self.assertEqual(True, isinstance(row[1], int))
        self.assertEqual(True, isinstance(row[2], int))
        
        conn.close()
    
    def test_userQuiz(self):
        """Test userQuiz schema"""
        conn = sqlite3.connect('cits.db')
        cursor = conn.execute("SELECT * FROM userQuiz LIMIT 1;")
        row = cursor.fetchall()[0]

        self.assertEqual(True, isinstance(row[0], str))
        self.assertEqual(True, isinstance(row[1], int))
        self.assertEqual(True, isinstance(row[2], int))
        
        conn.close()

if __name__ == '__main__':
    unittest.main()