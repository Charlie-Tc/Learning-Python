def return_distinct(*args):
    if sum(args) > 15:
        print('Greater Number')
    elif sum(args) < 10:
        print('Smaller Number')
    elif 10 < sum(args) < 15:
        print('Intermediate Number')

sum_greater = return_distinct(7,4,1)

def words(letters):
    my_sets = set(list(letters))
    my_sets_modifit = list(sorted(my_sets))

    return my_sets_modifit

word = words('modifiying')
print(word)

def indefinity_quatity(*args):
    zero = 0
    count = args.count(zero)
    if count == 2 in args:
        print(True)
    else:
        print(False)

number_cero = indefinity_quatity(2,4,6,7,4,9,0,0)

def count_primes(num):
    prime = True

    for n in range(2, num):
        if num % n == 0:
            print(f'{num} no es primo')
            prime = False
            break

    if prime and num != 1:
        print(f'{num} es primo')


count_primes(15)






