from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["StudentDB"]
collection = db["students"]


# Add Student
def add_student(roll_no, name, age, course):

    if collection.find_one({"roll_no": roll_no}):
        return False

    collection.insert_one({
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "course": course
    })

    return True


# Show Students
def get_students():

    students = []

    for student in collection.find({}, {"_id": 0}):
        students.append(student)

    return students


# Update Student
def update_student(roll_no, name, age, course):

    result = collection.update_one(
        {"roll_no": roll_no},
        {
            "$set": {
                "name": name,
                "age": age,
                "course": course
            }
        }
    )

    return result.modified_count > 0


# Delete Student
def delete_student(roll_no):

    result = collection.delete_one({"roll_no": roll_no})

    return result.deleted_count > 0
