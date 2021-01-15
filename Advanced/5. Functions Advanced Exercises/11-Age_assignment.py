def age_assignment(*args, **kwargs):
    result = {}
    for name in args:
        for key in kwargs:
            if name[0] == key:
                result[name] = kwargs[key]
                break
    return result


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))