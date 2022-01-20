HEAD
def are_valid_groups(studentNumbers, groups):
    for sNum in studentNumbers:
        found = False
        for group in groups:
            if sNum in group:
                found = True
        if not found:
            return False
    return True
f4ce5dcaf96143384d82bbc730a832e97c11f9d9
