from rest_framework import viewsets
from rest_framework.response import Response as RestResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import sys
import json


import logging
from sparql_query.constants import Endpoints
from sparql_query.QueryBuilder import QueryBuilder

logger = logging.getLogger('console')
# Create your views here.

def fairvasc_app(request):
	return HttpResponse(render(request, 'vue_index.html'))

def get_counts(request):
	registry_name = request.GET.get('registry')
	ep = Endpoints[registry_name]
	outcome_deceased = (request.GET.get('outcome_deceased') == "true")
	by_sex = (request.GET.get('Sex') == "true")
	by_ancaSpec = (request.GET.get('ANCA_Specificity') == "true")
	by_diagnosis = (request.GET.get('Main_Diagnosis') == "true")
	# total_counts == True
	q_total_count = QueryBuilder()
	result_total_count = q_total_count.send_query(ep)
	q_total_strats = QueryBuilder(by_sex=by_sex, by_ancaSpec=by_ancaSpec, by_diagnosis=by_diagnosis)
	result_total_strats = q_total_strats.send_query(ep)

	# total_counts = False
	q_total_with_outcome = QueryBuilder(total_counts=False, outcome_deceased=outcome_deceased)
	result_total_with_outcome = q_total_with_outcome.send_query(ep)
	q_strat_with_outcome = QueryBuilder(total_counts=False, outcome_deceased=outcome_deceased, by_sex=by_sex, by_ancaSpec=by_ancaSpec, by_diagnosis=by_diagnosis)
	result = q_strat_with_outcome.send_query(ep)
	for row_key in result:
		row = result[row_key]
		row["Total_Patient_Count"] = result_total_count[0]["Patient_Count"]
		row["Patient_Count_with_Outcome"] = result_total_with_outcome[0]["Patient_Count"]
		for strat_row_key in result_total_strats:
			strat_row = result_total_strats[strat_row_key]
			# checks that all included stratifications are equal (if not included, always valid)
			if (by_sex and row["Sex"] == strat_row["Sex"]) or (not by_sex):
				if (by_ancaSpec and row["ANCA_Specificity"] == strat_row["ANCA_Specificity"]) or (not by_ancaSpec):
					if (by_diagnosis and row["Main_Diagnosis"] == strat_row["Main_Diagnosis"]) or (not by_diagnosis):
						row["Patient_Count_Stratified"] = strat_row["Patient_Count"]
		row["Registry"] = registry_name
		result[row_key] = row
	return JsonResponse({registry_name : result})
