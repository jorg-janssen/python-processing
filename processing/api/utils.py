def random_value(low, high, random_module):
    if low is None and high is None:
        return random_module.random()
    if high is None:
        return random_module.uniform(0.0, float(low))
    return random_module.uniform(float(low), float(high))


def millis_value(state, pygame, time_module):
    if state["_millis_start"] is not None:
        return int(pygame.time.get_ticks() - state["_millis_start"])
    return int(time_module.perf_counter() * 1000)


def nf_format(value, left=0, right=0):
    left = int(left)
    right = int(right)

    number = float(value)
    sign = "-" if number < 0 else ""
    abs_number = abs(number)
    formatted = f"{abs_number:.{max(0, right)}f}"

    if "." in formatted:
        int_part, frac_part = formatted.split(".", 1)
        if left > 0:
            int_part = int_part.zfill(left)
        if right > 0:
            formatted = f"{int_part}.{frac_part}"
        else:
            formatted = int_part
    elif left > 0:
        formatted = formatted.zfill(left)

    return sign + formatted
