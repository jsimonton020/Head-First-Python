#!/usr/bin/python3.4
import pickle

man = []
other = []

try:
    data = open('sketch.txt')

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':' , 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')

try:
    man_file = open('man_data.txt', 'wb')
    other_file = open ('other_data.txt', 'wb')

    pickle.dump(man, man_file)
    pickle.dump(other, other_file)

except IOError as err:
    print('File Error:' + str(err))

except pickle.PickleError as perr:
    print('Pickling error:' + str(perr))


finally:
    man_file.close()
    other_file.close()
