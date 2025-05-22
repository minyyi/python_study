class PhoneInfo:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def show_info(self):
        print(f"이름: {self.name}, 전화번호: {self.phone}")
        
    def to_string(self):
        return f"{self.name}, {self.phone}"
    
    