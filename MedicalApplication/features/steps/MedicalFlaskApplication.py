import behave 
from pip._vendor import requests 
from nose.tools.trivial import ok_ 
from selenium import webdriver


@given("Request for All Patients")
def fetch_pat_from_api(context):
    context.pats = requests.get("http://localhost:7700/patient/example").json()
    
    
@then("Have all Patients available from application")
def check_all_patients_present(context):
    ok_(len(context.pats)>0,"Patients Not Available")

@given("a set of Patients for API")
def post_pat_data_to_API(context):
    context.currentCount = len(requests.get(
        "http://localhost:7700/patient/example").json())
    for row in context.table:
        new_pat = requests.post("http://localhost:7700/patient/create",
                    data={"patient_id":row["patient_id"],
                          "patient_name":row["patient_name"],
                          "patient_date_of_birth":row["patient_date_of_birth"],
                          "patient_location":row["patient_location"],
                          "patient_occupation":row["patient_occupation"]}.json())
        print(new_pat)

@then("increase Patients Count from API")
def check_count_increase(context):
    ok_(context.currentCount<len(requests.get(
        "http://localhost:7700//patient/example").json()), "Patient Registration Failed")
       
@given("Request for Patient Home Page")
def request_patient_home_page(context):
    context.driver =webdriver.Chrome()
    context.driver.get("http://localhost:7700/patient/example")
   
    print(context.countText)

@then("Able to fetch the Patient Count") 
def check_patient_count(context):
    context.driver.save_screenshot("snaps/PatientList.png")
    ok_(len(context.countText)>0,"Patient Count Found")
 

@given("a set of Patients for HTML Form") 
def submit_html_pat_form(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:7700/patient/example")
    context.count_text = context.driver.find_element_by_patient_id("count").text
    for row in context.table:
        context.driver.find_element_by_patient_id("patient_id").send_keys(row["patient_id"]) 
        context.driver.find_element_by_patient_id("patient_name").send_keys(row["patient_name"])
        context.driver.find_element_by_patient_id("patient_date_of_birth").send_keys(row["patient_date_of_birth"])  
        context.driver.find_element_by_patient_id("patient_location").send_keys(row["patient_location"])
        context.driver.find_element_by_patient_id("patient_occupation").send_keys(row["patient_occupation"])
        
        context.driver.save_screenshot("snaps/add_pat_form"+row["patient_id"]+".png") 
        context.driver.find_element_by_patient_id("add-pat").click()
        context.driver.save_screenshot("snaps/add_pat_submit"+row["patient_id"]+".png")

@then("increase Patients Count from Browser")
def check_count_increase_form(context):
    ok_(not (context.count_text == context.driver.find_element_by_patient_id("count").text),"Count Not Changed")
