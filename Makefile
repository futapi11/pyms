build:
	poetry run pipx install --force .

clean:
	rm -rf build/ dist/ *.spec

test-run:
	poetry run python pyms/main.py
