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

#### Building, packaging, running

For details, see [here](https://atlas.apache.org/InstallationSteps.html).

* `brew install maven`
* `wget http://mirrors.sonic.net/apache/atlas/1.1.0/apache-atlas-1.1.0-sources.tar.gz`
* `tar xvfz apache-atlas-1.1.0-sources.tar.gz`
* `cd apache-atlas-sources-1.1.0/`
* `export MAVEN_OPTS="-Xms2g -Xmx2g"`
* `mvn clean -DskipTests package -Pdist,embedded-hbase-solr`
* `ls distro/target/`
    ```
    ls distro/target 
    META-INF                                  apache-atlas-1.1.0-kafka-hook.tar.gz      atlas-distro-1.1.0.jar
    antrun                                    apache-atlas-1.1.0-migration-exporter     bin
    apache-atlas-1.1.0-bin                    apache-atlas-1.1.0-migration-exporter.zip conf
    apache-atlas-1.1.0-bin.tar.gz             apache-atlas-1.1.0-server                 hbase
    apache-atlas-1.1.0-falcon-hook            apache-atlas-1.1.0-server.tar.gz          hbase.temp
    apache-atlas-1.1.0-falcon-hook.tar.gz     apache-atlas-1.1.0-sources.tar.gz         maven-archiver
    apache-atlas-1.1.0-hbase-hook             apache-atlas-1.1.0-sqoop-hook             maven-shared-archive-resources
    apache-atlas-1.1.0-hbase-hook.tar.gz      apache-atlas-1.1.0-sqoop-hook.tar.gz      rat.txt
    apache-atlas-1.1.0-hive-hook              apache-atlas-1.1.0-storm-hook             solr
    apache-atlas-1.1.0-hive-hook.tar.gz       apache-atlas-1.1.0-storm-hook.tar.gz      solr.temp
    apache-atlas-1.1.0-kafka-hook             archive-tmp                               test-classes
   ```
* `./distro/target/apache-atlas-1.1.0-server/apache-atlas-1.1.0/bin/atlas_start.py`
    ```
    configured for local hbase.
    hbase started.
    configured for local solr.
    solr started.
    setting up solr collections...
    starting atlas on host localhost
    starting atlas on port 21000
    ..................................
    Apache Atlas Server started!!!
    ```
* `curl -u admin:admin http://localhost:21000/api/atlas/admin/version` 
    ```
    {"Description":"Metadata Management and Data Governance Platform over Hadoop","Revision":"release","Version":"1.1.0","Name":"apache-atlas"}
    ```
* `./distro/target/apache-atlas-1.1.0-server/apache-atlas-1.1.0/bin/atlas_stop.py`        
    ```
    stopping atlas....
    Apache Atlas Server stopped!!!
    
    Sending stop command to Solr running on port 9838 ... waiting 5 seconds to allow Jetty process 15655 to stop gracefully.
    stopping master........
    ```

#### Notes

* For Atlas 1.1.0, Java 8 (Update 151) or above is required.

## TODO

#### CI

* https://github.com/xvik/gradle-use-python-plugin
* https://github.com/ananthdurai/airflow-training/blob/master/.circleci/config.yml

