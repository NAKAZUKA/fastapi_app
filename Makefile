UV_RUN = uv run
APP_PATH = main:app
HOST = 0.0.0.0
PORT = 8044
COMMIT = 

run:
	$(UV_RUN) uvicorn $(APP_PATH) --host $(HOST) --port $(PORT) --reload

format:
	$(UV_RUN) black .

lint:
	$(UV_RUN) ruff check .

gitsync:
	$(UV_RUN) git add . && git commit -m "$(COMMIT)" && git push