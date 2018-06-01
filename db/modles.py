#!/usr/bin/env python
# -*- coding: utf-8 -*-
from db import handler

class Base:
    @classmethod
    def select_data(cls,name):
        return handler.select_the_data(name,cls.__name__.lower())

    def save_data(self):
        handler.save_the_data(self)


class Admin(Base):
    def registration(self,name,password):
        self.name = name
        self.password = password
        self.save_data()

    def create_school(self,school_name,school_address):
        school = School(school_name, school_address)
        school.save_data()

    def create_teacher(self,name,password):
        teacher = Teacher(name,password)
        teacher.save_data()

    def create_course(self,course_name):
        course = Course(course_name)
        course.save_data()

    def change_password(self,password):
        self.password = password
        self.save_data()

class School(Base):
    def __init__(self,school_name,school_address):
        self.name = school_name
        self.school_address = school_address
        self.course_list = []

    def add_course(self,course_name):
        self.course_list.append(course_name)
        self.save_data()



class Teacher(Base):
    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.course_list = []

    def add_course(self,course_name):
        self.course_list.append(course_name)
        self.save_data()

    def change_student_score(self, student, course_name, score):
        student.scores[course_name] = score
        student.save()
    def change_password(self,password):
        self.password = password
        self.save_data()

class Course(Base):
    def __init__(self, name):
        self.name = name
        self.student_list = []


class Student(Base):
    def __init__(self,name,password):
        self.name = name
        self.password =password
        self.school=None
        self.course_list = []
        self.scores = {}
        self.save_data()

    def choose_school(self,name):
        self.school = name
        self.save_data()

    def choose_course(self,course_name):
        self.course_list.append(course_name)
        self.save_data()

    def change_password(self,password):
        self.password = password
        self.save_data()

















