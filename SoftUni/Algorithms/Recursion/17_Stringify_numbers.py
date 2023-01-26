def stringifyNumbers(obj):
    for key, value in obj.items():
        if isinstance(value, dict):
            stringifyNumbers(value)
        if isinstance(value, int) and not isinstance(value, bool):
            obj[key] = str(value)
    return obj


obj = {
    "num": 1,
    "test": [],
    "data": {
        "val": 4,
        "info": {
            "isRight": True,
            "random": 66
        }
    }
}


obj2 = {'num': '1',
 'test': [],
 'data': {'val': '4',
          'info': {'isRight': True, 'random': '66'}
          }
 }

print(stringifyNumbers(obj))