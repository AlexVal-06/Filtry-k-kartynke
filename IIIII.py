alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]


def check(a):
    try:
        for i in a[:a.find('@')].replace('@', '').replace('.', ''):
            if i not in alphabet:
                return False

        for i in a[a.rfind('.') + 1:]:
            if i.isdigit():
                return False
        for i in range(0, len(a)):
            if a[i] == '@':
                if a[i - 1] in alphabet and a[i - 2] in alphabet and a[i + 1] in alphabet and a[i + 2] in alphabet:
                    pass
                else:
                    return False

        if '@' in a and '.' in a:
            if '.' in a[a.find('@'):] and len(a[:a.find('@')]) >= 4:
                if len(a[a.rfind('.') + 1:]) >= 2 and len(a[a.rfind('.') + 1:]) <= 4:
                    return True

        return False

    except Exception:
        return False
