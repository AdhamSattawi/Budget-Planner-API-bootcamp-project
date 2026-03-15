from typing import Any, Optional

from src.database import async_session_maker
from src.models.student import Student
from src.repositories.student_repository import StudentRepository


def _student_to_dict(student: Student) -> dict[str, Any]:
    return {
        "student_id": student.student_id,
        "first_name": student.first_name,
        "last_name": student.last_name,
        "email": student.email,
        "birth_date": student.birth_date,
        "created_at": student.created_at,
    }


class StudentService:

    def __init__(self, repo: Optional[StudentRepository] = None, session_maker=None):
        self.repo = repo or StudentRepository()
        self.session_maker = session_maker or async_session_maker

    async def get_all_students(self) -> list[dict[str, Any]]:
        async with self.session_maker() as session:
            students = await self.repo.get_all(session)
            return [_student_to_dict(student) for student in students]

    async def get_student_by_id(self, student_id: int) -> dict[str, Any] | None:
        async with self.session_maker() as session:
            student = await self.repo.get_by_id(session, student_id)
            if student is None:
                return None
            return _student_to_dict(student)

    async def create_student(self, student_data: dict[str, Any]) -> dict[str, Any]:
        async with self.session_maker() as session:
            async with session.begin():
                student = Student(
                    first_name=student_data["first_name"],
                    last_name=student_data["last_name"],
                    email=student_data["email"],
                    birth_date=student_data.get("birth_date"),
                )
                result = await self.repo.create(session, student)
            return _student_to_dict(result)
