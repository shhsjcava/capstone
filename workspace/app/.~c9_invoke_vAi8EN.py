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
from types import ModuleType

# Flask-Login login manager
global course, topic


mysql = MySQL(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


'''GENERAL ROUTES'''
@app.route('/')
def index():
    if 'logged_in' in session:
        if session['usertype'] == 'student':
            print 'Logged in as a student %s' % escape(session['user'])
            return redirect(url_for('home', uid = session['user']))
        elif session['usertype'] == 'lecturer':
            print 'Logged in as a lecturer %s' % escape(session['user'])
            return redirect(url_for('home', uid = session['user']))
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
                            return redirect(url_for('home', uid=uid))
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


@app.route('/home/<uid>')
def home(uid):
    # if not session.get('logged_in'):
    #     abort(401)
    
    cur = mysql.connection.cursor()
    if session['usertype']=='student':
        print 'student at work'
        courselist ={}
        cur.execute("SELECT course_id FROM enroll Where user_id = %s;", [uid])
        courses= cur.fetchall()
        print courses
        for i in courses:
            courselist[i] = []
        for n in courses:
            cur.execute("select topic_name from topic where course_id = %s;", [n])
            topics = cur.fetchall()
            courselist[n].append(topics)
        return render_template('studenthome.html', student=uid, courselist=courselist)

    elif session['usertype']=='lecturer':
        print 'here'
        courselist=[]
        print 'lecturer at work'
        cur.execute("SELECT course_id FROM course Where lect_id = %s;", [uid])
        for row in cur.fetchall():
            courselist.append(row)
    
        scourselist
        return render_template('lecthome.html', lecturer=uid, courselist=courselist)
        
'''LECTURER ROUTES'''
###REPORT ROUTE!!!
@app.route('/<topic>/report')
def topicreport(topic):
    return 'apage'


@app.route('/<cid>/students', methods =['GET', 'POST'])
def coursestudents(cid):
    cur = mysql.connection.cursor()
    if request.method=='POST':
        uid = request.args('name')
        if len(uid) in range(9, 12) and uid[:4] in ['6200', '9780']:
            flash ('student ID format is incorrect')
            return redirect(url_for('coursestudents', cid = cid))
            
        flash(addstudent(cid, uid))
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
    if request.method =='POST':
        sid = request.args['name']
        flash(addstudent(cid,sid))
        user
    topics =[]
    ccid =cid[3:11]
    cur = mysql.connection.cursor()
    cur.execute("select topic_name from topic where course_id = %s;", [ccid])
    for row in cur.fetchall():
        topics.append(row[0])
    print topics, 'here'
    return render_template('lect-topic.html', topics = topics, cid = cid)
   
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

@app.route('/home/<uid>/<cid>')
def lechome2(cid, uid):
    courselist = session['lectcourses']
    return render_template('lecturer-again.html', cid = cid, courselist =courselist)


    
# @app.route('/lectreport')
# def lectreport():
#     cur=mysql.connection.cursor()
#     cur.execute('select course_id fr')
    
# @app.route('/<cid>/students')
# def lectreport(cid):
#     print cid[3:10]
#     cur = mysql.connection.cursor()
#     cur.execute('select user_id from enroll where course_id = %s;', [cid])
#     return render_template('lecturer-students.html')
    

'''STUDENT ROUTES!!! '''
@app.route('/levels/<cour>/<toc>')
def levels( cour, toc):
    userlevels={}
    session['current_course']=cour
    # session['current_topic']=topic
    uid = session['user']
    print toc
    cur = mysql.connection.cursor()
    cur.execute('select question_id from plays where completed= 1 and user_id =%s;', [uid])
    for row in cur.fetchall():
        userlevels[int(row[0])] ='completed'
    for key in range(6):
        if key not in userlevels:
            userlevels[key]='noncomplete'

    print userlevels 
    print session
    return render_template('level.html', student =session['user'], topic=toc, course=cour ,userlevels =userlevels)


    

@app.route('/tasks/<topic>/<level>')
def getallqstns(level, topic):
    if level:
        num=[]
        print level
        cour = session['current_course']
        session['current_topic']=topic
        toc = topic
        session['current_level'] = level
        cur = mysql.connection.cursor()
        cur.execute('select question_id FROM plays where completed=1 and user_id =%s;', [session['user']])
        for row in cur.fetchall():
            num.append(row)
        #print level, cour, toc, num
        # cur.execute
        print session
        return render_template('tasknew.html', cour =cour, toc = toc, level =level, num=num)
    
    
@app.route('/tasks/<toc>/<level>/<qid>')
def gettask( toc, level, qid):
    qid =1
    session['current_task'] = qid
    taskinfo ={}
    cur = mysql.connection.cursor()
    cur.execute('select question, hints, test_cases, test_case_solution from question where question_id = %s;', [int(qid)])
    for row in cur.fetchall():

        taskinfo['question'] = row[0]
        taskinfo['hint'] =row[1]
        taskinfo['test_cases']= row[2]
        taskinfo['test_soln'] = row[3]
        '''soln= row[3]'''
    
    print session
    return render_template('task.html', taskinfo= taskinfo )





@app.route('/_test', methods= ['GET', 'POST'])
def compiler():
    
    soln = request.args.get('code')
    soln + '\n print code(4,5,6)'
    res =test(soln)
    #
    print res
    # print soln
    # test= dbconnect.functions()
    # results= test.fun(str(soln))
    #solntime =datetime.datetime.now().strftime("%H:%M") - time1
    #session['time'] = solntime
    if request.method =="POST":
        soln = request.args.get('code')
        print soln

        # cur.mysql.connection.cursor()
        #
        # cur.execute('update table plays where ')
        return 'soln added'
    return jsonify(res)

def test(codes):
    mycor = compile(code,'','exec')
    exec(mycor)
    result =eval('code()')
    return result
    # compiled = compile(codes, '', 'exec')
    # module = ModuleType("testmodule")
    # exec(compiled, module.__dict__)
    

@app.route('/testcases')
def testcase():
    #soln + '\n print code('+ )'
    return 'p'
''''HELPER fUNCTIONS'''
# def createpsw():
#     user_entered_password = 'pa$$w0rd'
#     salt = "5gz"
#     db_password = user_entered_password + salt
#     h = hashlib.md5(db_password.encode())
#
#
#     #password = sha256_crypt.encrypt("password")
#     #password2 = sha256_crypt.encrypt("password")

def addstudent(cid, sid):
    cur = mysql.connection.cursor()
    if cur.execute('select * from enrolls where user_id =%s and course_id=%s;', (sid, cid)):
        return 'STudent exist already'
    cur.execute('insert into enroll user_id =%s where course_id =%s;', (sid, cid))
    cur.commit()
    return 'student add'
    
def report(uid):
    cur = mysql.connection.cursor()
    cur.execute('select * from plays join topic where user_id =%s;', [uid])
    return cur.fetchall()

def deletestudent(uid,cid):
    cur = mysql.connection.cursor()
    if cur.execute('select * from enrolls where user_id =%s and course_id=%s;', (sid, cid)):
        cur.execute('delete from enroll where user_id =%s and course_id =%s;', (uid, cid))
        cur.commit()
        return 'student deleted'
    return 'STudent does not exist already'


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
