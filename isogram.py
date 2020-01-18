def is_isogram(string):
    if string == "":
        return True
    unicode = [ord(item) for item in string.lower() if 63 < ord(item) < 91 or 96 < ord(item) < 123]
    print(unicode)
    if len(set(unicode)) is len(unicode):
        print(list(set(unicode)))
        return True
    else:
        return False
