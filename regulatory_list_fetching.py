import sys

min_python = (3, 7)
if sys.version_info < min_python:
    sys.exit("Python %s.%s or later is required.\n" % min_python)

import requests
import time

form_date = str(int(time.time_ns() / 1000000))

payload = {
    "p_p_id": "disslists_WAR_disslistsportlet",
    "p_p_lifecycle": "2",
    "p_p_state": "normal",
    "p_p_mode": "view",
    "p_p_resource_id": "exportResults",
    "p_p_cacheability": "cacheLevelPage",
    "_disslists_WAR_disslistsportlet_formDate": form_date,
    "_disslists_WAR_disslistsportlet_exportColumns": "name,ecNumber,casNumber,haz_detailed_concern,dte_inclusion,doc_cat_decision,doc_cat_iuclid_dossier,doc_cat_supdoc,doc_cat_rcom,prc_external_remarks",
    "_disslists_WAR_disslistsportlet_orderByCol": "dte_inclusion",
    "_disslists_WAR_disslistsportlet_orderByType": "desc",
    "_disslists_WAR_disslistsportlet_searchFormColumns": "haz_detailed_concern,dte_inclusion",
    "_disslists_WAR_disslistsportlet_searchFormElements": "DROP_DOWN,DATE_PICKER",
    "_disslists_WAR_disslistsportlet_substance_identifier_field_key": "",
    "_disslists_WAR_disslistsportlet_haz_detailed_concern": "",
    "_disslists_WAR_disslistsportlet_dte_inclusionFrom": "",
    "_disslists_WAR_disslistsportlet_dte_inclusionTo": "",
    "_disslists_WAR_disslistsportlet_total": "1000", 		# the number of results to return, NOT the number of total SVHCs on the list (i.e. this number can be more than the number of SVHCs)
    "_disslists_WAR_disslistsportlet_exportType": "xml"
}
resp = requests.post('https://echa.europa.eu/candidate-list-table', data=payload)
print(resp.text)
with open("svhcFetched.utf8txt", 'w', encoding='UTF-8') as f:
    f.write(resp.text)
