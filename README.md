```bash
uv run alembic init -t async alembic # инициализация алембик миграций
```

```bash
uv run alembic revision -m "comment" # создать миграцию
```

```bash
uv run alembic upgrade head # применить миграцию к БД
```

```bash
uv run alembic downgrade -1 # откат бд на -1
```