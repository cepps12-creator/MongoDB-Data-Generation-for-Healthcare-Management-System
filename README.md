# MongoDB-Data-Generation-for-Healthcare-Management-System

Built a MongoDB-based healthcare management system using synthetic data generated with Python’s Faker library. Designed and populated three related collections—Patients, Doctors, and Appointments—using structured CSV files and UUID-based identifiers to simulate realistic healthcare relationships. Implemented one-to-many relationships between patients and doctors through appointment records, ensuring data integrity across collections.

The project focused on NoSQL data modeling, data generation, and querying in MongoDB using mongosh and MongoDB Compass. Performed filtering, projections, logical operators, comparison queries, and existence checks to analyze healthcare data, including patient demographics, doctor specialties, and appointment statuses.

# Skills & Concepts Used

MongoDB (NoSQL database design)

Data generation using Python Faker library

UUID-based unique identifiers

CSV data preparation and import

Collection design and relationships (one-to-many)

MongoDB queries (find, filters, projections)

Logical operators ($and, $or, $in, $exists, $not)

Data validation and schema consistency (implicit)

# Key Features

Generated realistic synthetic healthcare datasets for patients, doctors, and appointments

Modeled relational-style connections in a NoSQL database using referenced IDs

Imported structured CSV data into MongoDB Compass

Performed structured queries for real-world healthcare scenarios

Analyzed patient demographics, doctor expertise, and appointment outcomes

Practiced advanced MongoDB filtering, pagination, and conditional logic

# Example Queries Included 

Filtering patients by age, gender, and missing contact information

Retrieving doctors by specialty and experience level

Querying appointments by status (Scheduled, Completed, Cancelled)

Using pagination and sorting for scalable data retrieval

Checking field existence and handling incomplete data
