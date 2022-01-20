def are_valid_groups(studentNumbers, groups):
    studentNumbersAux = []
    for i in range(0, len(studentNumbers)):
        studentNumbersAux.append(False)
    for i in range(0, len(studentNumbers)):
        for j in range(0, len(groups)):
            if (studentNumbers[i] in groups[j]):
                studentNumbersAux[i] = True
    if (False in studentNumbersAux):
        return False
    else:
        return True
