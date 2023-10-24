#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="name", job="ITC"):
        self.setName(name);
        self.setJob(job);
    
    def setName(self, val):
        if (val == None):
            print("Name must be string between 1 and 25 characters.");
        elif (type(val) == str and len(val) > 1 and len(val) < 25):
            self.name = val.title();
        else: print("Name must be string between 1 and 25 characters.");
    
    def getName(self):
        return self.name;

    def setJob(self, val):
        if (val == None or val not in APPROVED_JOBS):
            print("Job must be in list of approved jobs.");
        else: self.job = val;
    
    def getJob(self):
        return self.job;
