class SSC :
    def __init__(self, id, board, result) -> None:
        self.ssc_id = id
        self.ssc_board = board
        self.ssc_result = result

class HSC : 
    def __init__(self, id, board, result) -> None:
        self.hsc_id = id
        self.hsc_board = board
        self.hsc_result = result

class UnderGrad : 
    def __init__(self, id, varsity, cgpa) -> None:
        self.uni_id = id
        self.uni_name = varsity
        self.uni_cgpa = cgpa
    
class Student (SSC, HSC, UnderGrad) :
    def __init__(self, name, hometown, ssc_id, hsc_id, uni_id, ssc_board, hsc_board, ssc_result, hsc_result, varsity, cgpa) -> None:
        self.name = name
        self.hometown = hometown
        SSC.__init__(self, ssc_id, ssc_board, ssc_result) 
        HSC.__init__(self, hsc_id, hsc_board, hsc_result)
        UnderGrad.__init__(self, uni_id, varsity, cgpa)

    def __repr__(self) -> str:
        print('----------- SSC -----------')
        print(f'Name : {self.name} \nId : {self.ssc_id} \nBoard : {self.ssc_board} \nGPA : {self.ssc_result}')

        print('----------- HSC -----------')
        print(f'Name : {self.name} \nId : {self.hsc_id} \nBoard : {self.hsc_board} \nGPA : {self.hsc_result}')

        print('----------- UnderGrad -----------')
        print(f'Name : {self.name} \nId : {self.uni_id} \nUnivarsity : {self.uni_name} \nCGPA : {self.uni_cgpa}')

        return 'Thank You'


asad = Student('Asaduzzaman', 'Rajshahi', '11773223', '2877677', '11703066', 'Rajshahi', 'Dhaka', '5.00', '4.94', 'DU', '3.56' )

# print(asad)


rashed = Student('Rasheduzzaman', 'Chittagong', '11775225', '2897675', '11705026', 'Chittagong', 'Dhaka', '5.00', '5.00', 'BUET', '3.76' )

print(rashed)