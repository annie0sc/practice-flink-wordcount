# Hello! Welcome!

## About

* This is my experiment for my big-data assignment. I am working on a [Covid dataset](https://www.kaggle.com/codebreaker619/covid-19-dataset) by running word-count algorithms coded in python and json. 

* Basically an analysis on the correlation between Weekly-covid-cases and deaths-weekly by counting.

## Tech Used:

* Apache-Flink
* Apache-Flink-PyFlink
* Python
* Google Collab

## Install & Execute Pyflink

*Locally:*
1. Install Python 3.8.0 

```
choco install python --version=3.8.0
```
2. Check for version in cmd
```
python --version
```
3. Install Flink in Python using pip command.
```
python -m pip install apache-flink
```
4. If a warning is dispalyed, update pip.
```
python -m pip install --upgrade pip
```
5. Store your python code in a .py file and run it using the following command:
```
python filename.py
```
6. To store the output on a file:
```
python filename.py --output output.txt
```

*TIPS:*

 Make sure all previous or advanced versions of python and flink are removed from the system so that the installations run smoothly.

 *Google Colab*

 1. Install Colaboratory in Google Drive.
 1. Create new Colab file.
 1. Install Flink
 ```
 !pip install apache-flink
 ```
 4. Connect the resources(RAM and Disk) to hosted runtime.
 5. Run python code cell by clicking:
 ```
 enter + shift 
 ```

## Demonstrative Video

https://use.vg/hboCoj

## Resources/References

1. [Kaggle Dataset on Covid-19](https://www.kaggle.com/codebreaker619/covid-19-dataset)
1. Code Forked from [uuboyscy]()
1. [Apache Flink Example](https://ci.apache.org/projects/flink/flink-docs-release-1.0/apis/batch/python.html#example-program)
1. [Apache Flink Table Example](https://ci.apache.org/projects/flink/flink-docs-stable/dev/python/table_api_tutorial.html)
1. Main [Group Repository](https://github.com/annie0sc/big-data-covid-vaccine)
