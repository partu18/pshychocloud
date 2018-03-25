# pshychocloud

## Description

Pshychocloud is a simple python-based conversation analyzer which aims to show the most used words from a person/group of (potentially) any chat service.
This tool will analyze the input provided looking for each person involved in the conversation, identifying them, and creating a [word cloud]() not only for each of them but also for the whole conversation.
Pshychocloud doesn't implements the wordcloud generation part. In order to achieve this, the following project was used: [wordcloud](https://github.com/amueller/word_cloud)

So far, we support:

* Whatsapp


## Installation

You just need to install the dependencies written inside **requirements.txt**.

As an advice, create a new virtualenv and install all the dependencies there using pip:
```bash
pip install -r requirements.txt
```

After installing dependencies: 
```bash
python setup.py build
```
```bash
python setup.py install
```


## How to use it
There is a special file to use as an entry point to the program called **analyze_text.py**
You just have to provide the parameters it requires. 

In order to know about the parameters, type:
```bash
python analyze_text.py --help
```




## Future work

* Filter stopwords in spanish
* Filter special autogenerate messages depending on the Analyzer
* Add output (and generate the directory if needed) for the graphs
* Prepare the project as an egg
* Create a directory with the output
* Support new chat clients
* Support multi lines mesages
* Post analysis:

    * Feelings extraction: Analyzing time windows, understand feelings of the person in a certain moment.
    * Deal with typos: "hello" and "helo" should be the same word.
    * Deal with homonyms (using context): "box" to store things? or the sport? 
