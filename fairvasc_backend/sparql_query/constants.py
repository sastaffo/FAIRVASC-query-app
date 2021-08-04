import json
Endpoints = {
	'Endor' : "http://localhost:3030/endor/sparql",
	'Hoth' : "http://localhost:3030/hoth/sparql",
}

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
