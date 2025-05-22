# PhoneInfo
#CRUD

# 1. 추가
# 2. 조회
#     2-1 전체조회
#     2-2 검색
# 3. 수정
# 4. 삭제
# 5. 종료

# -*- coding: utf-8 -*-
import sys
import io
import time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# print("한글 텍스트", flush=True)
from mymod.phone_mod import PhoneInfo, PhoneBook

def display_menu():
    """메인 메뉴를 표시합니다."""
    print("\n=== 전화번호부 관리 시스템 ===")
    print("1. 연락처 추가")
    print("2. 모든 연락처 보기")
    print("3. 이름으로 검색")
    print("4. 전화번호로 검색")
    print("5. 연락처 삭제")
    print("0. 종료")
    print("===========================")
    # return input("원하는 메뉴를 선택하세요: ")
    while True:
        try:
            choice = input("원하는 메뉴를 선택하세요(숫자만 입력): ")
            # 숫자만 허용
            if choice.isdigit() and 0 <= int(choice) <= 5:
                return choice
            print("잘못된 입력입니다. 0-5 사이의 숫자를 입력하세요.")
        except:
            print("입력 오류가 발생했습니다. 다시 시도하세요.")

def add_contact(phonebook):
    """새 연락처를 추가합니다."""
    print("\n=== 새 연락처 추가 ===")
    while True:
        try:
            name = input("이름: ")
            if name.strip():  # 이름이 공백이 아닌 경우
                break
            print("이름을 입력해주세요.")
        except EOFError:
            print("\n입력 오류가 발생했습니다. 다시 시도해주세요.")
        except KeyboardInterrupt:
            print("\n연락처 추가가 취소되었습니다.")
            return
    
    # 전화번호 입력 반복
    while True:
        try:
            phone = input("전화번호: ")
            if phone.strip():  # 전화번호가 공백이 아닌 경우
                break
            print("전화번호를 입력해주세요.")
        except EOFError:
            print("\n입력 오류가 발생했습니다. 다시 시도해주세요.")
        except KeyboardInterrupt:
            print("\n연락처 추가가 취소되었습니다.")
            return
    
    # 연락처 추가
    try:
        contact = PhoneInfo(name, phone)
        if phonebook.add_contact(contact):
            print(f"\n{name}님의 연락처가 성공적으로 추가되었습니다.")
        else:
            print("\n연락처 추가에 실패했습니다.")
    except Exception as e:
        print(f"\n연락처 추가 중 오류가 발생했습니다: {e}")
        retry = input("\n다시 시도하시겠습니까? (y/n): ").strip().lower()
        if retry == 'y':
            add_contact(phonebook)  # 재귀적으로 다시 시도
        else:
            print("\n연락처 추가를 취소하고 메인 메뉴로 돌아갑니다.")
            return  # 명시적으로 함수 종료, 메인 메뉴로 돌아감
    # try:
    #     name = input("이름: ")
    #     phone = input("전화번호: ")
        
    #     contact = PhoneInfo(name, phone)
    #     if phonebook.add_contact(contact):
    #         print(f"\n{name}님의 연락처가 성공적으로 추가되었습니다.")
    #     else:
    #         print("\n연락처 추가에 실패했습니다.")
    # except EOFError:
    #     # 입력 오류 시 샘플 데이터 추가
    #     contact = PhoneInfo("샘플 이름", "010-0000-0000")
    #     phonebook.add_contact(contact)
    #     print("\n샘플 연락처가 추가되었습니다. (입력 오류로 인해)")

def search_by_name(phonebook):
    """이름으로 연락처를 검색합니다."""
    try:
        search_name = input("\n검색할 이름을 입력하세요: ")
    except EOFError:
        search_name = ""
        print("입력 오류. 모든 이름을 검색합니다.")
        
    results = phonebook.search_by_name(search_name)
    
    if not results:
        print(f"\n'{search_name}'에 해당하는 연락처를 찾을 수 없습니다.")
        return
    
    print(f"\n=== '{search_name}' 검색 결과 ({len(results)}건) ===")
    for i, contact in enumerate(results, 1):
        print(f"\n결과 {i}:")
        contact.show_info()
    print("=================================")

def search_by_phone(phonebook):
    """전화번호로 연락처를 검색합니다."""
    try:
        search_number = input("\n검색할 전화번호를 입력하세요: ")
    except EOFError:
        search_number = ""
        print("입력 오류. 모든 번호를 검색합니다.")
        
    results = phonebook.search_by_phone(search_number)
    
    if not results:
        print(f"\n'{search_number}'에 해당하는 연락처를 찾을 수 없습니다.")
        return
    
    print(f"\n=== '{search_number}' 검색 결과 ({len(results)}건) ===")
    for i, contact in enumerate(results, 1):
        print(f"\n결과 {i}:")
        contact.show_info()
    print("=====================================")

def remove_contact(phonebook):
    """연락처를 삭제합니다."""
    if not phonebook.show_all_contacts():
        return
    
    try:
        index = int(input("\n삭제할 연락처 번호를 입력하세요: ")) - 1
        if phonebook.remove_contact(index):
            print("\n연락처가 성공적으로 삭제되었습니다.")
        else:
            print("\n유효하지 않은 번호입니다. 다시 시도해 주세요.")
    except (ValueError, EOFError):
        print("\n유효한 숫자를 입력해 주세요.")

def main():
    """메인 프로그램 실행 함수"""
    phonebook = PhoneBook()
    loaded_contacts = phonebook.get_contact_count()
    
    if loaded_contacts > 0:
        print(f"전화번호부가 로드되었습니다. {loaded_contacts}개의 연락처가 있습니다.")
    else:
        print("새 전화번호부를 시작합니다.")
    
    # start_time = time.time()
    # timeout = 60  # 60초 후 자동 종료
    
    while True:
        # 타임아웃 체크
        # if time.time() - start_time > timeout:
        #     print("\n시간 초과로 프로그램을 종료합니다.")
        #     break
        choice = display_menu()
        
        if choice == '1':
            add_contact(phonebook)
        elif choice == '2':
            phonebook.show_all_contacts()
        elif choice == '3':
            search_by_name(phonebook)
        elif choice == '4':
            search_by_phone(phonebook)
        elif choice == '5':
            remove_contact(phonebook)
        elif choice == '0':
            print("\n프로그램을 종료합니다. 감사합니다!")
            break
        else:
            print("\n잘못된 선택입니다. 다시 시도해 주세요.")

# 메인 함수 실행
if __name__ == "__main__":
    main() 