from datetime import datetime
from typing import Optional

def get_latest_med_ndc(data_obj: dict) -> Optional[str]:

    # Make variables to keep track of the latest fill date and latest "ndc9" value
    latestFillDate = None
    latest_ndc9 = None
    
    # Make sure the "medications" object inside the date_object exist and is valid
    if "medications" in data_obj:
        
        # Check if the "fills" object exists inside the date_object provided
        # Then iterate through each field to find the target value (most recent prescription fill date)
        for medication in data_obj["medications"]:
            if "fills" in medication:
                for fill in medication["fills"]:
                    fillDate = fill.get("fillDate")
                    if fillDate:
                       if latestFillDate is None or target > fillDate:
                            latestFillDate = fillDate
                            latest_ndc9 = medication.get("ndc9")
    return latest_ndc9

data_object = {
   
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
                "antihtn" 
            ],
            "route": "oral",
            "quantity": "90",
            "daysSupply": "90",
            "fills": [
                {
                    "fillDate": "2012-02-18",
                    "daysSupply": "90",
                    "quantity": "90", 
                },
                {
                    "fillDate": "2012-05-16",
                    "daysSupply": "90",
                    "quantity": "90",
                },
                {
                    "fillDate": "2012-08-06",
                    "daysSupply": "90",
                    "quantity": "90",
                },
                {
                    "fillDate": "2012-11-01",
                    "daysSupply": "90",
                    "quantity": "90"
                },
            ],
            "display": "AMLODIPINE BESYLATE 5 MG",
            "unitsPerDay": "1",
            "dosePerDay": "5",    
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
                    "quantity": "90", 
                },
                {
                    "fillDate": "2012-07-09",
                    "daysSupply": "90",
                    "quantity": "90",
                },
                {
                    "fillDate": "2012-10-09",
                    "daysSupply": "90",
                    "quantity": "90",
                },
                {
                    "fillDate": "2012-01-03",
                    "daysSupply": "90",
                    "quantity": "90"
                },
                {
                    "fillDate": "2012-04-01",
                    "daysSupply": "90",
                    "quantity": "90",
                },
            ],
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
                    "quantity": "90", 
                },
                {
                    "fillDate": "2012-05-25",
                    "daysSupply": "90",
                    "quantity": "90",
                },
                {
                    "fillDate": "2012-7-14",
                    "daysSupply": "90",
                    "quantity": "90",
                },
                {
                    "fillDate": "2012-10-15",
                    "daysSupply": "90",
                    "quantity": "90"
                },
            ],
            "unitsPerDay": "1",
            "dosePerDay": "50"
       },
       {
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
                    "quantity": "180", 
                },
                {
                    "fillDate": "2012-05-16",
                    "daysSupply": "90",
                    "quantity": "180",
                },
                {
                    "fillDate": "2012-08-13",
                    "daysSupply": "90",
                    "quantity": "180",
                },
                {
                    "fillDate": "2012-11-12",
                    "daysSupply": "90",
                    "quantity": "180"
                },
                {
                    "fillDate": "2012-02-16",
                    "daysSupply": "90",
                    "quantity": "180"
                },
            ],
            "unitsPerDay": "2",
            "dosePerDay": "50"
       }
   ],
   "resourceType": "cmr"
}

# Call the function and get the latest "ndc9" value
target = "2012-12-21"
latest_ndc = get_latest_med_ndc(data_object)

# Print the latest "ndc9" value
print(latest_ndc)
