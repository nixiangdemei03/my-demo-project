.PHONY: dev test deploy

dev:
	@echo "Starting APEX dev environment..."
	cd backend && uvicorn main:app --reload --port 8000 &
	cd frontend && npm run dev

test:
	cd backend && pytest -v

deploy:
	@echo "Deploy: Cloudflare Pages + Workers (see docs/05-roadmap.md)"
