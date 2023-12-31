def get_antihtn_meds(data_obj: dict) -> list:

    # Make a variable and assign it to the medications in sample data and construct an empty list to store the solution 
    medList = data_obj.get("medications", [])
    antihtnMeds = []


    # Search throught the drugGroup in sample data for the target medication 
    for medication in medList:
        if "antihtn" in medication.get("drugGroup", []):
            # If the target medication is found then add it to the back of the list
            antihtnMeds.append(medication)

    return antihtnMeds

# Sample data object
sample_data = {
   "etlUpdated": "2012-12-21T23:58:00",
    "id": "123",
    "medications": [
        {
            "ndc9": "39017-0147",
            "brandName": "AMLODIPINE BESYLATE",
            "dosageStrength": "5",
            "dosageUnit": "mg",
            "doseForm": "tablet",
            "drugGroup": [
"ccb",
"antihtn" ],
            "route": "oral",
            "quantity": "90",
            "daysSupply": "90",
            "fills": [
                {
                    "fillDate": "2012-02-18",
                    "daysSupply": "90",
                    "quantity": "90"
}, {
}, {
}, {
} ],
            "display": "AMLODIPINE BESYLATE 5 MG",
"fillDate": "2012-05-16",
"daysSupply": "90",
"quantity": "90",
"fillDate": "2012-08-06",
"daysSupply": "90",
"quantity": "90",
"fillDate": "2012-11-01",
"daysSupply": "90",
"quantity": "90",
     "unitsPerDay": "1",
    "dosePerDay": "5"
},
{
    "ndc9": "60505-2671",
    "brandName": "ATORVASTATIN CALCIUM",
    "genericName": "ATORVASTATIN CALCIUM",
    "dosageStrength": "80",
    "dosageUnit": "mg",
    "doseForm": "tablet, film coated",
    "drugGroup": [
        "statin",
        "azoleddi",
        "antilipid",
        "cms_statin",
        "cms_spc_statin"
    ],
    "route": "oral",
    "quantity": "90",
    "daysSupply": "90",
    "fills": [
        {
            "fillDate": "2012-04-10",
            "daysSupply": "90",
            "quantity": "90"
}, {
}, {
}, {
}, {
"fillDate": "2012-07-09",
"daysSupply": "90",
"quantity": "90",
"fillDate": "2012-10-09",
"daysSupply": "90",
"quantity": "90",
"fillDate": "2012-01-03",
"daysSupply": "90",
"quantity": "90",

             "fillDate": "2012-04-01",
            "daysSupply": "90",
            "quantity": "90"
} ],
    "unitsPerDay": "1",
    "dosePerDay": "80"
},
{
    "ndc9": "68382-0136",
    "brandName": "LOSARTAN POTASSIUM",
    "genericName": "LOSARTAN POTASSIUM",
    "dosageStrength": "50",
    "dosageUnit": "mg",
    "doseForm": "tablet, film coated",
    "drugGroup": [
        "arb",
        "antihtn",
        "cms_rasa"
    ],
    "route": "oral",
    "quantity": "90",
    "daysSupply": "90",
    "fills": [
        {
            "fillDate": "2012-02-25",
            "daysSupply": "90",
            "quantity": "90"
}, {
}, {
}, {
"fillDate": "2012-05-25",
"daysSupply": "90",
"quantity": "90",
"fillDate": "2012-07-14",
"daysSupply": "90",
"quantity": "90",
"fillDate": "2012-10-15",
"daysSupply": "90",

             "quantity": "90"
        }
    ],
    "unitsPerDay": "1",
    "dosePerDay": "50"
}, {
"ndc9": "00378-0018",
"brandName": "METOPROLOL TARTRATE",
"genericName": "METOPROLOL TARTRATE",
"dosageStrength": "25",
"dosageUnit": "mg",
"doseForm": "tablet, film coated",
"drugGroup": [
"antihtn",
    "betablocker"
],
"route": "oral",
"quantity": "180",
"daysSupply": "90",
"fills": [
    {
        "fillDate": "2012-02-06",
        "daysSupply": "90",
        "quantity": "180"
}, {
}, {
}, {
}, {
"fillDate": "2012-05-16",
"daysSupply": "90",
"quantity": "180",
"fillDate": "2012-08-13",
"daysSupply": "90",
"quantity": "180",
"fillDate": "2012-11-12",
"daysSupply": "90",
"quantity": "180",

"fillDate": "2012-02-16",
                    "daysSupply": "90",
                    "quantity": "180"
} ],
            "unitsPerDay": "2",
            "dosePerDay": "50"
        }
],
    "resourceType": "cmr"
}

# Call the function to get the list of medications with "antihtn" in their "drugGroup"
ans = get_antihtn_meds(sample_data)

for medication in ans:
    print(medication["brandName"])

