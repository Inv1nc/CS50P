def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        ipaddress = list(map(int,ip.split(".")))
        if not len(ipaddress) == 4:
            return False
        for number in ipaddress:
            if number>255:
                return False
    except ValueError:
        return False
    else:
        return True


if __name__ == "__main__":
    main()
