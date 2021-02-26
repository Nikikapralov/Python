class ParkingLot:
    def __init__(self, number_of_commands):
        self.n = number_of_commands
        self.car_dict = {}
        self.key_username = None
        self.command_input(self.n)

    def command_input(self, n):
        for _ in range(n):
            command = input().split()
            if 'register' in command:
                print(self.register(command, self.car_dict))
            elif 'unregister' in command:
                print(self.unregister(command, self.car_dict))
        print(self.output_print())

    def register(self, command, dictionary):
        username_key = command[1]
        self.key_username = username_key
        license_plate_value = command[2]
        if username_key not in dictionary:
            dictionary[username_key] = license_plate_value
            result = f'{username_key} registered {license_plate_value} successfully'
        else:
            result = f'ERROR: already registered with plate number {dictionary[username_key]}'
        return result

    def unregister(self, command, dictionary):
        username_key = command[1]
        if username_key not in dictionary:
            result = f'ERROR: user {username_key} not found'
            return result
        else:
            dictionary.pop(username_key)
            result = f'{username_key} unregistered successfully'
            return result

    def output_print(self):
        result = ''
        for key, value in self.car_dict.items():
            result += f'{key} => {value}\n'
        return result


Soft_Uni_Parking = ParkingLot(int(input()))


