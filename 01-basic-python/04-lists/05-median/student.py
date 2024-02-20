def median(ns):
    gesorteerd = sorted(ns)
    midden = len(ns) // 2

    if len(ns) % 2 == 0:
        return (gesorteerd[midden - 1] + gesorteerd[midden]) / 2
    else:
        return gesorteerd[midden]