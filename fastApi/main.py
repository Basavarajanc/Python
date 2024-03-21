from typing import Union

from fastapi import FastAPI

from models import Todo

app = FastAPI()

todos = []

# Get all todos
@app.get("/todos")
async def get_todos():
    return { "todos": todos }


# Get Single todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id:int):
   for todo in todos:
       if todo.id == todo_id:
           return {"todo": todo}
   return {"message": "no todos found"}

# Create todos
@app.post("/todos")
async def post_todos(todo: Todo):
    todos.append(todo)
    return { "message": "todo has been added" }


# delete Single todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id:int):
   for todo in todos:
       if todo.id == todo_id:
           todos.remove(todo)
           return {"message": "Todo is deleted"}
   return {"message": "no todos found delete"}

# update Single todo
@app.put("/todos/{todo_id}")
async def put_todo(todo_id:int, todo_obj: Todo):
   for todo in todos:
       if todo.id == todo_id:
           todo.id = todo_obj.id
           todo.item = todo_obj.item
           return {"message": "Todo is updated"}
   return {"message": "no todos found to update"}