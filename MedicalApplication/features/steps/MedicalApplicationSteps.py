import behave

from example import Patient
from example.MedicalStorageManager import PatientStorage
from example.Patient import Patient
from nose.tools.trivial import ok_


@given("I load for Patient details")
def read_patient_data(context):
    PatientStorage.add_Patient_to_binary_file(
        Patient({"patient_name":"dave",
            "patient_date_of_birth": "19/04/1994",
            "patient_location": "Leeds",
            "patient_occupation": "Builder"}), "files/pat_data.bin")
    context.pats = PatientStorage.get_patient_from_binary_file("files/pats_data.bin")            

 
@then("I will get the Patient Details") 
def check_patient_count(context):
    ok_(len(context.pats) > 0)("No Patients Found")          

        
@then("Count should increase")
def check_count_increase(context):
    ok_(context.currentCount < context.afterUpdateCount, "Add Employee in Failed")


@given("I load for Patient details from Json File")  
def read_patient_data_from_JSON(context):
    context.emps = PatientStorage.get_patients_from_json("files/emp_data.json")


@given("a set of pats")
def add_new_emps(context):
    context.currentCount = len(PatientStorage.get_patient_from_binary_file("files/pat_data.bin"))
    for row in context.table:
        PatientStorage.add_Patient_to_binary_file(
            Patient({"patient_id":row["patient_id"], "patient_name":row["patient_name"], "patient_date_of_birth":row["patient_date_of_birth"],
                     "patient_location":row["patient_location"], "patient_occupation":row["patient_occupation"]})
            , "files/pat_data.bin")
    context.afterUpdateCount = len(
            PatientStorage.get_patient_from_binary_file("files/pat_data.bin"))


@given("a set of pats for JSON")
def add_new_pats_to_JSON(context):
    context.currentCount = len(PatientStorage.get_patients_from_json("files/pat_data.json"))
    
    for row in context.table:
        PatientStorage.add_patient_to_json({"patient_id":row["patient_id"], "patient_name":row["patient_name"], "patient_date_of_birth":row["patient_date_of_birth"],
                     "patient_location":row["patient_location"], "patient_occupation":row["patient_occupation"]}, "files/pat_data.json")
        
    context.afterUpdateCount = len(Patient.get_patients_from_json("files/pat_data.json")) 

'''
@given("example of Patient to add in table")
def add_patients_to_DB(context):
    context.patientnos = []
    for row in context.table:
        context.patientnos.append(row["patient_id"])
        if(not isinstance(PatientStorage.fetch_all_patients_from_db(row["patient_id"]), Patient)):
            PatientStorage.insert_patient_in_db(
            Patient({"patient_id":row["patient_id"], "patient_name":row["patient_name"], "patient_date_of_birth":row["patient_date_of_birth"],
                     "patient_location":row["patient_location"], "patient_occupation":row["patient_occupation"]}))
'''
'''
@then("the  data could be fetched from table")
def check_pat_in_db(context):
    for patientnos in context.patientnos:
        ok_(isinstance(PatientStorage.fetch_patient_by_patient_id_from_db(patient_id), Patient),
            "Patient Not Found" + str(patient_id))


@given("Querying for Patient Data from Table")
def fetch_all_patients_from_db(context):
    context.pats = PatientStorage.fetch_all_patients_from_db()
 '''

@then("to get the List of All Patient present in table")
def check_patient_fetched(context):
    ok_(((len(context.emps) > 0), "No Patients Found"))  

'''
@given("examples of Patient to add in collection")  
def add_documents_in_patients_collection(context):  
    context.patientnos = []
    for row in context.table:
        context.patietnos.append(row["patient_id"])
        if(not isinstance({PatientStorage.fetch_all_patients_from_collection(row["patient_id"]), Patient)):
            PatientStorage.insert_patient_in_collection(
            Patient({"patient_id":row["patient_id"],
                     "patient_name":row["patient_name"],
                     "patient_date_of_birth":row["patient_date_of_birth"],
                     "patient_location":row["patient_location"],
                     "patient_occupation":row["patient_occupation"]}))


@then("the patient data could be fetched from collection")
def check_pat_in_collection(context):
    for patient_id in context.patientos:
        ok_(isinstance(PatientStorage.fetch_all_patients_from_collection(patient_id), Patient),
            "Patient Not Found: " + str(patient_id))
'''

@given("Querying for Patient Data from Collection")
def fetch_all_patients_documents(context):
    context.patientos = PatientStorage.fetch_all_patients_from_collection()() 

    
@then("to get the list of All patient present in Collection")
def check_patient_fetched_from_collection(context):
    ok_((len(context.emps) > 0), "No patient Found")  

