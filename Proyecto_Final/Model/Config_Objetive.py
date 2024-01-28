import json

def Read_JSON():
    with open('./Config/objective.json') as json_file:
        data = json.load(json_file)
        return data
    
def Update_JSON(x, y):
    data = Read_JSON()
    data['x_axis'] = x
    data['y_axis'] = y

    with open('./Config/objective.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
