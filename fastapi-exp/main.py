from fastapi import FastAPI, Depends
from pydantic import BaseModel
from starlette.requests import Request
import json

# class Task(BaseModel):
#     username: str
#     task_content: str


app = FastAPI()


database = {
    "Sarvesh": {
        1: {
            "title": "Do Morning Walk",
            "task_content": "We should always go for a walk in the morning"
        }
    }
}


# def get_database():
#     return database


# @app.post("/articles/{article_id}/comments")
# def post_comment(article_id: int, comment: Comment, database = Depends(get_database)):
#     database["articles"][article_id]["comments"].append(comment)
#     return {"msg": "comment posted!"}

@app.get("/tasks/")
async def get_tasks(request: Request):
    username = await request.body()
    username = json.loads(username.decode('utf-8'))
    print(username)
    return database[username["username"]]

@app.post("/update/")
async def update_task(request: Request):
    info = await request.body()
    info = json.loads(info.decode('utf-8'))
    print(info)
    task_id = info["task_id"]
    username = info['username']
    new_content = info["task_content"]
    database[username][task_id]["task_content"] = new_content
    print(database)
    return "Ok"

@app.put("/add/")
async def create_task(request:Request):
    info = await request.body()
    info = json.loads(info.decode('utf-8'))
    print(info)
    task_id = info['task_id']
    username = info['username']
    content = info["task_content"]
    title = info["title"]

    if(username not in database.keys()):
        database[username] = {}
    database[username][task_id] = {}
    database[username][task_id]["title"] = title
    database[username][task_id]["task_content"] = content

    print(database)
    return True

@app.delete("/delete_task/")
async def delete_task(request: Request):
    info = await request.body()
    info = json.loads(info.decode("utf-8"))
    print(info)

    task_id = info['task_id']
    username = info['username']
    del database[username][task_id]
    
    print(database)

    return "OK"

# {"username":"Sarvesh", "task_id":1, "task_content": "new_content"}_content"}