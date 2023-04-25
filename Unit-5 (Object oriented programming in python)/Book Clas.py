class Book:
    def get_Book_details(self):
        self.bookId=int(input("Enter Book ID:"))
        self.bookName=input("Enter Book Name:")
        self.bookPrice=float(input("Enter Book Price:"))
    def disp_book_details(self):
        print(self.bookId,"\t",self.bookName,"\t",self.bookPrice)

b1 = Book()
b2 = Book()
b1.get_Book_details()
b2.get_Book_details()
print("******** BOOK SHOP ********")
print("ID\tNAME\tPRICE")
print("---------------------------")
b1.disp_book_details()
b2.disp_book_details()