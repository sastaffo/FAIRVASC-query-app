import json
Endpoints = {
	'Hoth' : "http://localhost:3030/hoth/sparql",
	'Endor' : "http://localhost:3030/endor/sparql",
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
