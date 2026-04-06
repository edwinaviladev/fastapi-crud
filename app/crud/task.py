from sqlmodel import Session, select
from app.models.task import Task

def get_tasks(session: Session, offset: int, limit: int) -> list[Task]:
    return session.exec(select(Task).offset(offset).limit(limit)).all()

def get_task_by_id(session: Session, task_id: int) -> Task | None:
    return session.get(Task, task_id)

def create_task(session: Session, task: Task) -> Task:
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def update_task(session: Session, task_db: Task, task_data: Task) -> Task:
    task_db.sqlmodel_update(task_data.model_dump(exclude_unset=True))
    session.add(task_db)
    session.commit()
    session.refresh(task_db)
    return task_db

def delete_task(session: Session, task: Task) -> None:
    session.delete(task)
    session.commit()