build:
	uv run pipx install --force .

clean:
	rm -rf build/ dist/ *.spec

test-run:
	uv run python pyms/main.py wont-you-join-me.opus
