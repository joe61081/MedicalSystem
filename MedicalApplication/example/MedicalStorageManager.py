'''
Created on 6 Feb 2019

@author: Luke61084
'''
import sys
import pickle
from builtins import int
from example.Patient import Patient
import jsonpickle
from importlib.resources import contents
from mysql import connector


class TextFileStorage(object):
    
    
    #Reading the file Contents
    @staticmethod
    def read_text_content(file_name):
        try:
            contents =""
            file_obj = open(file_name,"r")
            contents = file_obj.read()
            #print(contents)
            file_obj.close()
            return contents
        except:
            print("Error Occured",sys.exc_info())
            return contents
            
            
    #Appending the file Contents 
    @staticmethod
    def append_text_content(content,file_name,mode="a"):
        try:
            file_obj = open(file_name,mode)
            file_obj.write(content)
            file_obj.close()
        except:
            print("Error Occured",sys.exc_info())
            
class PatientStorage(object):
    
    @staticmethod
    def add_Patient_to_binary_file(new_Patient,file_name):
        try:
            pats = PatientStorage.get_patient_from_binary_file(file_name)
            pats.append(new_Patient)
            file_obj = open(file_name,'wb')
            pickle.dump(pats,file_obj)
            file_obj.close()
        except:
            print("Error Occured",sys.exc_info())
    
    @staticmethod
    def get_patient_from_binary_file(file_name):
        try:
            pats = []
            file_obj = open(file_name,"rb")
            pats = pickle.load(file_obj)
            file_obj.close()
            return pats
        except:
            print("Error Occured",sys.exc_info())
            return pats 
    @staticmethod
    def get_patients_from_json(file_name):
        try:
            pats=[]
            json_text = TextFileStorage.read_text_content(file_name)
            pats = jsonpickle.decode(json_text)
            return pats
        except: 
            print("Exception Occured",sys.exc_info())
            return pats
        
    @staticmethod
    def add_Patient_to_json(new_pat,file_name):
        pats = PatientStorage.get_Patients_from_json(file_name)
        pats.append(new_pat)
        json_text = jsonpickle.encode(pats)
        TextFileStorage.append_text_content(json_text, file_name, "w")
        
    @staticmethod
    def insert_Patient_in_db(new_pat):
        #1. Connect to the database
        cnx = connector.connect(user='root',password='root',database='medicalreports',port=3306)
        #2.Fetching the Cursor
        cur = cnx.cursor()
        #3. Use the cursor and executing the tpatlate query
        cur.execute('insert into pat_data_python values(%s,%s,%s,%s,%s)',
                    (new_pat.patient_id,
                     new_pat.patient_name,
                     new_pat.patient_date_of_birth,
                     new_pat.patient_location,
                     new_pat.patient_occupation))
        #4. commit all the queries if DML 
        cnx.commit()
        
        #5. Close the resources used
        cur.close()
        cnx.close()
         
    @staticmethod  
    def fetch_all_Patients_from_db():    
        cnx = connector.connect(user='root',password='root',database='medicalreports',port=3306)
        cur = cnx.cursor()
        cur.execute('select * from pat_data_python')
        pats = []
        for (patient_id,patient_name,patient_date_of_birth,patient_location,patient_occupation) in cur: #fetch each column data from the cursor 
            pats.append(Patient({"patient_id":patient_id,
                                 "patient_name":patient_name,
                                 "patient_date_of_birth":patient_date_of_birth,
                                 "patient_location":patient_location,
                                 "patient_occupation":patient_occupation
                                 }))
        cur.close()
        cnx.close()
        return pats
    
    @staticmethod
    def fetch_Patient_by_patient_id_from_db(patno):
        cnx = connector.connect(user='root',password='root',
                               database='medicalreports',port=3306)
        
        cur = cnx.cursor()
        cur.execute('select * from pat_data_python where patno='+str(patno))
        
        for (patient_id,patient_name,patient_date_of_birth,patient_location,patient_occupation) in cur:
            pat = Patient({"patient_id":patient_id,
                                 "patient_name":patient_name,
                                 "patient_date_of_birth":patient_date_of_birth,
                                 "patient_location":patient_location,
                                 "patient_occupation":patient_occupation
                                 })
           
        cur.close()
        cnx.close()
        return pat
    
    
        
if __name__ == '__main__':
 
    print(PatientStorage.fetch_patient_id_patno_from_collection(1))
    
    pass 
