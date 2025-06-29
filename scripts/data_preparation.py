#!/usr/bin/env python3

import pandas as pd
import os

working_dir = "/home/rmalinowska/Documents/sem8/Data-Analysis-and-Visualisation/"
files = os.listdir(working_dir+"dati-regioni")
files_country = ["dpc-covid19-ita-andamento-nazionale.csv"]

areas = {"Abruzzo":10832, "Basilicata":10073, "Calabria":15222, "Emilia-Romagna":22453, "Campania": 13671,\
         "Friuli Venezia Giulia": 7924, "Lazio":17232, "Liguria":5416, "Lombardia": 23864, "Marche":9401,\
        "Molise":4461, "Piemonte": 25387, "Sardegna":24100, "Sicilia":25832, "P.A. Trento":13606,\
        "Toscana": 22987, "Umbria":8464, "Veneto":18345, "P.A. Bolzano":7400, "Puglia": 19362, "Valle d'Aosta": 3261 }

populations = {"Abruzzo" : 1307000 , "Basilicata" : 559000 , "Calabria" : 1870000, "Emilia-Romagna" : 4452000, "Campania" : 5615000,\
         "Friuli Venezia Giulia" : 1219000, "Lazio" : 5745000, "Liguria" : 1535000, "Lombardia" : 10342000, "Marche" : 1524000,\
        "Molise" : 324000 , "Piemonte" : 4302000, "Sardegna" : 1604000, "Sicilia" : 4825000, "P.A. Trento" : 1111000,\
        "Toscana" : 3698000, "Umbria" : 930000, "Veneto" : 4883000, "P.A. Bolzano" : 533267, "Puglia" : 3945000, "Valle d'Aosta" : 143000}

def merge_files(files_list, directory,add_deaths=False, add_recoveries=False):
    data = pd.DataFrame()
    
    for f in files_list:
        data = pd.concat([data, pd.read_csv(directory+f)],ignore_index=True)
    data = data.drop(columns=["stato", "lat", "long", "casi_da_sospetto_diagnostico", "casi_da_screening", "note", "note_test", \
                        "ingressi_terapia_intensiva","note_casi", "codice_nuts_1", "codice_nuts_2", "totale_positivi_test_molecolare",\
                        "totale_positivi_test_antigenico_rapido", "tamponi_test_molecolare", "tamponi_test_antigenico_rapido"], errors='ignore')
    data["data"] = data["data"].str[:10]
    data["data"] = pd.to_datetime(data["data"], format='%Y-%m-%d')
    data['year'] = pd.DatetimeIndex(data['data']).year
    data['month_year'] = pd.to_datetime(data['data']).dt.to_period('M')
    data.rename(columns = {'data':'date', 'codice_regione':'region_code', 'denominazione_regione':'region_name', 'ricoverati_con_sintomi':'hospitalised_patients_with_symptoms',\
                'terapia_intensiva':'intensive_care', 'totale_ospedalizzati':'total_hospitalised_patients', 'isolamento_domiciliare':'home_confinement',\
                'totale_positivi':'current_positive_cases', 'variazione_totale_positivi':'positive_cases_difference', 'nuovi_positivi':'new_positive_cases',\
                'dimessi_guariti':'recovered', 'deceduti':'deaths', 'totale_casi':'total_positive_cases', 'tamponi':'tests_performed', 'casi_testati':'people_tested'}, inplace = True)
    
    data = data.sort_values(by="date", ignore_index=True)
    new_deaths = [data["deaths"].values[0]]
    new_recoveries = [data["recovered"].values[0]]
    areas_arr = []
    populations_arr = []
    if "region_name" in data.columns:
        areas_arr.append(areas[data["region_name"].values[0]])
        populations_arr.append(populations[data["region_name"].values[0]])
    for i in range(1,data.shape[0]):
        new_deaths.append(data["deaths"].values[i]-data["deaths"].values[i-1])
        new_recoveries.append(data["recovered"].values[i]-data["recovered"].values[i-1])
        if "region_name" in data.columns:
            areas_arr.append(areas[data["region_name"].values[i]])
            populations_arr.append(populations[data["region_name"].values[i]])
    if add_deaths:
        data["new_deaths"] = new_deaths
    if add_recoveries:
        data["new_recoveries"] = new_recoveries
    if areas_arr != []:
        data["region_area"] = areas_arr
    if populations_arr != []:
        data["region_population"] = populations_arr
    return data
    
merge_files(files, working_dir+"dati-regioni/").to_csv(working_dir+"/covid19_italy_regions.csv",sep=",", header=True)
merge_files(files_country, working_dir, True, True).to_csv(working_dir+"/covid19_italy.csv", sep=",", header=True)
