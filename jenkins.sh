#!/bin/sh
scrapy crawl gov.uk -L INFO -o build/items.json -t jsonlines
