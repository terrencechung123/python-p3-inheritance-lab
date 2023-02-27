#!/usr/bin/env python

from user import User
from teacher import Teacher

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name,last_name)
        self.knowledge = []

    def learn(self, knowledge_string):
        return self.knowledge.append(knowledge_string)