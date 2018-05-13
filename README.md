Coursera: Data At Scale Specialization: CapStone Project

# Predicting blight in the city of Detroit

This repository contains the notebooks and processed files for the Data At Scale Specialization Capstone project proposed by Washington University.

## Introduction 

This project is part of the [Coursera Data Science at Scale Specialization](https://www.coursera.org/specializations/data-science) proposed by University of Washington and taught by Bill Howe. 
The objective of this assignment is to analyse various data source collected by the city of Detroit in order to build a model that could predict whether a building is likely to be blighted. The data was provided in  [datasci-capstone/get-the-data](https://www.coursera.org/learn/datasci-capstone/supplement/D44tm/get-the-data). 
Alternatively The data is available on the [Data At Scale Github repository: Capstone](https://github.com/uwescience/datasci_course_materials/tree/master/capstone/blight).

## Content

### Notebooks

* *Capstone_preprocessing*: Describe the processing of the original data on to the dataset saved within the Processed directory

### Processed data *Processed*

* *blight_demolition.csv*: processed demotion-permit dataset
  * **address**: address of the demolition site
  * **date**: date of issue of the demolition permit m/d/y
  * **type**: Takes value "DISM" or "Dismantle"
  * **long**: longitude 
  * **lat**: latitude
* *blight_incident_count.csv*: processed blight violation dataset
  * **ViolationStreetNumber**: Street number extracted from the source file, instance with negative or missing value were removed
  * **ViolationStreetName**: Street number extracted from the source file, street abbreviations were removed
  * **address**: Vialtion address concatenated from  ViolationStreetNumber and ViolationStreetName
  * **blight_inc**: number of blight violations associated to the adress 	
  * **blight_paid**: total amount in USD assocated with the original *PAID IN FULL* label
  * **blight_partial**: total amount in USD associated with the original *PARTIAL PAYMENT MADE* label
  * **blight_nopaid**: total amount in USD associated with the original *NO PAYMENT ON RECORD* label
  * **blight_notapplied**: total amount in USD associated with the original *NO PAYMENT APPLIED* label
  * **long**: longitude 
  * **lat**: latitude
* *c311_incident_count.csv*	
  * **long**: longitude associated to the complaint
  * **lat**: latitude associated to the complaint
  * **inc_311**: number of incidents reported through 311 call for these set of coordinates
* *crime_incident_count.csv*
  * **long**: longitude associated to the complaint
  * **lat**: latitude associated to the complaint
  * **crime_inc**: number of incidents reported through 311 call for these set of coordinates
* *test_set.csv*
  * **long**: longitude associated to the location
  * **lat**: latitude associated to the location
  * **demolition**: Categorical 1: demolition permit issued, 0: no demolition permit issued 
* *train_set.csv*
  * **long**: longitude associated to the location
  * **lat**: latitude associated to the location
  * **demolition**: Categorical 1: demolition permit issued, 0: no demolition permit issued 
* *grid.json*: json file containing parameters for reproducing a grid accross the city 

### python3 scripts

* *spider_dem_gps.py* python script used to recover gps coordinates from Detroit addresses for the demolition-permit dataset
* *spider_blight_gps.py* python script used to recover gps coordinates from Detroit addresses for the blight violation data set
