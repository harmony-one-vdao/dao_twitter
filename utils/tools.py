def open_file(fn):
    with open(fn, "r", encoding="utf8") as f:
        data = f.readlines()
        # print(data)
        rtn = "".join(data)
        return rtn
