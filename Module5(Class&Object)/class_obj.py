class Phone :
    price = 9000
    color = 'purple'
    brand = 'xiomi'

    def call(self) : 
        print("calling...")
    
    def send_sms(self, phn_no, text) : 
        print(f'{phn_no} sends : {text}')


my_phone  = Phone()
my_phone.call()
my_phone.send_sms("01791883658", 'hellow, how are you?')
