from weppy import App, url
import requests

app = App(__name__)

@app.route('/docs')
def docs():
    return

@app.route('/docs/ex1')
def ex1():
    response = requests.get("https://www.nwfsc.noaa.gov/data/api/v1/source/trawl.catch_fact/selection.json?filters=field_identified_taxonomy_dim$scientific_name=Eopsetta%20jordani,date_dim$year>=2010,date_dim$year<=2012&variables=date_yyyymmdd,field_identified_taxonomy_dim$scientific_name")
    return response

@app.route('/docs/ex2')
def ex2():
    response = requests.get("https://www.nwfsc.noaa.gov/data/api/v1/source/trawl.catch_fact/selection.csv?filters=field_identified_taxonomy_dim$scientific_name=Eopsetta%20jordani,date_dim$year>=2010,date_dim$year<=2012&variables=date_yyyymmdd,field_identified_taxonomy_dim$scientific_name")
    return response

if __name__ == "__main__":
    app.run()
