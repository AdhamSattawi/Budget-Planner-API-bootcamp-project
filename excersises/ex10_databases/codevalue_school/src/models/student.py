import datetime

from sqlalchemy import Date, DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

MAX_EMAIL_LENGTH = 255
MAX_NAME_LENGTH = 100


class Student(Base):
    __tablename__ = "students"

    student_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(125))
    birthday_date: Mapped[Date] = mapped_column(Date)
    created_at: Mapped[DateTime] = mapped_column(DateTime)
    #Exercise: Implement the Student model here
