# geneesmiddelen

Om te werken met de maximum geneesmiddelen prijzen

# installation

1. `cd docker && docker-compose build`
2. `docker-compose up -d`

# data

The actual data files are the json files in the `data` directory. The instructions below are to rebuild these files.

# building the data files

1. `docker exec -it docker_geneesmiddelen_1 bash`
2. `cd /opt/gm/bin`
3. `./get_urls.py >../urls.txt`
4. `./fetch.py`
5. `./parse.py`

# contact

Breyten Ernsting (breyten@openstate.eu)
