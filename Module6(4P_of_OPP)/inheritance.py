class Polygon :
    def __init__(self, no_of_sides) -> None:
        self.no_of_sides = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    
    def input_sides(self) :
        self.sides = [float(input(f'Enter side {i+1} : ')) for i in range(self.no_of_sides)]
    
    def disp_sides(self) :
        for i in range (self.no_of_sides) :
            print(f'side {i+1} : {self.sides[i]}')


class Triangle(Polygon) :
    def __init__(self) -> None:
        super().__init__(3)
    
    def findArea(self) :
        a, b, c = self.sides
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c))

        print(f'Area of the triangle : {area}')


class Square(Polygon) :
    def __init__(self) -> None:
        super().__init__(1)
    
    def findArea(self) : 
        a = self.sides
        area = a**2

        print(f'Area of the Square : {area}')


class Rectangle(Polygon) :
    def __init__(self) -> None:
        super().__init__(2)
    
    def findArea(self) :
        a, b = self.sides
        area = a*b

        print(f'Area of the Rectangle : {area}')


triangle1 = Triangle()
triangle1.input_sides()
triangle1.disp_sides()
triangle1.findArea()

