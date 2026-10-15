from .validation import validate_author, validate_name, validate_year
books=[]
def add_book(name, author,year):
    if not validate_name(name) or not validate_year(year) or not validate_author(author):
        print("Kitab məlumatları düzgün deyil")
    book={
        "name": name,
        "author": author,
        "year": year
    }
    books.append(book)
def show_books():
    for book in books:
        print(f"{book['name']} | {book['author']} | {book['year']}")
def search_book_by_name():
    axtarilan_ad = input("kitabini qeyd edin:")
    found=False
    for item in books:
        if item['name']==axtarilan_ad:
            print(item)
            found=True
    if not found:
        print("Kitab tapilmadi")
def search_book_by_author():
    axt_muellif=input("Muellifi daxil edin:")
    tapildi=False
    for items in books:
        if items["author"]==axt_muellif:
            print(items)
            tapildi=True
    if not tapildi:
        print("Bu muellife aid olan hech bir kitab tapilmadi")
def remove_book():
    delit_book=input("Silinəcək kitab: ").strip()
    tapildi=False
    for values in books:
        if delit_book==values['name']:
            books.remove(values)
            print(f"{delit_book} kitab silindi")
            tapildi=True
    if not tapildi:
        print("Kitab tapılmadı")
    print("Yenilenmis siyahi:",books)
