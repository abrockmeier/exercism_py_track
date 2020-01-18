def convert(number):
    primfac = [3,5,7]
    output = ''
    for item in primfac:
        if item == 3 and number % item == 0:
            output += 'Pling'
        if item == 5 and number % item == 0:
            output += 'Plang'
        if item == 7 and number % item == 0:
            output += 'Plong'
    if output == '':
        return str(number)
    else:
        return output
