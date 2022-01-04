#Data Representation - Project
#John Paul Lee - G00387906
#Lecturer - Andrew Beatty
#Code is adapted from code generated through lectures through the semester

#Import required modules

import mysql
import mysql.connector


#Create a class EmployeeDAO to contain all functions
class ElectronicDAO:
    #Variable stores database connection
    db = ""       
    def __init__(self):
        #Will open a connection to a MySQL server and return a MySQLConnection object
        self.db = mysql.connector.connect (   
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'datarepresentation'
        )
        #Check if connection is made
        #print("Connection made") 


#Add new item to electronic table (datarepresentation database on mysql)
    def create(self, electronic):
        cursor = self.db.cursor()
        sql = "Insert into electronic (electronic_make, electronic_model, electronic_price) values (%s,%s,%s)"
        values = [
            electronic['electronic_make'],
            electronic['electronic_model'],
            electronic['electronic_price']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

#Get all the item records from the electronic table
    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from electronic'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        return returnArray

#Find a specific item record by id (electronic_id)
    def findById(self,electronic_id):
        cursor = self.db.cursor()
        sql = 'select * from electronic where electronic_id = %s'
        values = [electronic_id]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        return self.convertToDict(result)

#Update an items record
    def update(self, electronic):
        cursor = self.db.cursor()
        sql = "update electronic set electronic_make = %s, electronic_model = %s, electronic_price = %s where electronic_id = %s"
        values = [
            electronic['electronic_make'],
            electronic['electronic_model'],
            electronic['electronic_price'],
            electronic['electronic_id']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return electronic

#Delete an items record from electronic table
    def delete(self, electronic_id):
        cursor = self.db.cursor()
        sql = "delete from electronic where electronic_id = %s"
        values = [electronic_id]
        cursor.execute(sql, values)   
        self.db.commit()
        cursor.close()   
        return {} 


#Convert a list to dictionary
    def convertToDict(self, result):
        colnames = ['electronic_id', 'electronic_make', 'electronic_model', 'electronic_price']
        electronic = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                electronic[colName] = value

        return electronic



electronicDAO = ElectronicDAO()


