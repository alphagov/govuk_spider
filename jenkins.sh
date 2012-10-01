#!/bin/sh
sudo pip install -r requirements.txt
scrapy crawl gov.uk -L INFO
