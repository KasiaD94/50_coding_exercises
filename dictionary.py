keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

new_dict = dict(zip(keys, values))
#print(new_dict)

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = {**dict1, **dict2}
#print(dict3)

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

#print(sampleDict["class"]["student"]["marks"]["physics"])

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

new_dict2 = dict.fromkeys(employees, defaults)
#print(new_dict2)

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
# Keys to extract
keys = ["name", "salary"]

new_dict3 = {k:v for k, v in sample_dict.items() if k in keys}

#print(new_dict3)

sample_dict2 = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys2 = ["name", "salary"]

for k in keys2:
    sample_dict2.pop(k, None)
#print(sample_dict2)

sample_dict3 = {'a': 100, 'b': 200, 'c': 300}

for k,v in sample_dict3.items():
    if v == 200:
        #print(str(v) + " present in dict")
        pass

sample_dict4 = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sample_dict4["location"] = sample_dict4.pop("city")
#print(sample_dict4)

sample_dict5 = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

#print(min(sample_dict5, key=sample_dict5.get))

sample_dict6 = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

print(sample_dict6['emp3']['salary'])
#print(sample_dict6)