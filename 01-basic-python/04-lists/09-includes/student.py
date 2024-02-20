def includes(xs, ys):
    for x in ys:
        if x not in xs:
            return False
    return True