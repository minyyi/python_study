class PhoneBook:
    def __init__(self, filename="phonebook.txt"):
        self.contacts = []
        self.filename = filename
        self.load_contacts()
    
    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_to_file()
        return True
        # contact = PhoneInfo(name, phone)
        # self.contacts.append(contact)
        # print(f"Contact {name} added.")
    def remove_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            self.save_to_file()
            return True
        return False
        # if 0 <= index < len(self.contacts):
        #     removed_contact = self.contacts.pop(index)
        #     print(f"Removed contact: {removed_contact.name}")
        #     self.save_to_file()
        # else:
        #     print("Invalid index. No contact removed.")
        
    def try_load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    if line.strip():  # 빈 줄 무시
                        self.contacts.append(PhoneInfo.from_string(line))
            return len(self.contacts)
        except FileNotFoundError:
            return 0
        # try:
        #     with open(self.filename, "r") as file:
        #         for line in file:
        #             name, phone = line.strip().split(", ")
        #             contact = PhoneInfo(name, phone)
        #             self.contacts.append(contact)
        # except FileNotFoundError:
        #     print(f"File {self.filename} not found. Starting with an empty contact list.")
        # except Exception as e:
        #     print(f"An error occurred while loading contacts: {e}")
        # results = []
        # for contact in self.contacts:
        #     if contact.name == name:
        #         results.append(contact)
        # return results
        
        
    def search_by_name(self, name):
        results = []
        for contact in self.contacts:
            if contact.name == name:
                results.append(contact)
        return results
                
        # results = [contact for contact in self.contacts if contact.name == name]
        # return results
        
    def search_by_phone(self, phone):
        results = []
        for contact in self.contacts:
            if contact.phone == phone:
                results.append(contact)
        return results
        # results = [contact for contact in self.contacts if contact.phone == phone]
        # return results
        
    def get_contact_count(self):
        """저장된 연락처 수를 반환합니다."""
        return len(self.contacts)