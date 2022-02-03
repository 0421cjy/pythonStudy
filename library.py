import random
import os

## 도서관 클래스
## 회원 등록, 회원 정보 변경, 회원 삭제, 도서 정보 등록, 도서 정보 변경, 도서 정보 삭제, 도서 대출, 도서 반납 기능

class Member:
    member_id = ""
    member_name = ""
        
    def __init__(self, id, name):
        self.member_id = id
        self.member_name = name
        
    def update_member_data(self, name):
        self.member_name = name
        
class Book:
    book_id = ""
    book_name = ""
    book_author = ""
    book_member_id = ""
        
    def __init__(self, id, name, author):
        self.book_id = id
        self.book_name = name
        self.book_author = author
        
    def update_member_id(self, member_id):
        self.book_member_id = member_id
        
    def update_book_data(self, name, author):
        self.book_name = name
        self.book_author = author
        
class Library:
    member_list = []
    book_list = []
        
    def regist_member(self, name):
        id_key = random.randint(65,90)
        string_key = chr(id_key)
        string_key += str(random.randint(100000,999999))
        
        new_member = Member(string_key, name)
        self.member_list.append(new_member)
        print("--회원 추가가 성공하였습니다.--")
        
    def regist_member_from_file(self, id, name):
        new_member = Member(id, name)
        self.member_list.append(new_member)
        print("--회원 추가가 성공하였습니다.--")
        
    def remove_member(self, id):
        for member in self.member_list:
            if member.member_id == id:
                self.member_list.remove(member)
                print("--회원 제거가 성공하였습니다.--")
                return
            
        print("--not exists id--")
        
    def update_member(self, id, name):
        for member in self.member_list:
            if member.member_id == id:
                member.member_name = name
                print("--회원 정보 변경이 성공하였습니다.--")
                print(member.member_id, member.member_name)
                return
            
        print("--존재하지 않는 회원 아이디입니다.--")
        
    def show_memberlist(self):
        print("--회원 정보 리스트 출력--")
        
        for member in self.member_list:
            print(member.member_id, member.member_name)
            
        print("\n")
        
    def write_member_list(self, file):
        for member in self.member_list:
            input_data = str(member.member_id) + " " + str(member.member_name)
            file.write(input_data)
        
    def read_member_list(self, file):
        
        lines = file.readlines()
        
        for line in lines:
            list = line.split()
            self.regist_member_from_file(list[0], list[1])
            
    def regist_book(self, name, author):
        id_key = random.randint(65,90)
        string_key = str(random.randint(100000,999999)) 
        string_key += chr(id_key)
        
        new_book = Book(string_key, name, author)
        self.book_list.append(new_book)
        
    def regist_book_from_file(self, id, name, author):
        new_book = Book(id, name, author)
        self.book_list.append(new_book)
        
    def remove_book(self, id):
        for book in self.book_list:
            if book.book_id == id:
                self.book_list.remove(book)
                print("--도서 제거가 성공하였습니다--")
                return
            
        print("--존재하지 않는 도서 아이디입니다.--")
        
    def update_book(self, id, name, author):
        for book in self.book_list:
            if book.book_id == id:
                book.book_name = name
                book.book_author = author
                print("--도서 정보 변경이 성공하였습니다.--")
                print(book.book_id, book.book_name, book.book_author)
                return
            
        print("--존재하지 않는 도서 아이디입니다.--")
        
    def show_book_list(self):
        print("--도서 정보 리스트 출력--")
        
        for book in self.book_list:
            print(book.book_id, book.book_name, book.book_author)
            
        print("\n")
        
    def write_book_list(self, file):
        for book in self.book_list:
            input_data = str(book.book_id) + " " + str(book.book_name) + " " + str(book.book_author)
            file.write(input_data)
        
    def read_book_list(self, file):
        
        lines = file.readlines()
        
        for line in lines:
            list = line.split()
            self.regist_book_from_file(list[0], list[1], list[2])
        
if __name__ == "__main__":
    
    library = Library()
    
    book_path = os.getcwd() + "\\book_data.txt"
    member_path = os.getcwd() + "\\member_data.txt"
    
    try:
        book_file = open(book_path, "r", encoding="utf-8")
        library.read_book_list(book_file)
    except FileNotFoundError as e:
        print(e)
    
    try:
        member_file = open(member_path, "r", encoding="utf-8")
        library.read_member_list(member_file)
    except FileNotFoundError as e:
        print(e)
    
    while True:
        print("1. 회원 등록")
        print("2. 회원 정보 삭제")
        print("3. 회원 정보 변경")
        print("4. 회원 목록 조회")
        print("5. 도서 등록")
        print("6. 도서 정보 삭제")
        print("7. 도서 정보 변경")
        print("8. 도서 목록 조회")
        print("9. 종료")
        
        input_value = input("원하는 메뉴를 입력해주세요. \n >>>")
        
        if input_value == '1':
            input_name = input("신규 회원의 이름을 입력해주세요. \n >>>")
            library.regist_member(input_name)
        elif input_value == '2':
            input_id = input("삭제할 회원의 아이디를 입력해주세요. \n >>>")
            library.remove_member(input_id)
        elif input_value == '3':
            input_id = input("변경할 회원의 아이디를 입력해주세요. \n >>>")
            input_name = input("변경할 회원의 이름을 입력해주세요. \n >>>")
            library.update_member(input_id, input_name) 
        elif input_value == '4':
            library.show_memberlist()
        elif input_value == '5':
            input_name = input("신규 도서의 이름을 입력해주세요. \n >>>")
            input_author = input("변경할 도서의 저자를 입력해주세요. \n >>>")
            library.regist_book(input_name, input_author)
        elif input_value == '6':
            input_id = input("삭제할 도서의 아이디를 입력해주세요. \n >>>")
            library.remove_book(input_id)
        elif input_value == '7':
            input_id = input("변경할 도서의 아이디를 입력해주세요. \n >>>")
            input_name = input("변경할 도서의 이름을 입력해주세요. \n >>>")
            input_author = input("변경할 도서의 저자를 입력해주세요. \n >>>")
            library.update_book(input_id, input_name, input_author) 
        elif input_value == '8':
            library.show_book_list()
        elif input_value == '9':
            break
    
    book_file = open(book_path, "w", encoding="utf-8")
    library.write_book_list(book_file)
    
    book_file.close()
    
    member_file = open(member_path, "w", encoding="utf-8")
    library.write_member_list(member_file)
    
    member_file.close()