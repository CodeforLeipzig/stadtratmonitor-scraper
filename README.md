# stadtratmonitor-scraper

## Requirements
### Python
 * [Python 3.12](https://www.python.org/downloads/)
 * [pyenv](https://github.com/pyenv/pyenv) (optional)
 * [PyCharm](https://www.jetbrains.com/pycharm/) (optional)
### Neo4J
 * [Neo4J Aura DB](https://neo4j.com/cloud/platform/aura-graph-database/) (optional)
   * create account at [Neo4J Console](https://console.neo4j.io/) and create a new free tier instance there
 * [Neo4J Desktop](https://neo4j.com/download/)
   * create a new project
   * connect to the just created remote Neo4J Aura instance or
   * create a local Neo4J database management system (DBMS)

## Usage
### Using python
#### Virtual environment
It is recommended to use a [virtual environment](https://docs.python.org/3/tutorial/venv.html) in order to isolate libraries used in this project from the environment of your operating system. To do so, run the following in the project directory:
```
# create the virtual environment in the project directory; do this once
python3 -m venv venv

# activate the environment; do this before working with the scraper
source venv/bin/activate

# install the required libraries
pip3 install -r requirements.txt
```

#### Configuration Pycharm
 * menu `File` -> `Settings...` -> search for `Python Interpreter`
   * `Add Interpreter`
   * keep selection on `Virualenv Environment`
   * either create `New` venv (when not done before) or choose `Existing` one
 * Run configuration
   * Script: `<your local path to clone Git repo>/app/scraping.py`
   * Working directory: `<your local path to clone Git repo>/app`
   * Environment variables: `PYTHONUNBUFFERED=1`

## Using Neo4J
### Prepare for usage in scraper
 * copy config_example to config and adapt the connection values there to match either your local or your remote database
```
[Neo4j]
NEO4J_URI=neo4j+s://<instance_id>.databases.neo4j.io:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=<password>
```
 * Download mirror.db linked in [this release](https://github.com/CodeforLeipzig/stadtratmonitor-scraper/releases/tag/non_git) and copy it to `app/mirror.db`
 * execute scraper either by using run configuration in PyCharm or by calling `python ./scraping.py` from Console being in folder `app`, this will import the contents of mirror.db (as configured in `app/oparl/fakerequest.py`) to Neo4J database (as configured in `config`)

### Neo4J Desktop
 * connect to your database and open it in Neo4J Browser 
 * now you can query the data

### Example queries
 * find paper by reference id: `MATCH(p:Paper) WHERE p.reference = 'VII-P-08704-VSP-01' RETURN p`
 * find entities by modified date: `MATCH(p) WHERE p.modified > datetime('2023-07-17') RETURN p`
   * find entities of type NamedEntity by modified date: `MATCH(p:NamedEntity) WHERE p.modified > datetime('2023-07-17') RETURN p`
 * find persons that issued more than 6 papers: 
   * only the persons: `MATCH(pa:Person)-[r]-(pe:Paper) WITH count(r) as cnt, pa WHERE cnt > 6 RETURN pa, cnt`
   * persons and the papers that belongs to them: `MATCH(pa:Paper)<-[r]-(pe:Person) WITH count(pa) as cnt, pe, collect(pa) as papers WHERE cnt > 6 RETURN pe, papers, cnt`

![image](https://github.com/CodeforLeipzig/stadtratmonitor-scraper/assets/994131/12434093-8051-4345-8216-f0ab81c04320)
