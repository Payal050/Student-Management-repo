import streamlit as st
import pandas as pd

from backend import add_student
from backend import get_students
from backend import update_student
from backend import delete_student

st.set_page_config(page_title="Student Database", page_icon="🎓")

st.title("🎓 Student Database Management System")

menu = st.sidebar.selectbox(
    "Menu",
    (
        "Add Student",
        "Show Students",
        "Update Student",
        "Delete Student"
    )
)

# ---------------- Add ----------------

if menu == "Add Student":

    st.header("Add Student")

    roll = st.text_input("Roll Number")
    name = st.text_input("Name")
    age = st.number_input("Age", 1, 100)
    course = st.text_input("Course")

    if st.button("Add"):

        if add_student(roll, name, age, course):
            st.success("Student Added Successfully")

        else:
            st.error("Roll Number Already Exists")


# ---------------- Show ----------------

elif menu == "Show Students":

    st.header("Student Records")

    data = get_students()

    if len(data) == 0:
        st.warning("No Records Found")

    else:
        df = pd.DataFrame(data)
        st.dataframe(df)


# ---------------- Update ----------------

elif menu == "Update Student":

    st.header("Update Student")

    roll = st.text_input("Roll Number")

    name = st.text_input("New Name")

    age = st.number_input("New Age", 1, 100)

    course = st.text_input("New Course")

    if st.button("Update"):

        if update_student(roll, name, age, course):
            st.success("Student Updated Successfully")

        else:
            st.error("Student Not Found")


# ---------------- Delete ----------------

elif menu == "Delete Student":

    st.header("Delete Student")

    roll = st.text_input("Roll Number")

    if st.button("Delete"):

        if delete_student(roll):
            st.success("Student Deleted Successfully")

        else:
            st.error("Student Not Found")
