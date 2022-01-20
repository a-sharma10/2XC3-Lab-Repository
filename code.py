def are_valid_groups(sNums, groups):
    for sNum in sNums:
        found = False
        for group in groups:
            if sNum in group:
                found = True
        if not found:
            return False
    return True