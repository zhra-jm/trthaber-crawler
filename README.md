# trthaber-crawler
A crawler that contains news data from trthaber.


## Build With
*sqlite

*python

## How To Use

* at first you should install virtualenv 

```apt-get install python3-virtualenv```

* then create a new virtual environment 

```virtualenv -p python3 venv```

* then we have to activate it

``` . venv/bin/activate```

* now we got to install the requirements

```pip install the requirements```

* first of all we have to create tables:

``` python3 main.py "create_tables"```

* to run the projects first of all we have to find the links we want to crawl so you have to run:
 
 ```python3 main.py "get_links"```
 
 * now we got the links in our db now we should crawl the links:
 
 ```python3 main.py "get_articles"```
 
 * now the crawl is done and you have pure data in case you want to see status run:
 
 ```python3 main.py "stats"```
 
 *Wish you have enjoyed that!Good Luck:D
