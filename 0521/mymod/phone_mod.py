# mymod.py

class PhoneInfo:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def show_info(self):
        print(f"이름: {self.name}, 전화번호: {self.phone}")
        
    def to_string(self):
        return f"{self.name},{self.phone}"
    
    @classmethod
    def from_string(cls, data_string):
        """문자열에서 객체를 생성합니다."""
        
        data = data_string.strip().split(',')
        name = data[0]
        phone = data[1]
        return cls(name, phone)


class PhoneBook:
    def __init__(self, filename="phonebook.txt", encoding='utf-8'):
        self.contacts = []
        self.filename = filename
        self.try_load_contacts()
    
    def add_contact(self, contact):
        """연락처를 추가하고 파일에 저장합니다."""
        self.contacts.append(contact)
        self.save_to_file()
        return True
    
    def remove_contact(self, index):
        """인덱스로 연락처를 삭제합니다."""
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            self.save_to_file()
            return True
        return False
    
    def save_to_file(self):
        """모든 연락처를 파일에 저장합니다."""
        with open(self.filename, 'w', encoding='utf-8') as file:
            for contact in self.contacts:
                file.write(contact.to_string() + "\n")
    
    def try_load_contacts(self):
        """파일에서 연락처를 로드합니다. 파일이 없으면 무시합니다."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                for line in file:
                    if line.strip():  # 빈 줄 무시
                        self.contacts.append(PhoneInfo.from_string(line))
            return len(self.contacts)
        except FileNotFoundError:
            return 0
    
    def show_all_contacts(self):
        """모든 연락처를 출력합니다."""
        if not self.contacts:
            print("연락처가 없습니다.")
            return False
            
        print("\n=== 연락처 목록 ===")
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}번. ", end="")
            contact.show_info()
        print("\n==================\n")
        return True
    
    def search_by_name(self, name):
        """이름으로 연락처를 검색합니다."""
        results = []
        for contact in self.contacts:
            if name.lower() in contact.name.lower():
                results.append(contact)
        return results
    
    def search_by_phone(self, phone):
        """전화번호로 연락처를 검색합니다."""
        results = []
        for contact in self.contacts:
            if phone in contact.phone:
                results.append(contact)
        return results
    
    def get_contact_count(self):
        """저장된 연락처 수를 반환합니다."""
        return len(self.contacts)