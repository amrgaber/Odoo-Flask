import uvicorn

if  __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.0.0", port=8000, reload=True)