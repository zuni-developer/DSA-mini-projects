class SpecialList:
    
    """A special list with undo/redo operations, preserving insertion order with correct logic."""
    def __init__(self):
        self._list = []
        self.action=[]
        self.type=[]
        self.redo_actions=[]
        self.redo_type=[]
        self.counter=True

    def insert(self, value):
        if value not in self._list:
            self._list.append(value)
        if self.counter:
            self.action.append(value)
            self.type.append("i")
            self.redo_actions.clear()
            self.redo_type.clear()

    def delete(self, value):
        existed = value in self._list
        if existed:
            self._list.remove(value)
            if self.counter:
                self.action.append(value)
                self.type.append("d")
                self.redo_actions.clear()
                self.redo_type.clear()
        else:
                self.type.append(None)
            
    def undo(self):
        if self.action:
            type=self.type.pop()
            if type==None:
                self.type.pop()
                return
            self.counter=False
            temp=self.action.pop()
            if type=="i":
                if temp in self._list:
                    self._list.remove(temp)
                self.redo_actions.append(temp)
                self.redo_type.append("i")
            elif type=="d":
                if temp not in self._list:
                    self._list.append(temp)
                self.redo_actions.append(temp)
                self.redo_type.append("d")
            self.counter=True

    def redo(self):
        if self.redo_actions:
            self.counter=False
            temp=self.redo_actions.pop()
            type=self.redo_type.pop()
            if type=="i":
                if temp not in self._list:
                    self._list.append(temp)
                self.action.append(temp)
                self.type.append("i")
            else:
                if temp in self._list:
                    self._list.remove(temp)
                self.action.append(temp)
                self.type.append("d")
            self.counter=True
            
    def display(self):
        print(self._list)

    def __str__(self):
        return f"SpecialList({self._list})"
