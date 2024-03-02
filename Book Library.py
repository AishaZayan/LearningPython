library = []
wish_library = []
#السؤال عن الكتاب اللي عنده
owend_book = input("Enter the name of a book you own:").lower()
library.append(owend_book)

#اسئله لو عنده كتاب تاني ولا لا وممكن يعمل سكب للسؤال
choice = input("Enter the name of anthor book you own (or press 'Enter' to skip):").lower()
if choice != '':
  library.append(choice)
    
print(library)

#الكتاب اللي عايز تجيبه في المستقبل
wanted_book = input("Enter the name of the book you wish to have in the future:")
wish_library.append(wanted_book)
  
#لو فيه كتاب تاني عايز تجيبه ولا سكب للسؤال
choice2 = input("Enter the name of anthor book you wish to have (or press 'Enter' to skip):")
if choice2 != '':
  wish_library.append(choice2)
    
#اكتب له قايمة التمني بتاعته
print(f"Your whishlist: {wish_library}")

#اسئله لو فيه كتاب من قايمة التمني عنده ولا لا
    
#اعمله ابدات للقايمة لو قال ان فيه كتاب من التمني عنده
#اسئله عن كتاب عايز يتبرع بيه ولا يعمل سكب
# اطبعله قايمته النهائية
