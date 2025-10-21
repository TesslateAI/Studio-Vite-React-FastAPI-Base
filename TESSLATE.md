# Vite + React + FastAPI Base

Separated fullstack template with Vite + React for the frontend and FastAPI for the backend. Perfect for data science and ML applications.

## Framework Configuration

**Frontend**: Vite + React
**Backend**: FastAPI (Python)
**Port**: 5173

## Development Server

**Start Command**:
```bash
# Start backend first (in background)
cd backend && pip install -r requirements.txt && uvicorn main:app --host 0.0.0.0 --port 8001 --reload &

# Start frontend
cd frontend && npm install && npm run dev -- --host 0.0.0.0 --port 5173
```

**Stop Command**:
```bash
pkill -f "uvicorn main:app"
pkill -f "vite"
```

## Environment Variables

The following environment variables are automatically provided by Tesslate Studio:

```env
VITE_BASE_PATH=/preview/user1-project5  # Auto-generated path prefix for routing
NODE_ENV=development                     # Development mode
PORT=5173                                # Frontend server port
VITE_HMR_PROTOCOL=ws                     # HMR WebSocket protocol (ws/wss)
VITE_HMR_PORT=80                         # HMR WebSocket port (80/443)
CHOKIDAR_USEPOLLING=true                 # File watching in Docker
CHOKIDAR_INTERVAL=1000                   # Polling interval
```

You can also define custom variables:

```env
VITE_API_URL=http://localhost:8001
PYTHONUNBUFFERED=1
FASTAPI_ENV=development
```

**Note**: `VITE_BASE_PATH` is automatically set by Tesslate and used by `vite.config.ts` for the `base` configuration. This allows your Vite app to work correctly when deployed under a path prefix.

## Project Structure

```
/frontend               # Vite + React Frontend
  /src
    /components        # React Components
    /pages            # Page Components
    App.tsx           # Main App Component
    main.tsx          # Entry Point
  vite.config.ts      # Vite Configuration
  package.json        # Frontend Dependencies

/backend                # FastAPI Backend
  main.py             # FastAPI Application
  requirements.txt    # Python Dependencies
  /api                # API Routes
  /models             # Database Models
  /services           # Business Logic
```

## Features

- **Vite Frontend**: Lightning-fast HMR and build times
- **FastAPI Backend**: High-performance async Python API
- **Dual Hot Reload**: Both frontend and backend reload automatically
- **CORS Configured**: Ready for cross-origin requests
- **PostgreSQL Ready**: Database integration included
- **Example CRUD API**: Starter endpoints for common operations

## Tech Stack

- Vite
- React 18
- TypeScript
- FastAPI
- Python 3.11+
- PostgreSQL (optional)
- SQLAlchemy (optional)

## Getting Started

1. The development servers will start automatically
2. Frontend accessible at preview URL
3. Backend API at `http://localhost:8001`
4. API docs at `http://localhost:8001/docs`

## Example API Usage

Frontend code to call backend:

```typescript
// src/api/client.ts
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8001';

export async function getItems() {
  const response = await fetch(`${API_URL}/items`);
  return response.json();
}
```

Backend API endpoint:

```python
# backend/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
async def get_items():
    return {"items": []}
```

## Learn More

- [Vite Documentation](https://vitejs.dev/)
- [React Documentation](https://react.dev/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
