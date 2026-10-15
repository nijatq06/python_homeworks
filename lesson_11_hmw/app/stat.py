from .books import books
def get_books_count():
    print(f"Umumi kitablarin sayi: {len(books)}")
def old_books_count():
    count=0
    for i in books:
        if i['year']<2000:
            count+=1
    print("2000-ci ilin evvel cixan kitablarin sayi: ",count)
def avg_year_count():
    sum=0
    if len(books)==0:
        print("Sistemde kitab yoxdur")
    for items in books:
        sum+=items['year']
    print(f"Orta buraxılış ili: {sum/len(books)}")