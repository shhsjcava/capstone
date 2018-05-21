from app import app 
import re,datetime
from flask import flash, request, render_template, url_for, redirect, jsonify, session, abort, escape,json
import dbconnect
from form import MyForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user, UserMixin, LoginManager
from flask import Flask
from flask_mysqldb import MySQL
from flask_login import LoginManager

# Flask-Login login manager
global course, topic


mysql = MySQL(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route('/')
def index():
    if 'user' in session:
        if session['usertype'] == 'student':
            print 'Logged in as a student %s' % escape(session['user'])
            return redirect(url_for('home', uid = session['user']))
        elif session['usertype'] == 'lecturer':
            print 'Logged in as a lecturer %s' % escape(session['user'])
            return redirect(url_for('lhome', uid = session['user']))
    return redirect(url_for('login'))


@app.route('/login', methods =['GET', 'POST'])
def login():
    error = None
    form = MyForm()
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        uid = request.form['uname']
        password = request.form['psw']
        if len(uid) in range(9, 12) and uid[:4] in ['6200', '9780']:
            try:
                user = cur.execute("SELECT COUNT(1) FROM player WHERE user_id = %s;", [uid])
                if cur.fetchone()[0]:
                    cur.execute("SELECT password FROM player WHERE user_id = %s;", [uid])  # FETCH THE PASSWORd
                    for row in cur.fetchall():
                        if bool(re.match(str(row[0]), str(password))): #check_password_hash(spass, password):
                            flash('welcome student ', uid)
                            session['logged_in'] = True
                            session['user'] = uid
                            session['usertype'] = 'student'
                            return redirect(url_for('home', uid=uid))

                        else:
                            flash("Wrong password, Try again")
                            return redirect(url_for("login"))
                else:
                    flash('User does not exist. Please contact your lecturer')
                    return redirect(url_for("login"))
            except ValueError:
                flash('Format was wrong, Enter again')
                return redirect(url_for("login"))
        elif re.match('^(1000)\d{4}', uid):
            print 'lecturer'
            try:
                user = cur.execute('SELECT COUNT(1) from lecturer where lect_id = %s;', [uid])
                if cur.fetchone()[0]:
                    cur.execute("SELECT lect_passwd FROM lecturer WHERE lect_id = %s;", [uid])  # FETCH THE HASHED PASSWORD
                    for row in cur.fetchall():
                        if bool(re.match(str(row[0]), str(password))):  # check_password_hash(lpass, password):
                            session['logged_in']= True
                            session['user'] = uid
                            session['usertype'] = 'lecturer'
                            return render_template('lecthome.html', lecturer = user)
                    else:
                            flash("Wrong password")
                            return redirect(url_for("login"))
                else:
                    flash('User does not exist. Please contact admin')
                    return redirect(url_for("login"))
            except ValueError:
                flash('Error')
                return redirect(url_for("login"))
        flash('Format was wrong, Enter again')
        return redirect(url_for("login"))
    return render_template('login.html', form = form)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out', 'success')
    return redirect(url_for('login'))

@app.route('/studenthome/<uid>')
def home(uid):
    # if not session.get('logged_in'):
    #     abort(401)
    courselist ={}

    cur = mysql.connection.cursor()
    cur.execute("SELECT course_id FROM enroll Where user_id = %s;", [uid])
    courses= cur.fetchall()
    print courses
    for i in courses:
        courselist[i] = []
        #courses.append(course[0])
    for n in courses:
        cur.execute("select topic_name from topic where course_id = %s;", [n])
        topics = cur.fetchall()
        courselist[n].append(topics)

        #print courselist
    return render_template('studenthome.html', student=uid, courselist=courselist)

@app.route('/home/<uid>')
def lhome(uid):
    courselist = []
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT course_id FROM course Where lect_id = %s;", [uid])
    for row in cur.fetchall():
        courselist.append(row)
    print courselist
    session['lectcourses'] = courselist
    return render_template('lecthome.html', lecturer=uid, courselist=courselist)

@app.route('/topic/report')
def topicreport():
    return 'apage'
    
@app.route('/addtask')
def addtask():
    print 'button'
    tests =[]
    testsoln =[]
    if request.method=='Post':
        task = request.form['task']
        soln = request.form['soln']
        hints = request.form['hints']
        tests.append(request.form['test'])
        testsoln.append(request.form['soln'])
        points = request.form['marks']
        print hints, task
        cur = mysql.connection.cursor()
        cur.execute('update question set question =%s, hints =%s, solution =%s, test_cases =%s, test_case_solution =%s, levels_num=%s, maxpoints =%s;', (task, hints, soln, tests, testsoln,session['level'], points))
        cur.commit()
        flash('task added')
        return redirect(url_for({{'addtask'}}))
    return render_template('addtask.html')

def report(uid):
    cur = mysql.connection.cursor()
    cur.execute('select * from plays join topic where user_id =%s;', [uid])
    return cur.fetchall()

def deletestudent(uid,cid):
    cur = mysql.connection.cursor()
    cur.execute('delete from enroll where user_id =%s and course_id =%s;', (uid, cid))
    cur.commit()
    return 'student deleted'


@app.route('/task')
def getquiz():
    topic = request.args.get('topic')
    course = request.args.get('course')

    session['current_course'] =course
    session['current_topic'] = topic
    print topic, course
    return redirect(url_for('tests', uid = session['user'], toc = session['current_topic'], cour= session['current_course']))
    #return jsonify(result='Select Level')

@app.route('/tasks/<cour>/<toc>')
def tests( cour, toc):
    comlevel =[]
    nonlevels=[]
    #uid = session['user']
    print (cour, toc)
    cur = mysql.connection.cursor()
    cur.execute('select levels_num from board where complete = 1')
    for row in cur.fetchall():
        comlevel.append(int(row[0]))
        for num in range(6):
            if int(row[0]) != num:
                nonlevels.append(num)
    # cur.execute('select question_id, levels_num from plays where user_id = %s;', [uid])
    # comlevqstn = cur.fetchall()
    print comlevel, nonlevels
    print session
    return render_template('test.html', student =session['user'], topic=toc, course=cour, nonlevels= nonlevels,comlevel =comlevel)

@app.route('/home/<uid>/<cid>')
def lechome2(cid, uid):
    courselist = session['lectcourses']
    return render_template('lecturer-again.html', cid = cid, courselist =courselist)

@app.route('/_check', methods= ['GET', 'POST'])
def task():

    if request.method =="POST":
        slevel = request.form['question'][0]
        session['current_level'] = slevel
        qid = request.form['question'][1]
        print slevel, qid

        session['current_task'] = qid

        cur = mysql.connection.cursor()
        cur.execute('select question, hints, test_cases, solution, test_case_solution from question where question_id = %s and levels_num = %s;', (int(qid), int(slevel)))
        for row in cur.fetchall():

            question = row[0]
            hint =row[1]
            test_cases= row[2]
            test_soln = row[4]
            soln= row[3]
            session['question'] = question
            session['qhint'] = hint
            session['qtestcases'] = test_cases
            session['qtestsolns'] = test_soln
            session['qsoln'] = soln
        #time1 = datetime.datetime.now().strftime("%H:%M")
        print session
        return render_template('task.html', question=question, hint=hint, testcase=test_cases)



@app.route('/<cid>/students', methods =['GET', 'POST'])
def coursestudents(cid):
    cur = mysql.connection.cursor()
    if request.method=='POST':
        uid = request.args('name')
        if len(uid) in range(9, 12) and uid[:4] in ['6200', '9780']:
            cur.execute('insert into enroll user_id =%s where course_id =%s;', (uid, cid))
            cur.commit()
            print(uid)
            flash ('student add')
            return redirect(url_for('coursestudents', cid = cid))
        flash('error')
        print 'no'
        return redirect(url_for('coursestudents', cid = cid))
    students =[]
    ccid =cid[3:11]
    cur.execute("select user_id from enroll where course_id = %s;", [ccid])
    for row in cur.fetchall():
        students.append(row[0])
    print students, 'here'
    return render_template('lecturer-students.html', students = students, cid = cid)
    
@app.route('/<cid>/topics')
def coursetopics(cid):
    print cid
    topics =[]
    ccid =cid[3:11]
    cur = mysql.connection.cursor()
    cur.execute("select topic_name from topic where course_id = %s;", [ccid])
    for row in cur.fetchall():
        topics.append(row[0])
    print topics, 'here'
    return render_template('lect-topic.html', topics = topics, cid = cid)

@app.route('/_test', methods= ['GET', 'POST'])
def compiler():
    soln = request.args.get('code')
    print soln
    test= dbconnect.functions()
    results= test.fun(soln)
    #solntime =datetime.datetime.now().strftime("%H:%M") - time1
    #session['time'] = solntime
    if request.method =="POST":
        soln = request.args.get('code')
        print soln

        # cur.mysql.connection.cursor()
        #
        # cur.execute('update table plays where ')
        return 'soln added'

    return jsonify(results)




# def createpsw():
#     user_entered_password = 'pa$$w0rd'
#     salt = "5gz"
#     db_password = user_entered_password + salt
#     h = hashlib.md5(db_password.encode())
#
#
#     #password = sha256_crypt.encrypt("password")
#     #password2 = sha256_crypt.encrypt("password")
#
#     return h

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)

