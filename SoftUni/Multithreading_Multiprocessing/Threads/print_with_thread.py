import threading

to_print = "abcdefghijklmnopqrstuvwxyz123456789"


def print_letter(to_print):
    print("Thread started.")
    for letter in to_print:
        print(letter)
    print("Thread ended.")


my_thread = threading.Thread(target=print_letter, args=[to_print])
my_thread2 = threading.Thread(target=print_letter, args=[to_print])
my_thread.start()
my_thread2.start()
my_thread.join()
my_thread2.join()


