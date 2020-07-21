from abc import ABCMeta,abstractmethod
class Shape(metaclass = ABCMeta):
    def __init__(self,line_color,line_width,line_height):
        self.line_color = line_color
        self.line_width = line_width
        self.line_height = line_height
        print("Shape constructor")
    
    @abstractmethod    
    def calculate_area(self):
        pass
    
    @abstractmethod 
    def check(self):
        pass
    
class Triangle(Shape):
  
    def calculate_area(self):
        print("1/2*base*height")
        
    def sample(self):
        print("Sample method!")
        
   
        
        
class Square(Shape):
    def calculate_area(self):
        print("side*side")
        

ref =  Triangle("Red",5,4)

        
'''



1. Abstract class is one which has atleast one abstract method
2. Abstarct method is one which has a method signature but no implementation/definition
3. Abstract classes(metaclass attribute present) CANNOT be instantiated
4. Abstract classes(metaclass attribute is NOT present) SHOULD NOT be instantiated
5. It is NOT mandatory for the derive classes to override the abstract methods of the base class.
If the derived classes don't override the abstract method(s) then it(derived) would become abstract
6. Why do we need abstract methods though it would not have a definition?
    6.1 To achieve overriding there by  polymorphism there by better performance
    6.2 To achieve a standardization. A decision to make whom to allow and whom not to allow inside the family'''