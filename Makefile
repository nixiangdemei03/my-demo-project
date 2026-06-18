.PHONY: dev test deploy

dev:
	@echo "Starting backend (port 8000) & frontend (port 5173)..."
	@trap 'kill 0' EXIT; \
		cd backend && uvicorn main:app --reload --port 8000 & \
		cd frontend && npm run dev

test:
	@echo "Running all tests..."
	cd backend && python -m pytest
	cd frontend && npm test

deploy:
	@echo "Deploying to Cloudflare..."
	cd frontend && npm run build
