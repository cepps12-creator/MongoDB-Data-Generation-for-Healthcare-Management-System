Last login: Sun Apr  5 19:25:46 on ttys001
crissaepps@Crissas-MacBook-Pro ~ % python3
Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from faker import Faker
>>> import pandas as pd
>>> import random
>>> import uuid
>>> from pathlib import Path
>>> N_PATIENTS = 30000
>>> N_DOCTORS = 10000
>>> N_APPTS = 50000
>>> SEED = NONE
Traceback (most recent call last):
  File "<python-input-8>", line 1, in <module>
    SEED = NONE
           ^^^^
NameError: name 'NONE' is not defined. Did you mean: 'None'?
>>> SEED = None
>>> if SEED is not None:
...     random.seed(SEED)
... 
>>> fake = Faker()
>>> SPECIALTIES = [
...     "Cardiology", "Dermatology", "Neurology", "Oncology",
...     "Pediatrics", "Orthopedics", "General Medicine"
... ]
>>> STATUSES = ["Scheduled", "Completed", "Cancelled", "Pending"]
>>> def maybe(value, p_missing=0.2):
...     """Return value or None with probability p_missing."""
...     
>>> return value if random.random() > p_missing else None
  File "<python-input-15>", line 1
    return value if random.random() > p_missing else None
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: 'return' outside function
>>> def maybe(value, p_missing=0.2):
...     """Return value or None with probability p_missing."""
...     return value if random.random() > p_missing else None
...     
>>> out_dir = Path("data")
>>> out_dir.mkdir(parents=True, exist_ok=True)
>>> patients = []
>>> for _ in range(N_PATIENTS):
...     patients.append({
...         "patient_id": str(uuid.uuid4()),           
ur domain ID)
...         "name": fake.name(),
...         "age": random.randint(1, 90),
...         "gender": random.choice(["Male", "Female"]),
...         "phone_number": maybe(fake.phone_number(), p_missing=0.2), 
missing 
...         "medical_history": maybe(fake.sentence(), p_missing=0.3) 
missing   
...     })
...     
>>> df_patients = pd.DataFrame(patients)
>>> df_patients.to_csv(out_dir / "patients.csv", index=False)
>>> doctors = []
>>> for _ in range(N_DOCTORS):
...     doctors.append({
...         "doctor_id": str(uuid.uuid4()),              
ur domain ID)
...         "name": fake.name(),
...         "specialty": random.choice(SPECIALTIES),
...         "experience_years": random.randint(1, 40)   
...     })
...     
>>> df_doctors = pd.DataFrame(doctors)
>>> df_doctors.to_csv(out_dir / "doctors.csv", index=False)
>>> patient_ids = [p["patient_id"] for p in patients]
>>> doctor_ids  = [d["doctor_id"]  for d in doctors]
>>> appointments = []
>>> for _ in range(N_APPTS):
...     appointments.append({
...         "appointment_id": str(uuid.uuid4()),       
ur domain ID)
...         "patient_id": random.choice(patient_ids),   
s.csv patient_id
...         "doctor_id": random.choice(doctor_ids),     
.csv doctor_id
...         "status": random.choice(STATUSES)
...     })
... 
>>> df_appts = pd.DataFrame(appointments)
>>> df_appts.to_csv(out_dir / "appointments.csv", index=False)
>>> print("Generated CSV files in ./data")
Generated CSV files in ./data
>>> print(f" patients.csv rows: {len(df_patients)}")
 patients.csv rows: 30000
>>> print(f" doctors.csv rows: {len(df_doctors)}")
 doctors.csv rows: 10000
>>> print(f" appointments.csv rows: {len(df_appts)}")
 appointments.csv rows: 50000
