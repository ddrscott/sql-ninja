
dist:
	python setup.py sdist bdist_wheel

publish: dist
	twine upload dist/*
