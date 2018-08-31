class Person:
  def __init__(self,name):
    self.name=name
  def display(self):
    print('name:',self.name)
    print()
  class Dob:
    def __init__(self):
     self.dd=23
     self.mm=03
     self.yy=1995
    def display(self):
     print('Dob={}/{}/{}'.format(self.dd,self.mm,self.yy))

p=Person('bindu')
p.display()
p.Dob().display()
