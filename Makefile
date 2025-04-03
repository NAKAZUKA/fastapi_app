UV_RUN = uv run
APP_PATH = main:app
HOST = 0.0.0.0
PORT = 8044
COMMIT = 

run:
	$(UV_RUN) uvicorn $(APP_PATH) --host $(HOST) --port $(PORT) --reload

format:
	uv run black .

lint:
	uv run ruff check .

gitsync:
	git add . && git commit -m "$(COMMIT)" && git push