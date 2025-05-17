#Simple Healthcare Diagnostic & Management System

import datetime

#Dummy data for diagnosis

diagnosis_db = {

("fever", "cough", "fatigue"): "You may have the Flu.",

chest pain", "shortness of breath", "dizziness"): "You may be experiencing heart-related issues.",

(" ("headache", "nausea", "blurred vision"): "Possible Migraine.",

("abdominal pain", "diarrhea", "vomiting"): "You may have a stomach infection."

#Storage for patient records

patient_records {}

Function to diagnose

def diagnose (symptoms):

for key_symptoms, condition in diagnosis_db.items():

if all (symptom in symptoms for symptom in key_symptoms):

return condition

return "Condition not recognized. Please consult a doctor."

#Function to store patient record

def store_patient_record (name, age, symptoms, diagnosis):

patient_id = len (patient_records) + 1

patient_records [patient_id] = {

"Name": name,

"Age": age,

"Symptoms": symptoms,

"Diagnosis": diagnosis,

"Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

}

print (f"\nRecord saved successfully with Patient ID: (patient_id)")

#Function to view all records

def view records():

if not patient records:

print("No records found.")

return

for pid, info in patient_records.items():

print (f"\nPatient ID: {pid)")
#Function to view all records

def view_records():

if not patient_records:

print("No records found.")

return

for pid, info in patient_records.items():

print (f"\nPatient ID: {pid)")

for key, value in info.items():

print (f" (key): (value)")

#Main program

def main():

while True:

print("\n--Healthcare Diagnostic & Management ----")

print("1. Diagnose Symptoms")

print("2. View Patient Records")

print("3. Exit")

choice input("Enter your choice: ")

if choice == "1":

name input ("Enter Patient Name: ")

age input ("Enter Age: ")

symptoms input ("Enter symptoms separated by commas: ").lower().split(',')

symptoms [s.strip() for s in symptoms]

diagnosis diagnose (symptoms)

print (f"\nDiagnosis: (diagnosis)")

store_patient_record (name, age, symptoms, diagnosis)

elif choice == "2":

view_records ()

elif choice == "3":

print("Exiting system. Stay healthy!")

break

else:

print("Invalid choice. Try again.")

If name ==" main":

main()