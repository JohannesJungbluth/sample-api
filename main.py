import os
import uvicorn

if __name__ == "__main__":
    host = os.getenv("UVICORN_HOST", "0.0.0.0")
    port = int(os.getenv("UVICORN_PORT", "8000"))
    workers = int(os.getenv("UVICORN_WORKERS", "1"))
    uvicorn.run("api:app", host=host, port=port, reload=True, debug=True, workers=workers)
