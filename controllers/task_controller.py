from fastapi import APIRouter, HTTPException, status
from models import Task

router = APIRouter()
tasks_list = []

@router.get('/tasks')
def get_tasks():
    return tasks_list

@router.post('/tasks')
def create_tasks(task: Task):
    tasks_list.append(task)
    return task

