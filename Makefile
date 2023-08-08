clean:
	rm -rf $(wildcard *.csv) $(wildcard *.png) $(wildcard *.jpg) __pycache__/*

build:
	docker build -t py3 .

rebuild:
	docker build --no-cache -t py3 .

run:
	docker run -v $(shell pwd):/usr/src/app py3 python3 jkent-challenge.py

show:
	code $(wildcard *.csv) $(wildcard *.png) $(wildcard *.jpg)
