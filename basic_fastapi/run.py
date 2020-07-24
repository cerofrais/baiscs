import uvicorn


if __name__=="__main__":
    uvicorn.run("basic_fastapi:app",host='0.0.0.0', port=5252, reload=True, debug=True, workers=1 )
