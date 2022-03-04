#WAP to perform addition using inheritance

'''class addd:
       def __init__(self):
              self.no1=int(input("Enter the first number: "))
class perform(addd):
       def __init__(self):
              super().__init__()
              self.no2=int(input("Enter the second number: "))
       def show(self):
              c=self.no1+self.no2
              print("Addition is: ", c)
p1=perform()
p1.show()
'''

class addd:
       def __init__(self,n):
              self.a=n
class perform(addd):
       def __init__(self,m1,n):
              super().__init__(n)
              self.b=m1
       def show(self):
              c=self.a+self.b
              print("Addition is: ",c)
p1=perform(10,20)
p1.show()
