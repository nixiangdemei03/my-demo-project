# APEX — Auto Parts EXport Platform

> B2B platform connecting Chinese auto parts suppliers with global buyers.

## Who is it for?

- **Suppliers** — Chinese auto parts manufacturers looking to sell overseas without building their own English website
- **Buyers** — Importers, wholesalers, and repair chains from SEA, Middle East, South America, Africa seeking competitive Chinese parts

## v1.0 Features

| Feature | Description |
|---------|-------------|
| 📦 **Product Catalog** | Browse by category, search by OEM number, detailed specs & multi-image gallery |
| 👤 **User System** | Dual-role registration (supplier/buyer), JWT auth, email verification |
| 📋 **Order Management** | Full lifecycle: pending → confirmed → shipped → delivered |
| 🚢 **Freight Integration** | Supplier links order to shipping company + tracking number; buyer tracks in real-time |
| 🖼️ **Image Management** | Drag-and-drop multi-upload to Cloudflare R2, sorting, cover selection |

## Tech Stack

- **Backend**: FastAPI + PostgreSQL + SQLAlchemy + Alembic
- **Frontend**: React + Vite + React Router v6
- **Storage**: Cloudflare R2 (S3-compatible)
- **Auth**: JWT (bcrypt + python-jose)
- **Deploy**: Cloudflare Pages + Workers

## Quick Start

```bash
# Clone
git clone https://github.com/nixiangdemei03/my-demo-project.git
cd my-demo-project

# Backend
cd projects/apex-app/backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# Frontend
cd ../frontend
npm install
npm run dev
```

## Project Structure

```
├── projects/apex-app/
│   ├── backend/         FastAPI backend
│   └── frontend/        React frontend
├── agents/              Agent definitions
├── docs/                PRD & technical docs
├── templates/           Templates
└── evidence/            Screenshots & logs
```

## Conventions

- Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`)
- All endpoints require tests
- PRs need green CI before merge

## Status

**v0** — PRD complete, scaffolding in progress.
