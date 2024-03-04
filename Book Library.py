library= []
wish_library = []
donate_books = []
#السؤال عن الكتاب اللي عنده
owend_book = input("Enter the name of a book you own:").lower()
library.append(owend_book)

#اسئله لو عنده كتاب تاني ولا لا وممكن يعمل سكب للسؤال
choice1 = input("Enter the name of anthor book you own (or press 'Enter' to skip):").lower()
if choice1 != "":
  library.append(choice1)
#اكتب له القايمة بتاعته بتاعت الكتب اللي عنده
print(f"Your book list: {library}")  
#الكتاب اللي عايز تجيبه في المستقبل
wanted_book = input("Enter the name of a book you want:").lower()
wish_library.append(wanted_book)
#لو فيه كتاب تاني عايز تجيبه ولا سكب للسؤال
choice2 = input("Enter the name of anthor book you wish to have (or press 'Enter' to skip)").lower()
if choice2 != "":
  wish_library.append(choice2)
#اكتب له قايمة التمني بتاعته
print(f"Your wish library is: {wish_library} ")

#اسئله عن كتاب عايز يتبرع بيه ولا يعمل سكب
choice3 = input("Enter a good book you want to donate (or press 'Enter' to skip):")
if choice3 in library:
  
  donate_books.append(choice3)
  library.remove(choice3)
# اطبعله قايمته النهائية
print(f"Your finally library is: {library}")