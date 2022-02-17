# *******************************************************
# Python Training Course _ Week 4
# Objects - Activity:  Create Health Diagnosis Program
# *******************************************************

class Patient:
    def __init__ (self, p_name, sugar_in, fat_in, salt_in):
        self.p_name = p_name
        self.sugar_in = sugar_in
        self.fat_in = fat_in
        self.salt_in = salt_in
    def health(self):
        if self.sugar_in > 37.5:
            print(f"""{self.p_name}: Warning! Your sugar intake is {self.sugar_in} g per day.
It should be no more than 37.5 g per day""")
        else:
            print(f'{self.p_name}, your sugar intake is OK')
        print()
        if self.fat_in > 77:
            print(f"""{self.p_name}: Warning! Your fat intake is {self.fat_in} g per day.
It should be no more than 77 g per day""")
        else:
            print(f'{self.p_name}, your fat intake is OK')
        print()
        if self.salt_in > 2300:
            print(f"""{self.p_name}: Warning! Your sugar intake is {self.salt_in} mg per day.
It should be no more than 2300 mg per day""")
        else:
            print(f'{self.p_name}, your salt intake is OK')
        print()

pat_rec = []
for i in range(3):
    a = input('Enter patient name: ')
    flag = 0
    while flag == 0:
        try:
            b = float(input('Enter sugar intake: '))
            flag = 1
        except:
            print('Please, enter a number')

    flag = 0
    while flag ==0:
        try:
            c = float(input('Enter fat intake: '))
            flag = 1
        except:
            print('Please, enter a number')
    flag = 0
    while flag ==0:
        try:
            d =float(input('Enter salt intake: '))
            flag = 1
        except:
            print('Please, enter a number')
    pat = Patient(a, b, c, d)
    pat_rec.append(pat)
    print('/////////////////////////////////////')
    print()
print(f'There are {len(pat_rec)} patients in the records')
print('///////////////////////////////////////////////')
for j in range(3):
    pat_rec[j].health()