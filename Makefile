UV_RUN = uv run
APP_PATH = main:app
HOST = 0.0.0.0
PORT = 8044

run:
	$(UV_RUN) uvicorn $(APP_PATH) --host $(HOST) --port $(PORT) --reload

format:
	uv run black .

lint:
	uv run ruff check .
