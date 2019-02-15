Feature: Patient Management using Flask Application 

Scenario: Get the Patient List from API 
	Given Request for All Patients
	Then Have all Patients available from application
	
Scenario: Add patient Details using API
<<<<<<< HEAD
	Given a set of patients for API
	|patient_id	|patient_name	|patient_date_of_birth	|patient_location|patient_occupation	|
	|1			|John			|19/03/1994				|Leeds			 |Builder				|
=======
	Given a set of Patients for API
	|patient_id	|patient_name	|patient_date_of_birth	|patient_location|patient_occupation
	|1			|John			|19/03/1994				|Leeds			 |Builder
>>>>>>> branch 'master' of https://github.com/joe61081/MedicalSystem.git
	Then increase Patients Count from API
	
Scenario: Get the Patient List from Browser
	Given Request for Patient Home Page
	Then Able to fetch the Patient Count

Scenario: Add Patient Details using Browser
	Given a set of Patients for HTML Form
	|patient_id	|patient_name	|patient_date_of_birth	|patient_location|patient_occupation
	|2			|Bill			|19/03/1995				|York			 |Drummer
	Then increase Patients Count from Browser
	