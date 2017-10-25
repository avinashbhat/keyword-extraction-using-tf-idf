# keyword-extraction-using-tf-idf
Extraction of keywords in Wikipedia articles using web scraping and TF-IDF concept. Keyword Extraction is an important area in the field of text summerization. This project is the first step towards summerizing Wikipedia pages.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
These are the modules required. 

* Python 3.x
* BeautifulSoup
* urllib
* re

### Installing
To install all the required modules, follow the steps. I'm assuming the system to be Linux based.

```
$ sudo apt-get update
$ sudo apt-get install python3.6
```
Rest of the stuff can be installed using pip.
To install pip,

```
$ sudo apt-get install python-pip python-dev build-essential 
$ sudo pip install --upgrade pip 
$ sudo pip install --upgrade virtualenv 
```
Then
```
$ sudo pip install bebeautifulsoup4 urllib re
```
to install rest of the modules.

## Deployment

Navigate to the folder and run main.py.
```
$ python3 main.py
```
You will get the keywords from the article as the output.

## Authors

* **Avinash Bhat** @ https://github.com/avinashbhat


## Acknowledgments

* Various websites to which I referred.
