class CPU : 
    def __init__(self, brand, cores) -> None:
        self.cpu_brand = brand
        self.cores = cores

class RAM : 
    def __init__(self, brand, size) -> None:
        self.ram_brand = brand
        self.size = size

class HDD : 
    def __init__(self, brand, capacity) -> None:
        self.hdd_brand = brand
        self.capacity = capacity

# Computer have CPU, RAM, HDD
class Computer : 
    def __init__(self, cpu_brand, cores, ram_brand, size, hdd_brand, capacity) -> None:
        self.cpu = CPU(cpu_brand, cores)
        self.ram = RAM(ram_brand, size)
        self.hdd = HDD(hdd_brand, capacity)
    
    def __repr__(self) -> str:
        print('------------ YOUR PC ------------')
        print(f'CPU Manufactured by {self.cpu.cpu_brand}, having {self.cpu.cores} cores')
        print(f'RAM Manufactured by {self.ram.ram_brand}, having {self.ram.size} GB size')
        print(f'HDD Manufactured by {self.hdd.hdd_brand}, having {self.hdd.capacity} GB capacity')
        return 'THANK YOU'

pc = Computer('Ryzen', 16, 'Transcend', 8, 'Seagate', 512)
print(pc)