#pip psycopg2-binary
import psycopg2

class Library:
    def __int__(self, author, title):
        self.book_inventory = {}
        self.author = author
        self.title = title

    def borrowed(self):
        if self.is_borrowed:
            return f"{self.title} has already been booked out"
        self.is_borrowed = True
        return f"You have returned the book: {self.title}"

    def search(self, search_item):
        if search_item in self.book_inventory:
            return f"the book {search_item} is available in the library"


def conn():
    try:
        connection = psycopg2.connect(
            dbname="dsd_libds",
            user="up2271401",
            password="",
            host="34.76.26.140",
            port=""
        )
        print("Connection successful")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    conn()

main()