# GOV.UK Spider

This is a web spider which will crawl all of the pages on
[www.gov.uk](https://www.gov.uk/) that it can find and expose
information relating to status responses and referrers.

## Requirements

You will need:

* Python 2.6 (or greater)
* Scrapy v0.14.4

To install the project dependencies you can use pip with the
following command:

    pip install -r requirements.txt

## Running the spider

Once you have the relevant dependencies you can view a list of the
available spiders by running:

    scrapy list

And then run a specific spider with:

    scrapy crawl insert_spider_name

A (local) JSON output can be created using the following options:

    scrapy crawl gov.uk -o items.json -t jsonlines
