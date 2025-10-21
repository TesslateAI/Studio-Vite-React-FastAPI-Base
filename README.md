# Vite + React + FastAPI Base Template

A separated fullstack template with Vite + React for the frontend and FastAPI for the backend. Perfect for data science and ML applications.

## Features

- **Vite + React** - Modern frontend with instant HMR
- **FastAPI** - High-performance async Python backend
- **TypeScript** - Full type safety on frontend
- **Tailwind CSS** - Utility-first styling
- **CORS Configured** - Ready for cross-origin requests
- **Dual Hot Reload** - Both servers reload automatically
- **API Documentation** - Auto-generated with Swagger UI

## What's Included

### Frontend (`/frontend`)
- Vite + React 18 setup
- TypeScript configuration
- Tailwind CSS integration
- API client examples
- Responsive UI components

### Backend (`/backend`)
- FastAPI application
- CORS middleware configured
- Example CRUD endpoints
- Health check endpoint
- Auto-generated API docs

## Development

Both servers start automatically when you create a project from this base in Tesslate Studio:

- **Frontend**: Accessible via the preview URL
- **Backend API**: `http://localhost:8001`
- **API Docs**: `http://localhost:8001/docs`

## Project Structure

```
/frontend
  /src
    App.tsx              # Main application
    main.tsx            # Entry point
    index.css           # Global styles
  vite.config.ts        # Vite configuration
  package.json          # Frontend dependencies

/backend
  main.py               # FastAPI application
  requirements.txt      # Python dependencies
```

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /items` - List all items
- `POST /items` - Create new item

## Frontend API Usage

The frontend is configured to proxy `/api/*` requests to the backend:

```typescript
// Calls http://localhost:8001/items
const response = await fetch('/api/items');
const data = await response.json();
```

## Adding New Endpoints

### Backend

```python
# backend/main.py
@app.get("/users")
async def get_users():
    return {"users": []}
```

### Frontend

```typescript
// frontend/src/api/users.ts
export async function getUsers() {
  const response = await fetch('/api/users');
  return response.json();
}
```

## Learn More

- [Vite Documentation](https://vitejs.dev/)
- [React Documentation](https://react.dev/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Tailwind CSS Documentation](https://tailwindcss.com/)

## Tesslate Studio

This base is optimized for use with Tesslate Studio. The `TESSLATE.md` file contains configuration for automatic dual-server startup.
