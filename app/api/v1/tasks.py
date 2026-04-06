from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi_cache.decorator import cache
from app.core.auth import get_current_active_user
from app.core.database import get_session
from app.crud import task as task_crud
from app.models.task import Task
from sqlmodel import Session

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/")
@cache(expire=60)
def read_tasks(
    _: Annotated[Task, Depends(get_current_active_user)],
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Task]:
    return task_crud.get_tasks(session, offset, limit)

@router.get("/{task_id}")
@cache(expire=60)
def read_task(
    _: Annotated[Task, Depends(get_current_active_user)],
    session: Session = Depends(get_session),
    task_id: int = 0,
) -> Task:
    task = task_crud.get_task_by_id(session, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/", status_code=201)
def create_task(
    _: Annotated[Task, Depends(get_current_active_user)],
    session: Session = Depends(get_session),
    task: Task = None,
) -> Task:
    return task_crud.create_task(session, task)

@router.put("/{task_id}")
def update_task(
    _: Annotated[Task, Depends(get_current_active_user)],
    session: Session = Depends(get_session),
    task_id: int = 0,
    task: Task = None,
) -> Task:
    task_db = task_crud.get_task_by_id(session, task_id)
    if not task_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return task_crud.update_task(session, task_db, task)

@router.delete("/{task_id}")
def delete_task(
    _: Annotated[Task, Depends(get_current_active_user)],
    session: Session = Depends(get_session),
    task_id: int = 0,
):
    task = task_crud.get_task_by_id(session, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task_crud.delete_task(session, task)
    return {"message": "Task deleted"}