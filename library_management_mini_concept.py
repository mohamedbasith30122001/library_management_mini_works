#Scope
#Library Class -----> Book availability  | Book issue          | add the book back
#Customer Class ---->                    | Requesting the book | Returning the book

class library:
  def __init__(self,book):
    self.book_list=book

  def  show(self):
    print(self.book_list)

  def borrow(self,book_name):
    if book_name in self.book_list:
      self.book_list.remove(book_name)
      print("thank yoy,book issued")
      return True
    else:
      print("this book is not available")
      return False

  def add_book_back(self,book_name):
    self.book_list.append(book_name)

class customer:
  def __init__(self):
    self.booklist=[]

  def add_book(self,book_name):
    self.booklist.append(book_name)

  def show(self):
    print(self.booklist)

  def requested_book(self):
    print("enter the book")
    self.book=input()
    return self.book

  def returning(self):
    print("may i return the book")
    self.book=input()
    return self.book

  def return_book(self,book_name):
    if book_name in self.booklist:
      self.booklist.remove(book_name)
      print("thankyou for returning sir")
      return True
    else:
      print("you return wrong book plz check your book! ")
      return False

lib_tsi=library(['b1','b2','b3','b4','b3','b0','b7'])
basi=customer()

while True:
  print("select the options")
  print("1 - Show the list of books \n2 - Lend a book \n3 - Customer borrowed books \n4 - returned books to library  \n0 - exit")
  option=int(input())
  if option == 1:
    lib_tsi.show()
  elif option == 2:
    request_book=basi.requested_book()
    sts=lib_tsi.borrow(request_book)
    if sts == True:
      basi.add_book(request_book)
  elif option == 3:
    basi.show()
  elif option == 4:
    returned_book=basi.returning()
    status=basi.return_book(returned_book)
    if status == True:
      add=lib_tsi.add_book_back(returned_book)
  elif option == 0:
    break
