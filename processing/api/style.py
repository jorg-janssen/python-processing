from ..core.constants import LEFT, RIGHT, CENTER, TOP, BOTTOM, BASELINE


def fill(state, r, g=None, b=None):
    state["_fill_enabled"] = True
    if g is None:
        state["_fill_color"] = (int(r), int(r), int(r))
    else:
        state["_fill_color"] = (int(r), int(g), int(b))


def no_fill(state):
    state["_fill_enabled"] = False


def stroke(state, r, g=None, b=None):
    state["_stroke_enabled"] = True
    if g is None:
        state["_stroke_color"] = (int(r), int(r), int(r))
    else:
        state["_stroke_color"] = (int(r), int(g), int(b))


def no_stroke(state):
    state["_stroke_enabled"] = False


def stroke_weight(state, w):
    state["_stroke_weight"] = int(w)


def color(r, g=None, b=None, a=None):
    if g is None:
        return (int(r), int(r), int(r))
    col = (int(r), int(g), int(b))
    if a is not None:
        col = (*col, int(a))
    return col


def text_size(state, sz):
    state["_text_size"] = int(sz)
    state["_font"] = None


def parse_text_align(value, axis):
    if axis == "x":
        if value in (LEFT, CENTER, RIGHT):
            return value
        x_map = {"LEFT": LEFT, "CENTER": CENTER, "RIGHT": RIGHT}
        key = str(value).upper()
        if key in x_map:
            return x_map[key]
        raise ValueError("text_align() x alignment must be LEFT, CENTER, or RIGHT")

    if value in (TOP, CENTER, BOTTOM, BASELINE):
        return value
    y_map = {"TOP": TOP, "CENTER": CENTER, "BOTTOM": BOTTOM, "BASELINE": BASELINE}
    key = str(value).upper()
    if key in y_map:
        return y_map[key]
    raise ValueError("text_align() y alignment must be TOP, CENTER, BOTTOM, or BASELINE")


def text_align(state, align_x, align_y=None):
    state["_text_align_x"] = parse_text_align(align_x, "x")
    if align_y is not None:
        state["_text_align_y"] = parse_text_align(align_y, "y")
