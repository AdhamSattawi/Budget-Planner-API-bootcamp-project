from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.student import Student


class StudentRepository:

    async def get_all(self, session: AsyncSession) -> list[Student]:
        result = await session.scalars(select(Student))
        return list(result.all())

    async def get_by_id(self, session: AsyncSession, student_id: int) -> Student | None:
        return await session.get(Student, student_id)

    async def create(self, session: AsyncSession, student: Student) -> Student:
        session.add(student)
        await session.flush()
        await session.refresh(student)
        return student
    
    async def find_by_email(email: str, session: AsyncSession) -> Student:
        stmt = select(Student).where(Student.email == email)
        return session.scalar(stmt)
    
    async def find_by_last_name(last_name: str, session: AsyncSession) -> list[Student]:
        stmt = select(Student).where(Student.last_name == last_name)
        return session.scalars(stmt).all()
    
    async def find_by_partial_name(partial_name: str, session: AsyncSession) -> list[Student]:
        stmt = select(Student).where(Student.last_name.like(f"%{partial_name}%"))
        return session.scalars(stmt).all()
    
    async def update_email(student: Student, new_email: str, session: AsyncSession) -> None:
        student_to_update = session.get(student, student.student_id)
        student_to_update.email = new_email
        session.commit()

    async def delete_student(student: Student, session: AsyncSession) -> None:
        student_to_delete = session.get(student, student.student_id)
        session.delete(student_to_delete)
        session.commit()

    

