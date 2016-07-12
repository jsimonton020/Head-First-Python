#!/usr/bin/python3

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return({'name': templ.pop(0),
              'dob': templ.pop(0),
              'times': str(sorted(set([sanitize(t) for t in templ]))[0:3])})
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return(None)

james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')

print(james['name'] + "'s fastest times are" + james['times'])
print(julie['name'] + "'s fastest times are" + julie['times'])
print(mikey['name'] + "'s fastest times are" + mikey['times'])
print(sarah['name'] + "'s fastest times are" + sarah['times'])
