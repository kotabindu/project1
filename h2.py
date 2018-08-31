class Car:
   def __init__(self,name,model,color):
      self.name=name
      self.model=model
      self.color=color
   def getinfo(self):
      print('car name: {},model: {},color: {}'.format(self.name,self.model,self.color)

class Employe:
   def __init__(self,ename,eno,car):
       self.ename=ename
       self.eno=eno
       self.car=car
   def empinfo(self):
       print('emp name',self.ename)
       print('emp num',self.eno)
       print('emp car info')
       self.car.getinfo()
c=Car('Innova','2.5z','grey')
e=Employe('hey','1',c)
e.empinfo()
