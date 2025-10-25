# TESSLATE.md - Project Context

> Context for AI agents working on this project.

## Framework Configuration

**Frontend**: Vite + React
**Backend**: FastAPI (Python)
**Port**: 5173 (Frontend), 8001 (Backend)

**Tech Stack:**
- React 18 with Vite
- Tailwind CSS
- TypeScript
- FastAPI
- Python 3.11+
- SQLAlchemy (optional)

## File Structure

```
frontend/
├── src/
│   ├── App.tsx          # Main app
│   ├── main.tsx         # Entry point
│   ├── components/      # Reusable components
│   └── pages/           # Page components
└── vite.config.ts       # Vite config

backend/
├── main.py              # FastAPI app
├── requirements.txt     # Dependencies
├── api/                 # API routes
├── models/              # Database models
└── services/            # Business logic
```

## Development Server

**Start Command**:
```bash
# Backend
cd backend && pip install -r requirements.txt && uvicorn main:app --host 0.0.0.0 --port 8001 --reload &

# Frontend
cd frontend && npm install && npm run dev -- --host 0.0.0.0 --port 5173
```

**Production Build**:
```bash
cd frontend && npm run build
```
