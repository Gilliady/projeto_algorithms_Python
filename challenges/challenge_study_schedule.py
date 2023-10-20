def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    count = 0
    for element in permanence_period:
        start, end = element
        if not isinstance(start, int) or not isinstance(end, int):
            count = None
            break
        if target_time in range(element[0], element[1] + 1):
            count += 1
    return count
