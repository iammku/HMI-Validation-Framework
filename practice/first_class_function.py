class EventDispatcher:
    def dispatch(self, event):
        event()

def brake():
    print("Brake Applied")

dispatcher = EventDispatcher()
dispatcher.dispatch(brake)

"""
1. What is stored in event ?
#Ans: function
2. Which function actually execute at event ?
#Ans: brake()
3. Why to you pass brake and not brake() to dispatch() ?
#Ans: brake = pass the function object
brake() = Execute the function
"""