
test:
	@python -m pytest -vv tests/

run:
	@python3 cmd/main.py

server:
	@fastapi run cmd/main.py --reload