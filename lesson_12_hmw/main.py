import app.books as books_service
from app.library import export_book, load_books, save_data, oper_history

books_service.books.clear()
books_service.books.extend(load_books())

while True:
    print("\n--- KİTABXANA MENYUSU ---")
    print("1. Kitab əlavə et ")
    print("2. Kitab sil ")
    print("3. Kitabları göstər ")
    print("4. Hesabat yarat və Çıx")
    
    secim = input("Seçiminizi daxil edin (1-4): ").strip()
    
    if secim == "1":
        books_service.add_book_interactive()
        save_data(books_service.books)
        export_book(books_service.books)
        
    elif secim == "2":
        books_service.remove_book()
        save_data(books_service.books)
        export_book(books_service.books)
        
    elif secim == "3":
        print("\n--------Cari kitablarin siyahisi---------")
        books_service.show_books()
        print("Umumi kitab sayi:", len(books_service.books))
        
    elif secim == "4":
        save_data(books_service.books)
        export_book(books_service.books)
        print("Məlumatlar yadda saxlanıldı. Sağ olun!")
        break
        
    else:
        print("Yanlış seçim! Zəhmət olmasa 1-4 arası rəqəm seçin.")