def formatted_numbers():
    list = []
    list.append("|{:^10}|{:^10}|{:^10}|".format('decimal', 'hex', 'binary'))
    for i in range(16):
        list.append("|{:<10}|{:^10}|{:>10}|".format(
            i, str(hex(i)[2:]), str(bin(i)[2:])))
    return list