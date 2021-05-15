from flask import Flask, request, jsonify, render_template, url_for
from flask_cors import CORS

import sqlite3

app = Flask(__name__)
CORS(app)

# test
@app.route('/api/test')
def hello():
    return 'Hello World!'

# user login
@app.route('/api/login', methods = ['POST'])
def login():
    if request.method == 'POST':
        conn = sqlite3.connect('cits.db')
        
        try:
            username = request.form['username']
            password = request.form['password']
            cursor = conn.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            rows = cursor.fetchall()

            if len(rows) > 0:
                return jsonify(code=200,msg='success')
            else:
                return jsonify(code=400,msg='error')
        except:
            return jsonify(code=400,msg='error')
        finally:
            conn.close()

# user register
@app.route('/api/register', methods = ['POST'])
def register():
    if request.method == 'POST':
        conn = sqlite3.connect('cits.db')

        try:
            username = request.form['username']
            password = request.form['password']
            cursor = conn.execute("SELECT * FROM users WHERE username = ?", (username,))
            rows = cursor.fetchall()

            if len(rows) > 0:
                # Check whether the user already exists 
                return jsonify(code=400,msg='username has exist')
            else:
                try:
                    conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                    conn.commit()
                    print('register success')
                    return jsonify(code=200,msg='success')
                except:
                    return jsonify(code=400,msg='error')
                finally:
                    conn.close()
        except:
            return jsonify(code=400,msg='error')
        finally:
            conn.close()

# get units
@app.route('/api/units', methods = ['GET'])
def getUnit():
    conn = sqlite3.connect('cits.db')
    
    cursor = conn.execute("SELECT * FROM Units")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(code=200,data=rows)

# get unit by id
@app.route('/api/unitsById', methods = ['GET'])
def getUnitById():
    conn = sqlite3.connect('cits.db')
    
    unitId = request.args['id']
    cursor = conn.execute("SELECT * FROM Units WHERE ID = ?", (unitId,))
    rows = cursor.fetchall()
    conn.close()
    if len(rows):
        return jsonify(code=200,data=rows[0])
    else:
        return jsonify(code=200)

# get chapters
@app.route('/api/chapters', methods = ['GET'])
def getChapters():
    conn = sqlite3.connect('cits.db')
    
    unitId = request.args['id']
    cursor = conn.execute("SELECT * FROM chapters WHERE UnitID = ?", (unitId,))
    rows = cursor.fetchall()
    conn.close()
    return jsonify(code=200,data=rows)

# get sections
@app.route('/api/sections', methods = ['GET'])
def getSections():
    conn = sqlite3.connect('cits.db')
    
    chapterId = request.args['id']
    cursor = conn.execute("SELECT * FROM sections WHERE ChapterID = ?", (chapterId,))
    rows = cursor.fetchall()
    conn.close()
    return jsonify(code=200,data=rows)

# get quiz
@app.route('/api/quiz', methods = ['GET'])
def getQuiz():
    conn = sqlite3.connect('cits.db')
    
    unitId = request.args['id']
    cursor = conn.execute("SELECT * FROM quiz WHERE ID = ?", (unitId,))
    rows = cursor.fetchall()
    conn.close()
    if len(rows):
        return jsonify(code=200,data=rows[0])
    else:
        return jsonify(code=200)

# get questions
@app.route('/api/questions', methods = ['GET'])
def getQuestions():
    conn = sqlite3.connect('cits.db')
    
    quizId = request.args['id']
    cursor = conn.execute("SELECT * FROM questions WHERE QuizID = ?", (quizId,))
    rows = cursor.fetchall()
    result = []

    if len(rows) > 0:
        try:
            # get answers
            for index in range(len(rows)):
                cur = conn.execute("SELECT * FROM quizAnswers WHERE QuestionID = ?", (rows[index][0],))
                ansRows = cur.fetchall()
                result.append(rows[index] + tuple(ansRows))

            return jsonify(code=200,data=result)
        except:
            return jsonify(code=400,msg='error')
        finally:
            conn.close()
    else:
        return jsonify(code=200,data=rows)
    
@app.route('/api/quizAnswers', methods = ['GET'])
def getQuizAnswers():
    conn = sqlite3.connect('cits.db')
    
    questionId = request.args['id']
    cursor = conn.execute("SELECT * FROM quizAnswers WHERE QuestionID = ?", (questionId,))
    rows = cursor.fetchall()
    conn.close()
    return jsonify(code=200,data=rows)

# get user has learned chapters
@app.route('/api/userLearn', methods = ['GET'])
def getUserLearn():
    conn = sqlite3.connect('cits.db')
    
    username = request.args['username']
    unitId = request.args['unitId']
    cursor = conn.execute("SELECT * FROM userLearn WHERE username = ? AND UnitID = ?", (username, unitId))
    rows = cursor.fetchall()
    
    conn.close()
    if len(rows) > 0:
        return jsonify(code=200,data=(rows[0][2]))
    else:
        return jsonify(code=200)

# save user has learned chapters       
@app.route('/api/userLearn', methods = ['POST'])
def setUserLearn():
    conn = sqlite3.connect('cits.db')
    
    username = request.form['username']
    unitId = request.form['unitId']
    chapterId = request.form['chapterId']
    cursor = conn.execute("SELECT * FROM userLearn WHERE username = ? AND UnitID = ?", (username, unitId))
    rows = cursor.fetchall()
    if len(rows) > 0:
        # if has saved, save only when it is greater than the current chapter
        if int(chapterId) > int(rows[0][2]):
            try:
                conn.execute("UPDATE userLearn set chapter = ? WHERE username = ? AND UnitID = ?", (chapterId, username, unitId))
                conn.commit()
                print('update success')
                return jsonify(code=200,msg='success')
            except:
                return jsonify(code=400,msg='error')
            finally:
                conn.close()
        else:
            return jsonify(code=200)
    else:
        try:
            # Save a new chapter
            conn.execute("INSERT INTO userLearn (username, UnitID, chapter) VALUES (?, ?, ?)", (username, unitId, chapterId))
            conn.commit()
            print('insert success')
            return jsonify(code=200,msg='success')
        except:
            return jsonify(code=400,msg='error')
        finally:
            conn.close()
    
# get chapters top 5
@app.route('/api/hot-chapters', methods = ['GET'])
def getChaptersTop5():
    conn = sqlite3.connect('cits.db')
    
    cursor = conn.execute("SELECT * FROM chapters AS p WHERE p.ID IN ( SELECT p_top5.chapter FROM ( SELECT chapter FROM userLearn AS od GROUP BY chapter LIMIT 5 ) AS p_top5 )")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(code=200,data=rows)

# get user's score
@app.route('/api/userQuiz', methods = ['GET'])
def getUserQuiz():
    conn = sqlite3.connect('cits.db')
    
    username = request.args['username']
    unitId = request.args['unitId']
    cursor = conn.execute("SELECT * FROM userQuiz WHERE username = ? AND UnitID = ?", (username, unitId))
    rows = cursor.fetchall()
    conn.close()
    return jsonify(code=200,data=rows)

# save user's score
@app.route('/api/userQuiz', methods = ['POST'])
def postUserQuiz():
    conn = sqlite3.connect('cits.db')
    
    username = request.form['username']
    unitId = request.form['unitId']
    score = request.form['score']
    try:
        conn.execute("INSERT INTO userQuiz (username, UnitID, score) VALUES (?, ?, ?)", (username, unitId, score))
        conn.commit()
        print('insert success')
        return jsonify(code=200,msg='success')
    except:
        return jsonify(code=400,msg='error')
    finally:
        conn.close()

# frontend home page
@app.route('/')
def home():
    url_for('static', filename='/')
    return render_template('/index.html')

# frontend login page
@app.route('/login')
def loginPage():
    return render_template('/login.html')

# frontend register page
@app.route('/register')
def registerPage():
    return render_template('/register.html')

# frontend learn page
@app.route('/learn')
def learnPage():
    return render_template('/learn.html')

# frontend learnSections page
@app.route('/learnSections')
def learnSectionsPage():
    return render_template('/learnSections.html')

# frontend quiz page
@app.route('/quiz')
def quizPage():
    return render_template('/quiz.html')

@app.route('/aboutUs')
def aboutUsPage():
    return render_template('/aboutUs.html')

if __name__ == '__main__':
    app.debug = True
    app.run()