DROP DATABASE IF EXISTS go_peli;
CREATE DATABASE go_peli;
use go_peli;

DROP TABLE IF EXISTS lecturer_addition;
DROP TABLE IF EXISTS accomplish;
DROP TABLE IF EXISTS enroll;
DROP TABLE IF EXISTS plays;
DROP TABLE IF EXISTS points;
DROP TABLE IF EXISTS board;
DROP TABLE IF EXISTS levels;
DROP TABLE IF EXISTS receives;
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS question;
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS lecturer;

DROP TABLE IF EXISTS course;





CREATE TABLE lecturer(
	 lect_id varchar(55),
	 lect_passwd varchar(55),
	 primary key(lect_id)
 )ENGINE=InnoDB;



CREATE TABLE course(
	course_id varchar(55),
	course_name varchar(55),
	course_desc varchar(55),
	lect_id varchar(55),
	PRIMARY KEY (course_id,lect_id),
	FOREIGN Key(lect_id) REFERENCES lecturer(lect_id) ON UPDATE CASCADE ON DELETE CASCADE
)ENGINE=InnoDB;




CREATE TABLE player(
	user_id varchar(55),
	password varchar(55),
	PRIMARY KEY(user_id)
)ENGINE=InnoDB;



CREATE TABLE topic(
	topic_id int,
	topic_name varchar(55),
	course_id varchar(55),
	primary key (course_id,topic_id),
	FOREIGN key(course_id) REFERENCES course(course_id) ON UPDATE CASCADE on DELETE CASCADE,
	Unique(topic_name),
	unique(topic_id)
)ENGINE=InnoDB;


CREATE TABLE question(
	question_id int AUTO_INCREMENT,
	question LONGTEXT,
	hints LONGTEXT,
	solution LONGTEXT,
	test_cases LONGTEXT,
	test_case_solution LONGTEXT,
	topic_name varchar(55),
	PRIMARY KEY(question_id),
	FOREIGN KEY(topic_name) REFERENCES topic(topic_name) ON UPDATE CASCADE ON DELETE CASCADE
)ENGINE=InnoDB;

-- INSERT INTO question(question, hints,solution,topic_name)VALUES()


CREATE TABLE items(
	items_name varchar(55),
	topic_name varchar(55),
	PRIMARY KEY(items_name)
)ENGINE=InnoDB;

CREATE TABLE receives(
	items_name varchar(55),
	user_id varchar(55),
	topic_name varchar(55),
	FOREIGN KEY (user_id) REFERENCES player(user_id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(items_name)REFERENCES items(items_name) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(topic_name) REFERENCES topic(topic_name) ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY(user_id,items_name,topic_name)
)ENGINE=InnoDB;


CREATE TABLE levels(
	levels_num int,
	topic_name varchar(55),
	FOREIGN KEY(topic_name) REFERENCES topic(topic_name) ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY(levels_num,topic_name)
)ENGINE=InnoDB;


CREATE TABLE board(
	user_id varchar(55),
	levels_num int,
	score int,
	FOREIGN KEY(user_id) REFERENCES player(user_id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (levels_num) REFERENCES levels(levels_num) ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY Key(user_id,levels_num)
)ENGINE=InnoDB;


CREATE TABLE points(
	grade varchar(55),
	points double,
	PRIMARY KEY(grade)
	-- remember to calculate the grade
)ENGINE=InnoDB;

CREATE TABLE plays(
	question_id int,
	player_sol LONGTEXT,
	completed BOOLEAN,
	play_time TIME,
	test_case_correct int,
	soln_level varchar(5),
	qpoints int,
	user_id varchar(55),
	FOREIGN KEY (question_id) REFERENCES question(question_id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(user_id) REFERENCES player(user_id) ON UPDATE CASCADE ON DELETE CASCADE
)ENGINE=InnoDB;


CREATE TABLE enroll(
	user_id varchar(55),
	course_id varchar(55),
	FOREIGN KEY (user_id) REFERENCES player(user_id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (course_id) REFERENCES course(course_id) ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY(course_id,user_id)
)ENGINE=InnoDB;

CREATE TABLE accomplish(
	user_id varchar(55),
	topic_id int,
	FOREIGN KEY (user_id) REFERENCES player(user_id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(topic_id) REFERENCES topic(topic_id) ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY(user_id,topic_id)
)ENGINE=InnoDB;

CREATE TABLE lecturer_addition(
	question LONGTEXT,
	lect_solutions LONGTEXT,
	lect_test_case LONGTEXT,
	lect_test_case_solution LONGTEXT
)ENGINE=InnoDB;



INSERT INTO player(user_id,password) VALUES('978087543','annajohn');
INSERT INTO player(user_id,password)VALUES('97804737','jonahpusey98');
INSERT INTO player(user_id,password)VALUES('97803985','fiercegoddess98');
INSERT INTO player(user_id,password)VALUES('97803732','techisnotme123');
INSERT INTO player(user_id,password)VALUES('97807294','raspberrypi1010');
INSERT INTO player(user_id,password)VALUES('978029490','cuntyanna');
INSERT INTO player(user_id,password)VALUES('97803839','mariojose');
INSERT INTO player(user_id,password)VALUES('978092049','hdhowdmsam');
INSERT INTO player(user_id,password)VALUES('97807920','novascotia1054');
INSERT INTO player(user_id,password)VALUES('97805466','orangejuice');
INSERT INTO player(user_id,password)VALUES('97803455','lettuceprey');
INSERT INTO player(user_id,password)VALUES('97804655','hbdshadows18');
INSERT INTO player(user_id,password)VALUES('97806666','trevjohn98');

INSERT INTO player(user_id,password)VALUES('620085198','marriedjohn');
INSERT INTO player(user_id,password)VALUES('978011334','monalisa');
INSERT INTO player(user_id,password)VALUES('978033446','techsavvysowhat');

-- INSERT INTO player(user_id,password)VALUES('gopeli','GoPeli');
-- username:gopeli password:GoPeli

-- SERVER add 198.121.101.247


INSERT INTO lecturer(lect_id,lect_passwd)VALUES('10005611','anacondapy');
INSERT INTO lecturer(lect_id,lect_passwd)VALUES('10005622','disgustingmofo');
INSERT INTO lecturer(lect_id,lect_passwd)VALUES('10005633','davabarnia');
INSERT INTO lecturer(lect_id,lect_passwd)VALUES('10005788','joanofark');
INSERT INTO lecturer(lect_id,lect_passwd)VALUES('10005799','danielletraboja');
INSERT INTO lecturer(lect_id,lect_passwd)VALUES('10004596','uwichapel');
INSERT INTO lecturer(lect_id,lect_passwd)VALUES('10008991','treeoflife');
INSERT INTO lecturer(lect_id,lect_passwd)VALUES('10007892','puseyisvital');
INSERT INTO lecturer(lect_id,lect_passwd)VALUES('10007922','teaherbal34');
INSERT INTO lecturer(lect_id,lect_passwd)VALUES('10001234','whoisliving77');

INSERT INTO course(course_id,course_name,course_desc,lect_id)VALUES('COMP1126','Intro to Computing I','Learning Python I','10005611');
INSERT INTO course(course_id,course_name,course_desc,lect_id)VALUES('COMP1127','Intro to Computing II','Learning Python I','10005611');
INSERT INTO course(course_id,course_name,course_desc,lect_id)VALUES('COMP1161','Intro to Object-Oriented Programming','Learning Java','10005633');
INSERT INTO course(course_id,course_name,course_desc,lect_id)VALUES('COMP2201','Discrete Mathematics for Computer Science','Probability Distributions, Permutations & Combinations, etc','10005611');
INSERT INTO course(course_id,course_name,course_desc,lect_id)VALUES('INFO2180','Web Programming','Front and Back End Development','10005611');
INSERT INTO course(course_id,course_name,course_desc,lect_id)VALUES('COMP2211','Discrete Mathematics for Computer Science,','Probability Distributions,Permutations & Combinations,etc','10005622');
INSERT INTO course(course_id,course_name,course_desc,lect_id)VALUES('INFO2180','Web Programming','Front and Back End Development','10005788');
INSERT INTO course(course_id,course_name,course_desc,lect_id)VALUES('COMP1161','Intro to Object-Oriented Programming','Learning Java','10005799');

INSERT INTO course(course_id,course_name,course_desc,lect_id)VALUES ('COMP1126','Intro to Computing I','Learning Python I','10004596');

INSERT INTO course(course_id,course_name,course_desc,lect_id)VALUES('INFO2180','Web Programming','Front and Back Developement','10008991');
INSERT INTO course(course_id,course_name,course_desc,lect_id)VALUES('COMP2211','Discrete Mathematics for Computer Science','Probability Distributions,Permutations & Combinations,etc','10008991');



INSERT INTO enroll(user_id,course_id) VALUES('978087543','COMP1126');
INSERT INTO enroll(user_id,course_id) VALUES('978087543','COMP1127');
INSERT INTO enroll(user_id,course_id) VALUES('978087543','COMP1161');
INSERT INTO enroll(user_id,course_id) VALUES('978087543','INFO2180');
INSERT INTO enroll(user_id,course_id) VALUES('978029490','COMP1126');
INSERT INTO enroll(user_id,course_id) VALUES('97803839','COMP1127');
INSERT INTO enroll(user_id,course_id) VALUES('97807920','COMP1161');
INSERT INTO enroll(user_id,course_id) VALUES('978092049','COMP1126');
INSERT INTO enroll(user_id,course_id)VALUES('97807920','COMP1126');
INSERT INTO enroll(user_id,course_id)VALUES('97805466','COMP1127');
INSERT INTO enroll(user_id,course_id)VALUES('97803455','COMP1126');
INSERT INTO enroll(user_id,course_id)VALUES('97804655','COMP1127');
INSERT INTO enroll(user_id,course_id)VALUES('97806666','COMP1127');

INSERT INTO enroll(user_id,course_id)VALUES('620085198','COMP1126');
INSERT INTO enroll(user_id,course_id)VALUES('620085198','COMP1127');
INSERT INTO enroll(user_id,course_id)VALUES('620085198','COMP1161');
INSERT INTO enroll(user_id,course_id)VALUES('978011334','INFO2180');
INSERT INTO enroll(user_id,course_id)VALUES('978011334','COMP1126');
INSERT INTO enroll(user_id,course_id)VALUES('978033446','COMP1126');

INSERT INTO topic(topic_id,topic_name,course_id) VALUES(1001,'Intro to Functions','COMP1126');
INSERT INTo topic(topic_id,topic_name,course_id)VALUES(1002,'Python DataTypes','COMP1126');
INSERT INTO topic(topic_id,topic_name,course_id)VALUES(1003,'Python Loop Structures', 'COMP1126');
INSERT INTO topic(topic_id,topic_name,course_id)VALues(1004,'Recursion','COMP1126');
INSERT INTO topic(topic_id, topic_name,course_id)VALUES(1005,'Higher Order Functions','COMP1126');
INSERT INTO topic(topic_id,topic_name,course_id) VALUES(2001,'Abstract Data Types','COMP1127');
INSERT INTO topic(topic_id,topic_name,course_id)VALUES(3008,'GUI Programming in Java','COMP1161');


INSERT INTO accomplish(user_id, topic_id)VALUES('978087543',1001);
INSERT INTO accomplish(user_id, topic_id)VALUES('978087543',1002);
INSERT INTO accomplish(user_id, topic_id)VALUES('978087543',1003);
INSERT INTO accomplish(user_id, topic_id)VALUES('978087543',1004);
INSERT INTO accomplish(user_id, topic_id)VALUES('978087543',1005);

INSERT INTO accomplish(user_id,topic_id)VALUES('978087543',2001);
INSERT INTO accomplish(user_id,topic_id)VALUES('978029490',1004);


INSERT INTO points(grade, points) VALUES('90-100',4.3);
INSERT INTO points(grade, points) VALUES('80-89',4.0);
INSERT INTO points(grade, points) VALUES('75-79',3.7);
INSERT INTO points(grade, points) VALUES('70-74',3.3);
INSERT INTO points(grade, points) VALUES('65-69',3.0);
INSERT INTO points(grade, points) VALUES('60-64',2.7);

INSERT INTO points(grade, points) VALUES('55-59',2.3);
INSERT INTO points(grade, points) VALUES('50-54',2.0);
INSERT INTO points(grade, points) VALUES('45-49',1.7);
INSERT INTO points(grade, points) VALUES('40-44',1.3);
INSERT INTO points(grade,points)  VALUES('0-39',0.0);

INSERT INTO items(items_name,topic_name) VALUES('Tie','Intro to Functions');
INSERT INTO items(items_name,topic_name) VALUES('Jacket', 'Python DataTypes'); 
INSERT INTO items(items_name,topic_name) VALUES('Shoes','Python Loop Structures');
INSERT INTO items(items_name,topic_name) VALUES('Cap', 'Recursion');
INSERT INTO items(items_name,topic_name) VALUES('Gown','Higher Order Functions');
INSERT INTO items(items_name,topic_name) VALUES('Badge', 'Abstract Data Types');
INSERT INTO items(items_name,topic_name) VALUES('Socks','GUI Programming in Java');

INSERT INTO levels(levels_num,topic_name) VALUES(100,'Intro to Functions');
INSERT INTO levels(levels_num,topic_name) VALUES(101, 'Python DataTypes');
INSERT INTO levels(levels_num,topic_name) VALUES(102, 'Recursion');



-- UPDATE plays set completed= CASE WHEN(end_time NOT NULL) THEN completed="True" ELSE completed="False";

-- SELECT * FROM enroll; --show all students that are enrolled in the course game--
-- SELECT * FROM enroll WHERE course_id='COMP1126'; --show all the students that are enrolled in COMP1126 course game--
-- SELECT * FROM enroll WHERE course_id='COMP1127'; --show all the students that are enrolled in COMP1127 course game--
-- SELECT * FROM enroll WHERE course_id='COMP1161';--show all the students that are enrolled in COMP1161 course game--
-- SELECT * FROM enroll WHERE course_id='INFO2180';--show all the students that are enrolled in INFO2180 course game--

-- SELECT COUNT(user_id),course_id FROM enroll GROUP by course_id; --shows the numbers of students enrolled in each course--
 

-- SELECT * FROM player;

-- -- --Queries

 
INSERT INTO question(question, hints,solution,topic_name)VALUES("Given the lists above, write a function days_in_month which takes a month as an 
argument and finds the corresponding month in the month_days list and returns the 
number of days associated with that month,"'January',[31], February,[28,29], 'March',[31]), 


day_names =['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] 


","Solution
 
 
def days_in_month(mont):
    n=0
    for x in range (0,len(month_days)):
        if mont==month_days[x][0] :
            break
        else:
            n+=1
    return month_days[n][1]","Python Loop Structures");
    

INSERT INTO question(question, hints,solution, topic_name)VALUES("Using list comprehension, define a python function unlucky, which returns all the days in a given year which have the 
	date Friday 13th e.g.

>>>unlucky(2010) [(13, 8, 2010)]
>>>unlucky(2009)

[(13, 2, 2009), (13, 3, 2009), (13, 11, 2009)]",

" you need two ranges one for day starting from 1 and going to 31 and another one for month starting from 1 going to 12.
 Using these and the year which comes as an argument and use the function day_of_week in the if part of list comprehension to
 check if a given date is ‘Friday’ and also check if the day is equal to 13.]",

 "def unlucky(year):
    q=[]
    for x in range(1,13):
        s = day_of_week(13,x,year)
        if s=='Friday':
            q+=[(13,x,year)]
    return q
","Higher Order Functions");


INSERT INTO question(question, hints, solution, topic_name)Values("
Write a python function mostUnlucky, which lists all the years between 0 and 2010 which have 3 unlucky 
days. Use function unlucky to get a list of unlucky dates for a particular year and find the length of this list. If the length 
is greater than 2 then the year is added to another list which is returned as output.",


"Use List comprehension",
"def most_unlucky():
    return [x for x in range(0000,2010) if len(unlucky(x))>2]",
    

    "Higher Order Functions");

INSERT INTO question(question,test_cases,hints,solution, topic_name)VALUES("Complete the implementation of the rectangle class which takes three arguments no-sides 
	(number of sides), breadth and length to create a rectangle object. The rectangle class is a subclass of polygon class. Implement messages area and perimeter 
	for the rectangle class using the formulae given below.
	Area=length * breadth
	Perimeter= 2+( length * breadth)
",
"Testcases
>>>r1=rectangle(2,4)
>>>r1.area()
8
>>>r1.howmanysides()
4
>>>r1.perimeter()
12
","",'class Polygon:
    def __init__(self,nbrsides):
        self.nbr_sides = nbrsides
 
    def whoamI(self):
        if self.nbr_sides == 3:
            return "Triangle"
        elif self.nbr_sides == 4:
            return "Rectangle"
        else: return "Polygon"
 
    def howmanysides(self):
        return self.nbr_sides
 
    def area(self):
        return "No Area"
 
    def perimeter(self):
        return "No Perimeter"
 
class rectangle(Polygon):
    def area(self):
        return self.length * self.breadth
 
    def perimeter(self):
        return (2*(self.length + self.breadth))
 
    def __init__(self,breadth,length):
        Polygon.__init__(self,4)
        self.length= length
        self.breadth= breadth
 
class triangle(Polygon):
    def perimeter(self):
        return(self.a+self.b+self.c)
 
    def area(self):
        s= (self.a+self.b+self.c)/2.0
        return math.sqrt(s*(self.a)*(self.b)*(self.c))
 
    def __init__(self,a,b,c):
        Polygon.__init__(self,3)
        self.a=a
        self.b=b
        self.c=c

',"Intro to Functions");


INSERT INTO question(question, hints,solution,topic_name)VALUES("The postorder() method of flattening the example expression tree 
	tree_ex would give [40, 5, '+', 3, 7, 2, '-', '*', '/']. A stack is often used to evaluate such an expression. While traversing 
	through this list if an element is as operand then it is pushed onto a stack, and when an operator is found, then the stack is popped twice 
	and the operator is evaluated with the popped value and its result is pushed back onto the stack.

e.g.[40,5, ‘+’,3,2, ‘-’, ‘*’]	→ 45
","Write a function is_operator() which returns True if the argument is an operator (i.e. “+”, “-”, “*” or “/”)
 and False otherwise.",
 "def is_operator(x):
    if x == '+':
        return True
    elif x == '-':
        return True
    elif x == '*':
        return True
    elif x == '/':
        return True
    else:
        return False
 
","Intro to Functions");

INSERT INTO question(question, hints,solution,topic_name)VALUES("Write a function calc_letter_grade() which takes a student as input and returns a list of tuples 
	where the first part of the tuple is the course code and second part of the tuple is the letter grade.

From the student structure, first extract the course list which is a list of tuples of course codes 
and the number grades. Get the number grades from the course list and create a new list in which each number 
grade is converted to a letter grade. Recreate a new courses list with the list of courses and the list of letter grades.",

" Use map to apply a function to every element of the list. Also remember that zip takes two lists as 
inputs and creates a list of tuples e.g. zip ([1,2,3] ,[4,5,6]) => [(1, 4), (2, 5), (3, 6)] }

>>>calc_letter_grade(st1)
[('cs11q','A'),('cs11r','B'),('cs20r','C'),('cs20s','B'),('cs22q','B+'),('cs23q', 'A')]
","def compute_letter_grades(x):
    if x>100 or x<0:
        return 'Invalid Input'
    elif x>85:
        return 'A+'
    elif x>=70:
        return 'A'
    elif x>=67:
        return 'A-'
    elif x>=63:
        return 'B+'
    elif x>=60:
        return 'B'
    elif x>=57:
        return 'B-'
    elif x>=53:
        return 'C+'
    elif x>=50:
        return 'C'
    elif x>=47:
        return 'C-'
    elif x>=43:
        return 'D+'
    elif x>=36:
        return 'D'
    else:
        return 'F'
","Intro to Functions");

INSERT INTO question(question, test_cases,solution,topic_name)VALUES("Given a decimal number as input, Write a program to convert the given decimal number into equivalent binary number.",

"Input : 7                                                         
Output :111

Input :10
Output :1010",

"
findBinary(decimal)
   if (decimal == 0)
      binary = 0
   else
      binary = decimal % 2 + 10 * (findBinary(decimal / 2)
","Recursion");

INSERT INTO question(question, test_cases,solution, topic_name)VALUES("Given a number n, find sum of first n natural numbers. 
	To calculate the sum, we will use a recursive function recur_sum().",
	"Input : 3
	Output : 6
	Explanation : 1 + 2 + 3 = 6

	input : 5
	Output : 15
	Explanation : 1 + 2 + 3 + 4 + 5 = 15",

	"
	# Python code to find sum 
	# of natural numbers upto
	# n using recursion
 
	# Returns sum of first
	# n natural numbers
	def recurSum(n):
    if n <= 1:
        return n
    return n + recurSum(n - 1)
 

","Recursion");


INSERT INTO question(question,test_cases,solution,topic_name)VALUES("Given a number, we need to find sum of its digits using recursion.",
	"Input : 12345
	Output : 15

	Input : 45632
	Output :20",
	"# Recursive Python3 program to 
	# find sum of digits of a number
 
	# Function to check sum of
	# digit using recursion
	def sum_of_digit( n ):
    if n == 0:
        return 0
    return (n % 10 + sum_of_digit(int(n / 10)))
 

 
","Recursion");

 





 














