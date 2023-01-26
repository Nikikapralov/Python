def collectStrings(obj, array=[]):
    for key, value in obj.items():
        if isinstance(value, dict):
            collectStrings(value, array)
        if isinstance(value, str):
            array.append(value)
    return array


obj = {
    "stuff": 'foo',
    "data": {
        "val": {
            "thing": {
                "info": 'bar',
                "moreInfo": {
                    "evenMoreInfo": {
                        "weMadeIt": 'baz'
                    }
                }
            }
        }
    }
}

print(collectStrings(obj))  # ['foo', 'bar', 'baz']