from utils.input_utils import (
    take_dept,
    take_year,
    take_semister
)
from config import LMS

def get_book_details():
    dept = take_dept()
    year = take_year()
    sem = take_semister()
    return dept,year,sem


def add_book(book_name,book_id):
    dept,year,sem = get_book_details()
    book = {
        'id' : book_id,
        'name': book_name 
    }
    LMS['books'][dept][year][sem].append(book)
    print("Book added successfully!")

def get_books():
    dept,year,sem = get_book_details()
    print(LMS['books'][dept][year][sem])
    print("Books fetched successfully!")




