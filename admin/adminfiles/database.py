import mysql.connector
import mysql

# import sqlite3

data=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    db="python_project_1"
)

# data =sqlite3.connect("python_project_1")
Cursor=data.cursor() #program will not run without cursor

def adminLogin(arg):
    try:
        print("i am arg",arg)
        Cursor.execute("SELECT * FROM admin WHERE user_name =%s and password =%s", arg)
        return Cursor.fetchone()
    except:
        return False


def addEmp(arg):
    
    try:
        print(arg)
        Cursor.execute("INSERT INTO addemployee (EmpId, Name, Email, Password, Contact, Address, DOJ) VALUES (%s,%s,%s,%s,%s,%s,%s)", arg)
        data.commit()
        return True
    except:
        return False

def addPro(arg):
    
    try:
        print(arg)
        Cursor.execute("INSERT INTO addproject (ProName, details) VALUES (%s,%s)", arg)
        data.commit()
        return True
    except:
        return False


def addtask(arg):
    try:
        # print(arg)
        Cursor.execute("INSERT INTO tasks (projectId,name) VALUES (%s,%s)", arg)
        data.commit()
        return True
    except:
        return []

def assigntask(arg):
    try:
        # print(arg)
        Cursor.execute("INSERT INTO assigntask (EmpId,taskId,Startdate,Enddate,Status) VALUES (%s,%s,%s,%s,%s)", arg)
        data.commit()
        return True
    except:
        return []

def allEmployees():
    try:
        Cursor.execute("SELECT * FROM addemployee")
        return Cursor.fetchall()
    except:
        return False
    
def allProjects():
    try:
        Cursor.execute("SELECT * FROM addproject")
        return Cursor.fetchall()
    except:
        return False

def allTask():
    # Cursor.execute("SELECT * FROM addtask")

    try:
        Cursor.execute("SELECT tasks.id,addproject.ProName,tasks.name FROM tasks inner join addproject on addproject.id=tasks.projectId")
        return Cursor.fetchall()
    except:
        return []

def allassignTask():
    try:
        Cursor.execute("SELECT assigntask.id,addemployee.Name, tasks.name, assigntask.Startdate, assigntask.Enddate, assigntask.Status FROM assigntask left join addemployee on addemployee.id = assigntask.EmpId left join tasks on tasks.id = assigntask.taskId")
        return Cursor.fetchall()
    except:
        return []


def allFeedback():
    try:
        Cursor.execute("SELECT * FROM feedback")
        return Cursor.fetchall()
    except:
        return False

def deleteEmp(id):
    try:
        Cursor.execute("DELETE FROM addemployee WHERE id = %s", id)
        data.commit()
        return True
    except:
        return False


def deleteTask(id):
    try:
        Cursor.execute("DELETE FROM tasks WHERE id = %s", id)
        data.commit()
        return True
    except:
        return []

def deleteProject(id):
    try:
        Cursor.execute("DELETE FROM addproject WHERE id = %s", id)
        data.commit()
        return True
    except:
        return False

def get_employee(gup):
    try:
        print('get',gup)
        Cursor.execute("SELECT * FROM addemployee WHERE Id=%s",gup)
        return Cursor.fetchone()
    except:
        return False

def get_project(gup):
    try:
        print('get',gup)
        Cursor.execute("SELECT * FROM addproject WHERE id=%s",gup)
        return Cursor.fetchone()
    except:
        return False

def get_assigntask(gup):
    try:
        print('get',gup)
        Cursor.execute("SELECT addemployee.id, addemployee.Name, tasks.name, assigntask.Startdate, assigntask.Enddate, assigntask.Status, tasks.id FROM assigntask left join addemployee on addemployee.id = assigntask.EmpId left join tasks on tasks.id = assigntask.taskId WHERE assigntask.id = %s", gup)
        return Cursor.fetchone()
    except:
        return False

def update_employee(gup):
    try:
        print('get hello',gup)
        Cursor.execute(" UPDATE addemployee SET EmpId=%s,Name=%s,Email=%s,Password=%s,Contact=%s,Address=%s,DOJ=%s WHERE Id=%s",gup)
        data.commit()
        return True
    except:
        return False

def update_project(gup):
    try:
        print('get hello',gup)
        Cursor.execute(" UPDATE addproject SET ProName=%s,date=%s,details=%s WHERE id=%s",gup)
        data.commit()
        return True
    except:
        return False

def update_assigntask(gup):
    try:
        print('get hello',gup)
        Cursor.execute(" UPDATE assigntask SET EmpId=%s,taskId=%s,Startdate=%s,Enddate=%s,Status=%s WHERE id=%s",gup)
        data.commit()
        return True
    except:
        return False

def get_task(gup):
    try:
        print('get',gup)
        Cursor.execute("SELECT addproject.id, addproject.ProName, tasks.name FROM tasks left join addproject on addproject.id = tasks.projectId WHERE tasks.id = %s", gup)
        return Cursor.fetchone()
    except:
        return []


def update_task(gup):
    # Cursor.execute(" UPDATE addtask SET EmpId=%s,TaskName=%s,Status=%s,StartDate=%s,EndDate=%s WHERE Id=%s",gup)
    # data.commit()
    try:
        print('get',gup)
        Cursor.execute(" UPDATE tasks SET projectId=%s,name=%s WHERE id=%s",gup)
        data.commit()
        return True
    except:
        return []

#  Cursor.execute(" UPDATE addtask SET EmpId=:EmpId,TaskName=:TaskName,Status=:Status,StartDate=:StartDate,EndDate=:EndDate WHERE Id=:Id",
#             {
#             'EmpId':gup[0],
#             'TaskName':gup[1],
#             'Status':gup[2],
#             'StartDate':gup[3],
#             'EndDate':gup[4],
#             'Id':gup[5],
#         })
#         dat


def nameEmp():
    # Cursor.execute('SELECT Name from sqlb_temp_table_4')

    try:
        Cursor.execute('SELECT id,Name from addemployee')
        return Cursor.fetchall()
    except:
        return False

def namePro():
    # Cursor.execute('SELECT Name from sqlb_temp_table_4')

    try:
        Cursor.execute('SELECT id,ProName from addproject')
        return Cursor.fetchall()
    except:
        return False

def nameTask():
    try:
        Cursor.execute('SELECT id,name from tasks')
        return Cursor.fetchall()
    except:
        return False
        


def pendingTask():
    try:
        Cursor.execute('SELECT * from assigntask WHERE status = "pending"')
        return Cursor.fetchall()
    except:
        return []

def completedTask():
    try:
        Cursor.execute('SELECT * from assigntask WHERE status = "completed"')
        return Cursor.fetchall()
    except:
        return []

def ReportTask(val):
    try:
        Cursor.execute("SELECT * from tasks where projectId = %s", (val,))
        return Cursor.fetchall()
    except:
        return []

def reportassignTask(val):
    print("value in db ",val)
    try:
        Cursor.execute("SELECT assigntask.id,addemployee.Name, tasks.name, assigntask.Startdate, assigntask.Enddate, assigntask.Status FROM assigntask left join addemployee on addemployee.id = assigntask.EmpId left join tasks on tasks.id = assigntask.taskId WHERE assigntask.taskId = %s",(val,))
        return Cursor.fetchall()
    except:
        return []