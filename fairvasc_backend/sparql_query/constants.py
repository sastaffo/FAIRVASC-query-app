import json
Endpoints = {
	'Hoth' : "http://localhost:3030/hoth/sparql",
	'Endor' : "http://localhost:3030/endor/sparql",
}

Queries = {
	'prefixes' : ("PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX fvc: <http://ontologies.adaptcentre.ie/fairvasc#> "),
	'total_count' : ("SELECT (COUNT(?subject) as ?patientCount) WHERE {?subject a fvc:Patient.}"),
	'count_deaths' : ("SELECT (COUNT(?subject) as ?patientCount) WHERE {  ?subject a fvc:Patient; fvc:hasOutcomes ?o. ?o fvc:dateOfDeath ?d. }"),
	'count_sex' : ("SELECT (COUNT(?subject) as ?patientCount) WHERE {  ?subject a fvc:Patient; fvc:gender ?g; FILTER (?g ='SEX') } group by ?g"),
	'count_deaths_sex' : ("SELECT (COUNT(?subject) as ?patientCount) WHERE {  ?subject a fvc:Patient; fvc:gender ?g; fvc:hasOutcomes ?o. ?o fvc:dateOfDeath ?d. FILTER (?g ='SEX') } group by ?g"),
	'count_single_param' : ("SELECT (COUNT(?subject) as ?patientCount) WHERE {  ?subject a fvc:Patient; fvc:STRAT_TYPE ?type. ?type fvc:STRAT_PRED ?param. FILTER (?param = 'STRAT_PARAM') } group by ?param"),
	'count_deaths_single_param' : ("SELECT (COUNT(?subject) as ?patientCount) WHERE {  ?subject a fvc:Patient; fvc:STRAT_TYPE ?type; fvc:hasOutcomes ?o. ?o fvc:dateOfDeath ?d. ?type fvc:STRAT_PRED ?param. FILTER (?param = 'STRAT_PARAM') } group by ?param"),
};

FVC_PARAMS = {
	'ancaSpec' : [
		"MPO positive",
		"PR3 positive",
		"ELISA negative",
		"No ELISA performed",
		"MPO and PR3 positive",
		"Other"
	],
	'diagnosis' : [
		"Microscopic polyangiitis (MPA)",
		"Granulomatosis with polyangiitis (GPA)",
		"Eosinophilic granulomatosis with polyangiitis (EGPA)",
		"ANCA vasculitis unclassified"
	],
	'sex' : [
		"Male",
		"Female"
	]
}
FVC_stratify = {
	'ancaSpec' : {
		'type_pred' : "hasANCA",
		'param_pred' : "ancaSpec",
		'params' : {
			'mpo' : "MPO positive",
			'pr3' : "PR3 positive",
			'elisa_neg' : "ELISA negative",
			'elisa_none' : "No ELISA performed",
			'mpo_pr3' : "MPO and PR3 positive",
			'other' : "Other"
		}
	},
	'ancaIF' : {
		'type_pred' : "hasANCA",
		'param_pred' : "ancaIF",
		'params' : {
			'panca' : "pANCA positive",
			'canca' : "cANCA positive",
			'if_neg' : "Negative",
			'atyp' : "Atypical",
			'none' : "Not tested"
		}
	},
	'diag' : {
		'type_pred' : "hasDiagnosis",
		'param_pred' : "mainDiagnosis",
		'params' : {
			'mpa' : "Microscopic polyangiitis (MPA)",
			'gpa' : "Granulomatosis with polyangiitis (GPA)",
			'egpa' : "Eosinophilic granulomatosis with polyangiitis (EGPA)",
			'unclas' : "ANCA vasculitis unclassified"
		}
	},
	'sex' : {
		'type_pred' : "gender",
		'params' : {
			'male': "Male",
			'female' : "Female"
		}
	}
};
