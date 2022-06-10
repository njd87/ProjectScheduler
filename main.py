from datetime import date, timedelta
from event import Event, DayCollector

def assignEventsToDates(start, end, events, algorithms="basic"):
    global datesAndEvents
    totalSubsteps = 0
    for e in events:
        totalSubsteps += e.getSubSteps()
    
    # assigns events based off of max rest days between subevents
    if algorithms == "basic":
        timeDifference = end.getDate() - start.getDate()
        optimalSepatartion = ((timeDifference.days) - 1) // totalSubsteps
        
        # load all substeps into array:
        totalSubs = []

        for event in events:
            a = event.popEvent()
            while a != "No more events":
                totalSubs.append(a)
                a = event.popEvent()

        for i in range(timeDifference.days + 1):
            if i % optimalSepatartion == 0:
                try:
                    datesAndEvents[list(datesAndEvents.keys())[i]] = totalSubs.pop()
                except:
                    return 0



def main():
    global datesAndEvents
    # collect beginning and end dates
    startingDate = DayCollector("starting day")
    endingDate = DayCollector("ending day")
    startingDate.collectDay()
    endingDate.collectDay()
    timeDifference = endingDate.getDate() - startingDate.getDate()
    
    middleDates = []
    pc1 = startingDate.getDate()
    for i in range(timeDifference.days + 1):
        middleDates.append(startingDate.getDate() + timedelta(days=i))
    
    datesAndEvents = {}
    for d in middleDates:
        datesAndEvents[d] = "Free Day :)"
    
    # need to find a way for users to easily input events and sub events
    # in the meantime I will have temporary placeholders

    # VERSION ALPHA 1.0
    # All events are treated as one kind of event
    # This type of event can be separated
    # Each event has same priority level and the same end-date
    # Goal: Have each subgoal completed on some date
        # Each main goal is then necessarily completed before end-date

    event1 = Event("Finish painting")
    event2 = Event("Get money for that vacation I wanted")

    event1.addStep("Paint layer 1")
    event1.addStep("Paint layer 2")
    event1.addStep("Paint layer 3")

    event2.addStep("Work job 1")
    event2.addStep("Work job 2")
    event2.addStep("Word job 3")

    
    assignEventsToDates(startingDate, endingDate, [event1, event2])

    print(datesAndEvents)

    # for (d, e) in datesAndEvents:
    #     print("Step {0} on {1}".format(d, e))



if __name__ == "__main__":
    main()