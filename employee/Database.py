import mysql.connector
import mysql

# import sqlite3

data=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    db="python_project_1"
)

# data =sqlite3.connect('E:/copy_project/project zip (1)/project folder/task_management.db')
Cursor=data.cursor() #program will not run without cursor

def employeeLogin(arg):
    print(arg)
    # Cursor.execute("SELECT * FROM addemployee WHERE email =%sand password =%s", arg)

    try:
        Cursor.execute("SELECT * FROM addemployee WHERE Email =%s and Password =%s", arg)
        return Cursor.fetchone()
    except:
        return False

def allTask():
    try:
        Cursor.execute("SELECT * FROM tasks")
        Cursor.fetchall()
        return True
    except:
        return False


def getEmpName(email):
    try:
        Cursor.execute('SELECT id from addemployee WHERE Email = %s', (email, ))
        return Cursor.fetchone()
    except:
        return False

def allPendingEmpTask(data):
    try:
        Cursor.execute('SELECT assigntask.id, addemployee.Name, tasks.name, assigntask.Startdate, assigntask.Enddate, assigntask.Status FROM assigntask inner join addemployee on addemployee.id = assigntask.EmpId left join tasks on tasks.id = assigntask.taskId WHERE addemployee.id = %s and assigntask.Status = "pending"', data)
        return Cursor.fetchall()
    except:
        return []


def allCompletedEmpTask(data):
    try:
        Cursor.execute('SELECT assigntask.id, addemployee.Name, tasks.name, assigntask.Startdate, assigntask.Enddate, assigntask.Status FROM assigntask inner join addemployee on addemployee.id = assigntask.EmpId left join tasks on tasks.id = assigntask.taskId WHERE addemployee.id = %s and assigntask.Status = "completed"', data)
        return Cursor.fetchall()
    except:
        return []

def allEmpTask(data):
    try:
        Cursor.execute('SELECT assigntask.id, addemployee.Name, tasks.name, assigntask.Startdate, assigntask.Enddate, assigntask.Status FROM assigntask left join addemployee on addemployee.id = assigntask.EmpId left join tasks on tasks.id = assigntask.taskId WHERE addemployee.id = %s ', data)
        return Cursor.fetchall()
    except:
        return []


def completeTask(arg):
    try:
        Cursor.execute('UPDATE assigntask SET Status = "completed" WHERE id = %s ', arg)
        data.commit()
        return True
    except:
        return []

def completeProject(arg):
    try:
        Cursor.execute('UPDATE assigntask SET Status = "completed" WHERE id = %s ', arg)
        data.commit()
        return True
    except:
        return []

def addFeedbacks(arg):
    try:
        Cursor.execute('INSERT INTO feedback (TaskName, EmpId, Feedback) VALUES (%s, %s, %s)', arg)
        data.commit()
        return True
    except:
        return False


def allEmpTaskName(data):
    try:
        Cursor.execute('SELECT tasks.name FROM assigntask left join addemployee on addemployee.id = assigntask.EmpId left join tasks on tasks.id = assigntask.taskId WHERE addemployee.Name = %s ', data)
        return Cursor.fetchall()
    except:
        return False

def allEmpName(data):
    try:
        Cursor.execute('SELECT addemployee.Name FROM assigntask left join addemployee on addemployee.id = assigntask.EmpId left join tasks on tasks.id = assigntask.taskId WHERE addemployee.Name = %s ', data)
        return Cursor.fetchall()
    except:
        return False

def allFeedback(args):
    try:
        Cursor.execute('SELECT * FROM feedback WHERE EmpId = %s', args)
        return Cursor.fetchall()
    except:
        return False
        
def allEmpProject(data):
    try:
        Cursor.execute('SELECT assigntask.id, addemployee.Name, tasks.name,addproject.ProName, assigntask.Startdate, assigntask.Enddate, assigntask.Status, addproject.id FROM assigntask left join addemployee on addemployee.id = assigntask.EmpId left join tasks on tasks.id = assigntask.taskId left join addproject on addproject.id=tasks.projectId WHERE addemployee.id = %s ', data)
        return Cursor.fetchall()
    except:
        return []

def allCompletedEmpProject(data):
    try:
        Cursor.execute('SELECT assigntask.id, addemployee.Name, tasks.name,addproject.ProName, assigntask.Startdate, assigntask.Enddate, assigntask.Status FROM assigntask left join addemployee on addemployee.id = assigntask.EmpId left join tasks on tasks.id = assigntask.taskId left join addproject on addproject.id=tasks.projectId WHERE addemployee.Name = %s and assigntask.Status = "completed"', data)
        return Cursor.fetchall()
    except:
        return []

def allPendingEmpProject(data):
    try:
        Cursor.execute('SELECT assigntask.id, addemployee.Name, tasks.name,addproject.ProName, assigntask.Startdate, assigntask.Enddate, assigntask.Status FROM assigntask left join addemployee on addemployee.id = assigntask.EmpId left join tasks on tasks.id = assigntask.taskId left join addproject on addproject.id=tasks.projectId WHERE addemployee.Name = %s and assigntask.Status = "pending"', data)
        return Cursor.fetchall()
    except:
        return []