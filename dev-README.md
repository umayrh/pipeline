# Contractual Compliance Pipeline

## Setup

### Apache Airflow

* `source activate`
* `airflow initdb`
* `airflow scheduler` (foreground process)
* `airflow webserver`

#### Notes

* Ensure that all dags are present before starting the webserver and scheduler.
  Otherwise they may not be reread.

#### References

* https://github.com/ananthdurai/airflow-training
* https://airflow.apache.org/installation.html
* https://gist.github.com/msumit/40f7905d409fe3375c9a01fa73070b73

### Apache Atlas

#### Building and packaging

For details, see [here](https://atlas.apache.org/InstallationSteps.html).

* `brew install mvn`
* `tar xvfz apache-atlas-1.1.0-sources.tar.gz`
* `cd apache-atlas-sources-1.1.0/`
* `export MAVEN_OPTS="-Xms2g -Xmx2g"`
* `mvn clean -DskipTests package -Pdist,embedded-hbase-solr`
* `ls distro/target/`

```
```

#### Installing and running

* `tar -xzvf apache-atlas-${project.version}-server.tar.gz`
* `cd atlas-${project.version}`
* `export MANAGE_LOCAL_HBASE=true`
* `export MANAGE_LOCAL_SOLR=true`
* `bin/atlas_start.py`
* `curl -u username:password http://localhost:21000/api/atlas/admin/version`

#### Notes

* For Atlas 1.1.0, Java 8 (Update 151) or above is required.

## TODO

#### CI

* https://github.com/xvik/gradle-use-python-plugin
* https://github.com/ananthdurai/airflow-training/blob/master/.circleci/config.yml

