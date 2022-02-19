'''
    hooks in precommit 
    hook file .yaml
    Python uses True, JSON uses true
    all data in json format uses "" rather than ''

    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

'''
import json 

json_string = open('Week_2_JSON.json').read()
json_data = json.loads(json_string)
print(json_data['name'])

