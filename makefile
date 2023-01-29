SHELL:=bash

download-data:
	mkdir -p data

	pushd data && \
		wget https://files.grouplens.org/datasets/movielens/ml-1m.zip -O ml-1m.zip && \
		unzip -o ml-1m.zip && \
		rm ml-1m.zip
	
	pushd data && \
		wget https://files.grouplens.org/datasets/movielens/ml-25m.zip -O ml-25m.zip && \
		unzip -o ml-25m.zip && \
		rm ml-25m.zip

scrape-movie-metadata:
	mkdir -p ./data/crawls

	pushd spiders/imdb && \
		scrapy crawl imdb \
			-o ../../data/movie_metadata.jsonl \
			--logfile ../../data/crawls/imdb_spider.log \
			-a urls=../../data/imdb_urls.txt \
			-s JOBDIR=../../data/crawls/imdb