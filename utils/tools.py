def open_file(fn):
    with open(fn, "r", encoding="utf8") as f:
        rtn = "".join(f.readlines())
        return rtn
