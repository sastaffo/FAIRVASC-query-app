from SPARQLWrapper import SPARQLWrapper as sparql
from SPARQLWrapper import JSON as sparql_JSON
import json
import logging

from sparql_query.constants import Endpoints, Queries

def send_sparql_query(reg_name, query_string):
	query_obj = sparql(Endpoints[reg_name]['endpoint'])
	query_string = Queries['prefixes'] + Endpoints[reg_name]['prefix'] + query_string
	query_obj.setQuery(query_string)
	query_obj.setReturnFormat(sparql_JSON)
	result_dict = query_obj.query().convert()
	return result_dict

def get_patient_count(result_dict, bind_index=0):
	if len(result_dict['results']['bindings']) == 0:
		value = 0
	else:
		value_dict = result_dict['results']['bindings'][bind_index]
		value_str = value_dict['patientCount']['value']
		try: value = int(value_str)
		except: value = 0
	return value
