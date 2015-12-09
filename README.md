# gdsmongo
Search site for genotype database (at http://10.1.8.167:8000/report/) for use by Plant and Food Research.

Like [genotypedatasearch](https://github.com/MicrowavedScrambledEggs/genotypedatasearch), except runs on Python 2.7 with a MongoDB backend

Uses library django-non-rel 1.6 with MongoDB-engine. Both these libraries only compatible with Python 2, hence why this is a seperate project and not a branch of [genotypedatasearch](https://github.com/MicrowavedScrambledEggs/genotypedatasearch)

To run server, from project directory enter command:
```shell
$ manage.py runserver [ip address with port]
```

Allows for searching by experiment name, primary investigator and date created. Displays table of matching results, with links in each row to the relavant datasource table and a download link for the data.

On start up, syncs local db with http://10.1.8.167:8000/report/experiment/csv/.

Datasource table got from querying via url: "http://10.1.8.167:8000/report/data_source/csv/?experiment=" + experiment_name

Download links are to: "http://10.1.8.167:8000/report/genotype/csv/?experiment=" + experiment_name

(Test use csv files in test_resources instead of http://10.1.8.167:8000/report/)
