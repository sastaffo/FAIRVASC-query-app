import pandas as pd
from io import StringIO
from SPARQLWrapper import SPARQLWrapper as sparql
from SPARQLWrapper import JSON as sparql_JSON
from SPARQLWrapper import CSV as sparql_CSV
import json

from sparql_query.constants import FVC_PARAMS

import logging

prefixes = ("PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX fvc: <http://ontologies.adaptcentre.ie/fairvasc#> ")
select_base = ("SELECT (COUNT(?p) as ?Patient_Count) ")
where_base_open = ("WHERE { ?p a fvc:Patient. ")
where_close_bracket = ("}")
group_by = (" group by ")
where_deceased = (" ?p fvc:hasOutcomes ?o. ?o fvc:dateOfDeath ?dd. ")
where_eskd = (" ?p fvc:hasOutcomes ?o. ?o fvc:dateOfESKD ?de. ")
strat_dict = {
	"sex" : {
		"where" : (" ?p fvc:gender ?Sex. "),
		"var" : (" ?Sex "),
	},
	"ancaSpec" : {
		"where" : ( "?p fvc:hasANCA ?anca. ?anca fvc:ancaSpec ?ANCA_Specificity. " ),
		"var" : (" ?ANCA_Specificity "),
	},
	"diagnosis" : {
		"where" : ( "?p fvc:hasDiagnosis ?diag. ?diag fvc:mainDiagnosis ?Main_Diagnosis. " ),
		"var" : (" ?Main_Diagnosis "),
	},
}


class QueryBuilder():
	def __init__(self, total_counts=True, outcome_deceased=False, by_sex=False, by_ancaSpec=False, by_diagnosis=False):
		self.logger = logging.getLogger('console')
		self.total_counts = total_counts
		self.outcome_deceased = outcome_deceased
		self.by_sex = by_sex
		self.by_ancaSpec = by_ancaSpec
		self.by_diagnosis = by_diagnosis
		self.select_string = select_base
		self.where_string = where_base_open
		self.group_string = where_close_bracket
		self.result_dict = {}
		self._get_empty_results()
		if not total_counts:
			# if stratified, strat by deceased xor by eskd
			if outcome_deceased: self.where_string = self.where_string + where_deceased
			else : self.where_string = self.where_string + where_eskd
		if by_sex or by_ancaSpec or by_diagnosis:
			self.group_string = self.group_string + group_by
			if by_sex: self._add_strat("sex")
			if by_ancaSpec: self._add_strat("ancaSpec")
			if by_diagnosis: self._add_strat("diagnosis")
		self.query_string = prefixes + self.select_string + self.where_string + self.group_string
	# end init

	def __str__(self):
		return self.query_string

	def _add_strat(self, strat_by):
		strat_var = strat_dict[strat_by]["var"]
		self.select_string = self.select_string + strat_var
		self.where_string = self.where_string + strat_dict[strat_by]["where"]
		self.group_string = self.group_string + strat_var
	# end _add_strat

	def send_query(self, endpoint):
		sparql_query = sparql(endpoint)
		sparql_query.setReturnFormat(sparql_CSV)
		sparql_query.setQuery(self.query_string)
		result_str = (sparql_query.query().convert()).decode("utf-8")
		#self.logger.info(result_str)
		result_dict_raw = self._parse_csv_string(result_str)
		self._add_results_to_empty(result_dict_raw)
		#self.logger.info(json.dumps(self.result_dict, indent=2) + "\n\n")
		return self.result_dict
	# end send_query

	def _parse_csv_string(self, result_str):
		result_buffer = StringIO(initial_value=result_str, newline="\r\n")
		df = pd.read_csv(result_buffer)
		result_dict_raw = df.to_dict(orient="index")
		return result_dict_raw

	def _add_results_to_empty(self, result_dict_raw):
		for r_raw in result_dict_raw:
			row_raw = result_dict_raw[r_raw]
			for r in self.result_dict:
				row = self.result_dict[r]
				if (not self.by_ancaSpec) or (self.by_ancaSpec and (row['ANCA_Specificity'] == row_raw['ANCA_Specificity'])):
					if (not self.by_diagnosis) or (self.by_diagnosis and (row['Main_Diagnosis'] == row_raw['Main_Diagnosis'])):
						if (not self.by_sex) or (self.by_sex and (row['Sex'] == row_raw['Sex'])):
							row['Patient_Count'] = row_raw['Patient_Count']
				self.result_dict[r] = row
		return

	def _get_empty_results(self):
		anca_list = []
		diag_list = []
		sex_list = []
		if self.by_ancaSpec:
			for a in FVC_PARAMS['ancaSpec']:
				anca_list.append({ "Patient_Count" : 0, "ANCA_Specificity" : a })
		else: anca_list.append({ "Patient_Count" : 0 })

		if self.by_diagnosis:
			for d in FVC_PARAMS['diagnosis']:
				for a_row in anca_list:
					d_row = a_row.copy()
					d_row['Main_Diagnosis'] = d
					diag_list.append(d_row)
		else: diag_list = anca_list

		if self.by_sex:
			for s in FVC_PARAMS['sex']:
				for d_row in diag_list:
					s_row = d_row.copy()
					s_row['Sex'] = s
					sex_list.append(s_row)
		else: sex_list = diag_list

		for index in range(0, len(sex_list)):
			self.result_dict[index] = sex_list[index]
		return
