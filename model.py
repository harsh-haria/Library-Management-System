from pydantic import BaseModel


class Social(BaseModel):
    social_type: str
    link: str


class Book(BaseModel):
    book_id: str
    book_name: str


class Address(BaseModel):
    street: str
    city: str


class Timestamp(BaseModel):
    entry_time: str
    exit_time: str


class Student(BaseModel):
    name: str
    email: str
    phone_no: list = []
    address: Address
    socials: Social
    books: Book
    entry_time: Timestamp
