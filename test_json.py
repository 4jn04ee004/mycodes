##Test

a = {
    'name' : 'Json file',
    'data' : '{
   "data":{
      "sectorInformation":[
         {
            "sectorId":"chbM00014B_01",
            "antennaName":null,
            "rtsAzimuth":null,
            "agl":"1.0",
            "actualAzimuth":"60.0",
            "actualLatitude":null,
            "technology":"5G",
            "antennaType":"mmW",
            "siteReferenceId":"chbM00014B",
            "actualElectricalTilt":"4.0",
            "actualMechanicalTilt":"4.0",
            "sectorNumber":"1",
            "rtsTilt":null,
            "id":"ddb3291d-5aea-44c2-800a-52f65887e950",
            "band":"400MHz",
            "actualLongitude":null,
            "status":"Active",
            "actualAntennaheight":"10.0"
         }
      ]
   },
   "eventType":"SECTOR_EVENT_TYPE",
   "source":"RCP",
   "operation":"CREATE"
}'
    }

print(a)
