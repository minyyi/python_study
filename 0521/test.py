
# def main():
#     name = input("이름을 입력하세요: ")
#     print(f"입력된 이름: {name}")

# if __name__ == "__main__":
#     main()

def main():
    print("테스트 시작")
    count = 0
    while count < 3:
        count += 1
        print(f"반복 {count}번째")
        user_input = input("아무 키나 입력하세요(종료는 q): ")
        print(f"입력값: {user_input}")
        if user_input.lower() == 'q':
            break
    print("테스트 종료")

if __name__ == "__main__":
    main()