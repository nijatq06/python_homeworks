from pathlib import Path
import json
from app.stat import get_books_count, old_books_count, avg_year_count
from datetime import datetime
BASE_DIR=Path(__file__).resolve().parent.parent
DATA_DIR=BASE_DIR/'data'
REPORT_FILE=DATA_DIR/"book_report.txt"
BOOK_FILE=DATA_DIR/"books.json"
History_dir=DATA_DIR/"operations.txt"
def oper_history(action, book_name):
    DATA_DIR.mkdir(exist_ok=True)
    now = datetime.now().isoformat(timespec="seconds")
    with open(History_dir, "a", encoding="utf-8") as file:
        file.write(f"{now} | {action} | {book_name}\n")
def export_book(book_list):
    DATA_DIR.mkdir(exist_ok=True)
    with open(REPORT_FILE,"w",encoding="utf-8") as file:
        file.write("--------Kitab hesabatı---------\n\n\n")
        for book in book_list:
            file.write(
                f"{book['name']}|"
                f"{book['author']}|"
                f"{book['year']}\n"
            )
        file.write("\n")
        file.write(f"{get_books_count()}\n")
        file.write(f"{old_books_count()}\n")
        file.write(f"{avg_year_count()}\n")
def save_data(book_list):
    DATA_DIR.mkdir(exist_ok=True)
    with open(BOOK_FILE,"w",encoding="utf-8") as file:
        json.dump(
            book_list,
            file,
            ensure_ascii=False,
            indent=4
        )
        
def load_books():
    if not REPORT_FILE.exists():
        print("Hesabat hele ki yaradilmayib")
        return[]
    try:
        with open(BOOK_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []
# def delete_book(book_name):
#     DATA_DIR.mkdir(exist_ok=True)
    