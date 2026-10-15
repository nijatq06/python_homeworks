import app.books as books
import app.stat as st
books.add_book("1948", "GeorgeOrwell",1949)
books.add_book("CodeDaVinci","DanBrown",2003)
books.add_book("DigitalFortress","DanBrown", 1998)
books.add_book("Angels&Demons", "DanBrown", 2000)
books.add_book("TheHarryPotterSeries", "J.K.Rowling",2003)
books.show_books()
books.search_book_by_author()
books.search_book_by_name()
books.remove_book()
st.avg_year_count()
st.old_books_count()
st.get_books_count()