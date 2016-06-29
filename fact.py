class Factorielle:
    def __init__(self,number):
        self.number = number
        self.current = 0
        self.derniere = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.number:
            raise StopIteration

        if self.current == 0:
            self.current += 1
            return 1

        val = self.current * self.derniere
        self.derniere = val
        self.current +=1
        return val

for i in Factorielle(5):
    print(i)

def factorielle(n):
    derniere = 1
    #pour i dans 5+1
    for i in range(n+1):
        #si ce n'est pas le cas particulier 0(pour ça que la variable derniere est deja a 1)
        if i != 0:
            # fact(n) = n * fact(n-1)
            derniere = i * derniere
        #yield mot clé à se souvenir et a bien comprendre.

        yield derniere



print('-------------------')
for i in factorielle(5):
    print(i)

print('---------------------------')

