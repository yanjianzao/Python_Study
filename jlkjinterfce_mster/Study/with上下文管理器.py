with open('some_file.txt', 'w') as opened_file:
    opened_file.write('Hola!')
def profile():
    name = "Danny"
    age = 30
    return name, age

if __name__ == '__main__':
    print(type(profile()))
