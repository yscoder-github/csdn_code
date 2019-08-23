new_json = './new_method.json'
old_json = './old_best.json'
import json 
# quesiton as key 
new_q_set = set([])
with open(new_json, 'r') as f:
    for d in f.readlines():
        if 'question' in json.loads(d):
            new_q_set.add(json.loads(d)['question'])


old_q_set = set([])
with open(old_json, 'r') as f:
    for d in f.readlines():
        if 'question' in json.loads(d):
            old_q_set.add(json.loads(d)['question'])



inte_set = new_q_set - old_q_set

print(inte_set)

print(len(inte_set))

for d in inte_set:
    print(d)
# with open(old_json, 'r') as f:
#     print(f.readlines())
