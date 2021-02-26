def trains(wagons):
    global globals_wagons_list
    globals_wagons_list = [0 for number in range(wagons)]

    while True:
        command = input()
        if command == 'End':
            return globals_wagons_list
        elif 'add' in command:
            people = [int(objekt) for objekt in command.split('add ') if objekt != '']
            add(people)
        elif 'insert' in command:
            split_list_insert = command.split('insert ')
            for x in split_list_insert:
                if x != '':
                    index_number = x.split()
            insert(index_number)
        elif 'leave' in command:
            split_list_leave = command.split('leave ')
            for n in split_list_leave:
                if n != '':
                    index1_number1 = n.split()
            leave(index1_number1)






def add(people):
    globals_wagons_list[-1] += people[0]


def insert(index_number):
    index = int(index_number[0])
    number = int(index_number[1])
    globals_wagons_list[index] += number

def leave(index1_number1):
    index1 = int(index1_number1[0])
    number1 = int(index1_number1[1])
    globals_wagons_list[index1] -= number1

wagons = int(input())
execute = trains(wagons)
print(execute)


#REGEX VERSION

#def trains(wagons):
   # import re
   # global wagons_list
   # wagons_list = [0 for number in range(wagons)]

    #while True:
        #command = input()
        #if command == 'End':
           # return wagons_list
       # elif 'add' in command:
         #   people = [int(objekt) for objekt in command.split('add ') if objekt != '']
          #  add(people)
       # elif 'insert' in command:
          #  split_list_insert = re.split(r'[insert ]', command)
          #  index_number = [int(item) for item in split_list_insert if item != '']
          #  insert(index_number)
        #elif 'leave' in command:
            #split_list_leave = re.split(r'[leave ]', command)
            #index1_number1 = [int(item) for item in split_list_leave if item != '']
            #leave(index1_number1)






#def add(people):
    #wagons_list[-1] += people[0]


#def insert(index_number):
    #index = index_number[0]
    #number = index_number[1]
    #wagons_list[index] += number

#def leave(index1_number1):
    #index1 = index1_number1[0]
    #number1 = index1_number1[1]
    #wagons_list[index1] -= number1

#wagons = int(input())
#execute = trains(wagons)
#print(execute)
