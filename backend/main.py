from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI(
    title="Vite + React + FastAPI",
    description="Backend API for Tesslate Studio base template",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to FastAPI backend!",
        "framework": "FastAPI",
        "version": "1.0.0"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "message": "Backend connected successfully!",
        "timestamp": datetime.now().isoformat()
    }


@app.get("/items")
async def get_items():
    return {
        "items": [
            {"id": 1, "name": "Item 1", "description": "First example item"},
            {"id": 2, "name": "Item 2", "description": "Second example item"},
            {"id": 3, "name": "Item 3", "description": "Third example item"},
        ]
    }


@app.post("/items")
async def create_item(item: dict):
    return {
        "message": "Item created successfully",
        "item": item,
        "timestamp": datetime.now().isoformat()
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, reload=True)
