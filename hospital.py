from abc import ABC, abstractmethod
class MedicalService(ABC):

    def __init__(self, patient, base_fee):
        self.patient = patient
        self._base_fee = base_fee
        self._paid = 0

    def book_appointment(self):
        print("Appointment booked for", self.patient)

    @abstractmethod
    def calculate_charge(self):
        pass
    
    def make_payment(self, amount):
        if amount > 0:
            self._paid += amount
            print("Payment successful:", amount)
        else:
            print("Invalid payment")

    def summary(self):
        print("\nPatient:", self.patient)
        print("Total Charge:", self.calculate_charge())
        print("Amount Paid:", self._paid)

class GeneralConsultation(MedicalService):

    def calculate_charge(self):
        return self._base_fee

class SpecialistConsultation(MedicalService):

    def calculate_charge(self):
        return self._base_fee + 2000

class LaboratoryService(MedicalService):

    def calculate_charge(self):
        return self._base_fee + 1500

class EmergencyTreatment(MedicalService):

    def calculate_charge(self):
        return self._base_fee + 5000


services = [

    GeneralConsultation("Kamal", 3000),

    SpecialistConsultation("Nimal", 5000),

    LaboratoryService("Amal", 2500),

    EmergencyTreatment("Saman", 7000)
]

for service in services:

    service.book_appointment()

    charge = service.calculate_charge()

    service.make_payment(charge)

    service.summary()
