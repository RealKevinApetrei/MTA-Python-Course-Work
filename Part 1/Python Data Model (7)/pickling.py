from datetime import datetime
from copy import deepcopy
import pickle


class Employee:
    def __init__(self, name, title, supervisors):
        self.name = name
        self.title = title
        self.supervisors = supervisors
        self.save_date = "?"

    def __repr__(self):
        return f"<Employee: (name={self.name}, title={self.title}, supervisors={self.supervisors}), save_date={self.save_date}>"

    def __getstate__(self, *args, **kwargs):
        state = deepcopy(self.__dict__)
        del state["supervisors"]
        state["save_date"] = datetime.now()
        print(state)
        return state

    def __setstate__(self, state):
        self.supervisors = []
        for piece in state:
            print("Setting the {} piece to {}".format(piece, state[piece]))
            setattr(self, piece, state[piece])


e = Employee("Kevin", "Programmer", ["...", "..", "."])


# d = pickle.dumps(e)
# b = pickle.loads(d)