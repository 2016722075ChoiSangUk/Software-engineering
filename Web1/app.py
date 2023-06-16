from flask import Flask, request, render_template, redirect, session, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy import create_engine, text

app = Flask(__name__)
app.debug = True
app.secret_key = 'av6sv7wwrnwr26f8a8g8g28742y4f'

app.config.from_pyfile('config.py')

engine = create_engine(app.config['DB_URL'])
app.database = engine
 

def get_user(user_id):
    with app.database.connect() as connection:
        user = connection.execute(text("""
            SELECT 
                id,
                username,
                password
            FROM users
            WHERE id = :user_id
        """), {
            'user_id': user_id 
        }).fetchone()

        return {
            'id': user[0],
            'username': user[1],
            'password' : user[2]
        } if user else None


def insert_user(user):
    with app.database.connect() as connection:
        result = connection.execute(text("""
            INSERT INTO users (
                id,
                username,
                password
            ) VALUES (
                :id,
                :username,
                :password
            )
        """), {
            'id': user['id'],
            'username': user['username'],
            'password': user['password']
        })

        last_inserted_id = result.lastrowid
        connection.commit()
        return last_inserted_id

def get_subjects():
    subjects = []
    with app.database.connect() as connection:
        subject = connection.execute(text("""
            SELECT *
            FROM subject
        """)

        )
        for row in subject:
            subject = {
                '학정번호': row[0],
                '과목명': row[1],
                '이수': row[2],
                '학점': row[3],
                '시간': row[4],
                '담당교수': row[5],
                '강의시간': row[6],
                '강의유형': row[7]
            }
            subjects.append(subject)

    return subjects

def get_lecture(user_id):
    lectures = []
    with app.database.connect() as connection:
        lecture = connection.execute(text("""
            SELECT 
                *
            FROM student
            WHERE login_ID = :user_id
        """), {
            'user_id': user_id 
        }

        )
        for row in lecture:
            lecture = {
                '과목명': row[1],
                '강의시간': row[3]
            }
            lectures.append(lecture)

    return lectures

whitelist = ["/static", "/login","/register",'/forgot-password']

@app.before_request
def require_authorization():
    if any(filter(lambda x:request.path.startswith(x), whitelist)) or ('username' in session.keys()):
        print("PASS")
        pass
    else:
        print("REDIRECT", request.path, whitelist)
        return redirect('/login')



@app.route('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login?logout')

@app.route('/login.do', methods=["POST"])
def login_do():
    uid = request.form['id']
    pw = request.form['password']
    exist_user = get_user(uid) 

    print(uid, pw)
    print(exist_user)

    if uid == 'admin':
        session['username'] = uid
        return redirect('/index_admin')

    elif int(uid) == exist_user['id'] and pw == exist_user['password']:
        session['username'] = uid
        return redirect('/index')
        
    else:
        return redirect('/login')

@app.route('/register')
def register():
    return render_template('register.html')



@app.route('/register.do', methods=["POST"])
def register_do():
    new_user    = request.form
    new_user    = dict(new_user)
    
    exist_user = get_user(new_user['id'])
    if exist_user:
        return redirect('/register')
    
    new_user_id = insert_user(new_user)
    
    return redirect('/login')

    #return jsonify(new_user)


@app.route('/forgot-password')
def forgotpwd():
    return render_template('forgot-password.html')

@app.route('/index')
def index():
    uid = session['username']
    lectures = get_lecture(uid)
    users = get_users()
    week = ['월', '화', '수', '목', '금']
    lec = [(d['과목명'], d['강의시간']) for d in lectures]
    return render_template('index.html', lectures=lectures, users=users, week = week, lec = lec, uid = uid)

@app.route('/index_admin')
def index_admin():
    uid = session['username']
    return render_template('index_admin.html', uid = uid)

def get_subject():
    with app.database.connect() as connection:
        subjects = connection.execute(text("""
            SELECT *
            FROM subject
        """)).fetchall()
        
        return subjects

def get_users():
    with app.database.connect() as connection:
        users = connection.execute(text("""
            SELECT *
            FROM users
        """)).fetchall()
        
        return users

def get_student():
    with app.database.connect() as connection:
        student = connection.execute(text("""
        SELECT *
        FROM student
        """)).fetchall()
        
        return student

@app.route('/tables', methods=['GET', 'POST'])
def tables():
    uid = session['username']

    if request.method == 'POST':
        login_ID = request.form.get('user_id')
        subject_id = request.form.get('subject_id')
        
        with app.database.connect() as connection:
            # 사용자 정보 가져오기
            user = connection.execute(text("""
                SELECT id, username
                FROM users
                WHERE id = :login_ID
            """), {'login_ID': login_ID}).fetchone()
            
            # 과목 정보 가져오기
            subject = connection.execute(text("""
                SELECT *
                FROM subject
                WHERE 과목명 = :subject_id
            """), {'subject_id': subject_id}).fetchone()

            print(user)
            print(subject_id)
        
            # 수강신청 정보를 student 테이블에 저장
            connection.execute(text("""
                INSERT INTO student (login_ID, 과목, 학점, 시간, 담당교수)
                VALUES (:login_ID, :과목, :학점, :시간, :담당교수)
            """), {'login_ID': user['id'], '과목': subject['과목명'], '학점': subject['학점'], '시간': subject['강의시간'], '담당교수': subject['담당교수']})
        
        return redirect('/index')  # 수강신청이 성공적으로 완료되었을 경우 반환할 메시지
        
    else:
        subjects = get_subject()
        users = get_users()
        return render_template('tables.html', subjects=subjects, users=users, uid = uid)

@app.route('/notice')
def notice():
    student = get_student()
    uid = session['username']
    return render_template('notice.html', student=student, uid = uid)

@app.route('/noticepage')
def noticepage():
    uid = session['username']
    return render_template('noticepage.html', uid = uid)

@app.route('/noticewrite')
def noticewrite():
    uid = session['username']
    return render_template('noticewrite.html', uid = uid)

@app.route('/noticemodify')
def noticemodify():
    uid = session['username']
    return render_template('noticemodify.html', uid = uid)


@app.route('/work')
def work():
    uid = session['username']
    return render_template('work.html', uid = uid)

@app.route('/workpage')
def workpage():
    uid = session['username']
    return render_template('workpage.html', uid = uid)

@app.route('/workwrite')
def workwrite():
    uid = session['username']
    return render_template('workwrite.html', uid = uid)

@app.route('/workmodify')
def workmodify():
    uid = session['username']
    return render_template('workmodify.html', uid = uid)


@app.route('/file')
def file():
    uid = session['username']
    return render_template('file.html', uid = uid)

@app.route('/filepage')
def filepage():
    uid = session['username']
    return render_template('filepage.html', uid = uid)

@app.route('/filewrite')
def filewrite():
    uid = session['username']
    return render_template('filewrite.html', uid = uid)

@app.route('/filemodify')
def filemodify():
    uid = session['username']
    return render_template('filemodify.html', uid = uid)


@app.route('/grade')
def grade():
    uid = session['username']
    if(uid == 'admin'):
        return redirect('/index_admin')
    subjects = get_subject()
    users = get_users()
    return render_template('grade.html', subjects=subjects, users=users, uid = uid)

@app.route('/gradeview')
def gradeview():
    uid = session['username']
    if(uid == 'admin'):
        return redirect('/index_admin')
    lectures = get_lecture(uid)
    return render_template('gradeview.html', subjects=lectures, uid = uid)


@app.route('/lecture')
def lecture():
    uid = session['username']
    subjects = get_subjects()
    return render_template('lecture.html', subjects=subjects, uid = uid)

if __name__ == '__main__':
    app.run(debug=True)
