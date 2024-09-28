build:
	poetry run pipx install --force .

clean:
	rm -rf build/ dist/ *.spec
