# Introduction

Code to accompany the [How To Use Vector Search To Quickly Build A Content-Based Filtering Recommender System](https://medium.com/@_init_/how-to-quickly-build-a-content-based-filtering-recommender-system-using-a-vector-database-f6c52d444c94) blog post on Medium

# Prerequisites

1. VS Code
2. Docker

# Usage

1. Clone the repo
2. Open the folder in VS Code inside a dev container when prompted
3. Run `make download-data` to download the datasets
4. Run the [01_metadata.ipynb](./notebooks/01_metadata.ipynb) notebook to prepare to scrape the movie posters and stuff
5. Run `make scrape-movie-metadata` to scrape the movie posters and stuff
6. Read the rest of the notebooks in the [notebooks](./notebooks/) folder in sequence