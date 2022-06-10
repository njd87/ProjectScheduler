from datetime import date

class Event():
    def __init__(self, name):
        self.name = name
        self.steps = []
    
    def addStep(self, step):
        self.steps.append(step)
    
    def getSubSteps(self):
        return len(self.steps)

    def popEvent(self):
        try:
            return self.steps.pop()
        except:
            return "No more events"

class DayCollector():
    def __init__(self, name):
        self.name = name
        self.day = 0
        self.month = 0
        self.year = 0

    def collectDay(self):
        self.day = int(input("Input the day (number) for {0}: ".format(self.name)))
        self.month = int(input("Input the month (number) for {0}: ".format(self.name)))
        self.year = int(input("Input the year (number) for {0}: ".format(self.name)))
    
    def getDate(self):
        return date(self.year, self.month, self.day)
