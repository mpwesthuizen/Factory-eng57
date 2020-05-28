# recap function

# define a function

def say_hello(name):
    return (f'Hello {name}' )

# #BAD!
# def return_formatted_name(name):
#     print(name.title().strip())


def return_formatted_name(name):
    return name.title().strip()

# print the return of the function outside - NOT print inside the function. If you do all argument will return none (because return is already set to none)
f_name = (return_formatted_name("marcus           "))

print(say_hello((f_name)))


# # Basis of a test
#
# def return_formatted_name(name):
#     return name.title().strip()


# test setup
print("Testingfunction return formatted name() with 'filipe   '--> Filipe")
know_input = 'filipe   '
expected_out = 'Filipe'
#test execution
print("Testingfunction return formatted name() with 'filipe   '--> Filipe")
print(return_formatted_name() == expected_out)

# testing say_hello()