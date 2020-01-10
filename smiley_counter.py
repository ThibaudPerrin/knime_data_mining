import csv


positiv_smileys = [':)', ':-)', '^^', '^_^', ':D', ':*', ': )', ':p', '^-^',
                '^_^', "'_'", "'-'", '❤', '<3', ':d', 'c:', ':>']
negativ_smileys = [':(', ':-(', ':-\'(', ':/', 'D:', ': (', ':-/', ':@',
                '-_-', ':l', ':|']

def count_smiley(smiley, text):
    c = 0
    position = 0

    while True:
        position = text.find(smiley, position)
        if position == -1:
            return c
        
        c = c + 1
        position = position + 1


def count_smileys(list_of_smiley, text):
    c = 0
    for smiley in list_of_smiley:
        c = c + count_smiley(smiley, text)
    return c


def analyze_smileys(text):
    return count_smileys(positiv_smileys, text), \
           count_smileys(negativ_smileys, text), \
           count_smileys(['UPDATE:'], text)


with open('data/googleplaystore_user_reviews.csv') as read_file:
    with open('data/googleplaystore_user_reviews_with_smiley.csv', mode='w+') as writ_file:
        csv_reader = csv.reader(read_file, delimiter=',', quotechar='"', doublequote=True,  quoting=csv.QUOTE_MINIMAL)
        csv_writer = csv.writer(writ_file, delimiter=',', quotechar='"', doublequote=True, quoting=csv.QUOTE_MINIMAL)
        is_first_row = True
        for row in csv_reader:
            if is_first_row:
                csv_writer.writerow(row + ['PositifEmoji', 'NegativEmoji', 'UPDATE'])
                is_first_row = False
            else:
                text = row[1]
                positiv, negativ, update = analyze_smileys(text)
                csv_writer.writerow(row + [positiv, negativ, update])
