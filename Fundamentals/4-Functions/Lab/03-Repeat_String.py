def repeat_string(string, times_to_repeat_it):
    repeated_string = string * times_to_repeat_it
    return repeated_string


string = input()
times_to_repeat_it = int(input())
result = repeat_string(string=string, times_to_repeat_it=times_to_repeat_it)
print(result)