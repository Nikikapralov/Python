def get_primes(my_list):

    def is_prime(num):
        for n in range(2, num):
            if num % n == 0:
                return False
        return True


    for num in my_list:
        if num == 0 or num == 1:
            continue
        elif num == 2:
            yield num
            continue
        if is_prime(num):
            yield num

