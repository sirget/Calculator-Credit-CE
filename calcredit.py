import re
my_id = '61010280'
location = "./test.txt"
data_credit_require = {

    "01006030": 1,  # cal 1
    "01076001": 1,  # ICT
    "01076002": 1,  # ProFun
    "01006028": 1,  # Pre-eng
    "01006031": 1,  # cal 2
    "01076003": 1,  # circuit
    "01076004": 1,  # oop
    "01076012": 1,  # discrete
    "01076032": 1,  # linear
    "01076005": 1,  # data struct
    "01076006": 1,  # digi
    "01076007": 1,  # data com
    "01076253": 1,  # prob
    "01076008": 1,  # soft dev
    "01076009": 1,  # com org
    "01076010": 1,  # com net
    "01076011": 1,  # os
    "01076263": 1,  # ds
    "01076013": 1,  # theory
    "01076014": 1,  # pre project
    "01076311": 1,  # pro 1
    "01076015": 1,  # com eng pro dev
    "01076312": 1   # pro 2
}

data_credit_elective = {
    "901": 2,
    "902": 4,
    "903": 2,
    "904": 2,
    "0107": 8,
    "xxxx": 2
}


file = open(location, 'r')
match = re.findall('\d{8}', file.read())
match.remove(my_id)
require = data_credit_require.keys()
elective = data_credit_elective.keys()

for i in match:
    if i in require:
        data_credit_require[i] -= 1
    elif i[0] == '9':
        if i[2] == '1':
            data_credit_elective["901"] -= 1
        elif i[2] == '2':
            data_credit_elective["902"] -= 1
        elif i[2] == '3':
            data_credit_elective["903"] -= 1
        elif i[2] == '4':
            data_credit_elective["904"] -= 1
    elif i[1] == '1' and i[3] == '7':
        data_credit_elective["0107"] -= 1
    elif data_credit_elective["xxxx"] != 0:
        data_credit_elective["xxxx"] -= 1
    else:
        print('0')

print(data_credit_require)
print(data_credit_elective)
