
### Installation and setup
Fast Api is buit on top of starlette (gen2 web framework)


### If we want to work with jinja template, install the following also
    # uvicorn concurrency request handler
    pip install jinja2 aiofiles uvicorn

### swaggger
    you can see the swagger documnetation at /docs endpoint in your api

### fastapi has a module BackgroundTasks to run time taking tasks
    
### Add more workers to increase performance

### curl command to check the performance:
```curl -X POST "http://127.0.0.1:5252/task/run/harsha/1" -H  "accept: application/json" -d ""```

### shell command to do concurrency testing:
```for i in {1..1000}; do curl -X POST "http://0.0.0.0:5700/task/run/NAME/$i" -H  "accept: application/json"; done```
