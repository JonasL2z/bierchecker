import uvicorn

uvicorn.run("bierchecker_api:app", host="0.0.0.0", port=8000, reload=True)
