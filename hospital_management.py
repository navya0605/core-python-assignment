
class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease
patients = [
    Patient("Alice", 30, "Flu"),
    Patient("Bob", 45, "Diabetes"),
    Patient("Charlie", 35, "Flu")
]
def search_by_disease(patients, disease):
    result = []
    for patient in patients:
        if patient.disease.lower() == disease.lower(): 
            result.append(patient.name)
    return result

search_disease = "Flu"  
patients_with_disease = search_by_disease(patients, search_disease)
print(f"Patients with {search_disease}: {patients_with_disease}")
