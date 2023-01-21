SHELL:=bash

download-data:
	mkdir data && \
		pushd data && \
		wget https://files.grouplens.org/datasets/movielens/ml-1m.zip && \
		unzip ml-1m.zip && \
		rm ml-1m.zip