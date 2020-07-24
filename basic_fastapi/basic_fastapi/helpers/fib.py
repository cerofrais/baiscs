import time
from basic_fastapi import app
from fastapi import Request, BackgroundTasks, Header
from datetime import datetime
from fastapi import Body
from pydantic import BaseModel,Field
from typing import Optional

def bad_fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==0: 
        return 0
    # Second Fibonacci number is 1 
    elif n==1: 
        return 1
    else: 
        return bad_fibonacci(n-1)+bad_fibonacci(n-2) 

def better_fib(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n+1): 
            c = a + b 
            a = b 
            b = c 
        return b 
  
def run_task(name: str, id=None):
    time.sleep(3)
    
    with open("task_result.txt", mode="a") as file:
        now = datetime.now()
        content = f"{name} [{id}]:  {now}\n"
        file.write(content)

@app.post("/task/run/{name}/{id}")
async def task_run(name: str, id: int, background_tasks: BackgroundTasks):
    ''' runs a task '''
    background_tasks.add_task(run_task, name, id)
    print(f"working on {name}, {id}")
    return {"message": f"Task {name}: ID [{id}] is being run now.\n"}

class Item(BaseModel):
    name:str
    description: str =Field(None,title="descrip",max_length=30)
    # if any field is optional
    id:Optional[int]=None
    data: Optional[dict] = None

# example to handle multiple fields as input
@app.post("/test/multifiled")
async def multifield(req:Request,item:Item=Body(...,embed=True),header1:str=Header("Default")):
    # accessing the item information
    print(header1)
    print(req.headers)
    print(item.name)
    return item