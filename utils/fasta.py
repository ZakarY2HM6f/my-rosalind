def parse_fasta(s: str) -> dict[str, str]:
    result = {}

    label = None
    current = ""
    for l in s.splitlines():
        if l[0] == ">":
            if label:
                result[label] = current
                current = ""
            label = l[1:]
        elif label:
            current += l

    if label:
        result[label] = current

    return result