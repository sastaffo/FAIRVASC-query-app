# FAIRVASC Query Application

This web application was developed for the [FAIRVASC project](https://fairvasc.eu/about-us/).

[Link to Github Repository](https://github.com/sastaffo/FAIRVASC-query-app)

## Project Abstract

ANCA-Associated Vasculitis (AAV) is an auto-immune disease that causes inflammation in small blood vessels, often leading to organ damage; most commonly kidney disease and lung disease. The cause of AAV and the factors involved in the occurrence of flare-ups are mostly unknown, although it's thought that genetic and environmental factors play a role.

The disease affects a little more than 100,000 people in Europe, resulting in very few cases in any one country. The FAIRVASC Project was started by the European Vasculitis Society. Its primary goal is to make national registries containing medical information about AAV patients consistent across Europe. By granting researchers access to a greater amount of patient data, they will be able to learn more about the disease, its onset, and possible treatments and cures.

This project involves the creation of a web application that will act as the front-end for researchers accessing information from FAIRVASC registries.


## Running the Project Locally

#### 1. Running RDF databases locally
1. In the command line, navigate to the `apache-jena-fuseki-3.16.0` directory
2. Run command `.\fuseki-server`
The Fuseki server is automatically hosted locally on port 3030 (<http://localhost:3030>)

#### 2. Running Django Project
Python 3 must be installed on this computer

1. In a separate command window, navigate to the `fairvasc_backend` directory
2. Run command `python manage.py runserver`
3. Open <http://localhost:8000> to view and use the application locally



## Project Files Description

#### Fuseki RDF Databases
`apache-jena-fuseki-3.16.0` contains the files needed to run the Fuseki server. The server contains two RDF databases, named **Endor** and **Hoth**. Both databases contain synthetic data that are compliant with FAIRVASC ontology, as of April 2021.

The configurations for these databases are found in
`apache-jena-fuseki-3.16.0\run\configuration\~.ttl`

The encrypted contents of the databases are found in
`apache-jena-fuseki-3.16.0\run\databases\~\*`

#### Query Application
`fairvasc_backend` is a Django project that contains the FAIRVASC query web application.

The `fairvasc_backend` sub-directory manages the two project apps.

The front-end is in the `vue_frontend` app directory. The HTML file for the web page is located in
`vue_frontend\templates\vue_frontend\vue_app.html`.

The back-end functionality is in the `sparql_query` app directory.
* `urls.py` contains the path to the `get_counts` function that can be referenced by the front-end.
* `views.py` contains the `get_counts` function that takes a HttpRequest from the front-end and parses the parameters. The parameters are used to create instances of the QueryBuilder class.
* `QueryBuilder.py` contains the `QueryBuilder` class which builds a SPARQL Query from the parameters given, poses it to the given RDF end-point and parses the results.
* `constants.py` contains the end-point URLs (currently Hoth and Endor exist as local end-points) and the correct formatting for the parameters for each of the data elements that can be queried in the application.
