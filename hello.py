class Human:
     def __init__(self):
     self.name='bindu'
     self.head=self.Head()
     def display(self):
        print 'hello',self.name'
     class Head:
        def talk(self):
            print'talking'
h=Human()
h.display()
h.head.talk()

