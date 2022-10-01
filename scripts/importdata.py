#Take a subset of data and attach it to geojson. Trying to keep the geojson file size down so I don't bring it all over
import json

geojson = json.load(open('../data/waltham_parcels.geojson'))
new_attrs = json.load(open('../data/selected_B&T.json'))

#For each feature
#Find it's LOC_ID
#For each LOD_ID
#Add total Value
#Add LUC to array
#If no OO, add it; if same OO, skip; if opposite OO, mark mixed

for feature in geojson['features']:
  LOC_ID = feature['properties']['LOC_ID']
  print(LOC_ID)
  index=next((i for i, d in enumerate(new_attrs) if d["LOC_ID"] == LOC_ID), None)
  print(index)
  if index is None:
    continue
  
  if "TotalValue" in feature['properties'].values():
    feature['properties']['TotalValue'] += new_attrs[index]['TotalValue']
  else:
    feature['properties']['TotalValue'] = new_attrs[index]['TotalValue']

  feature['properties']['LUC'] = new_attrs[index]['LUC']
  
  if "OwnerOccup" in feature['properties'].values():
    if feature['properties']['OwnerOccup'] != new_attrs[index]['OwnerOccup']:
      feature['properties']['OwnerOccup'] = 'M'
  else:
    feature['properties']['OwnerOccup'] = new_attrs[index]['OwnerOccup']
    
json.dump(geojson, open('output.json', 'w'))
