def isValidWalk(walk):
    #determine if walk is valid
    print(walk)
    if len(walk) != 10:
        return 0
    elif walk.count('w') != walk.count('e'):
        return 0;
    elif walk.count('n') != walk.count('s'):
        return 0;
    else:
        return 1;
