IPv4_STRING = "127.0.0.1"
IPv4_INVALID_STRING = "300.0.0.1"
IPv6_STRING = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
IPv6_INVALID_STRING = "2001:0db8:85a3:0000:0000:8a2e:0370:7334:7334"
INVALID_IP_STRING = "Error"

# Create a functions to validate IPv4 and IPv6 addresses.
# The print_result function should print the result of the IP validation.

def is_valid_IPv4_octet(octet: str):
    return 0 <= int(octet) <= 255


def is_valid_IPv4(ip: str):
    for octet in ip.split("."):
        if not is_valid_IPv4_octet(octet):
            return False
    return True


def is_valid_IPv6_hextet(hextet: str):
    return 0 <= int(hextet, 16) < int("ffff", 16)


def is_valid_IPv6(ip: str):

    # if split by more than 7 colons, it's invalid
    if ip.count(":") == 7:
        for hextet in ip.split(":"):
            if not is_valid_IPv6_hextet(hextet):
                return False
            return True
    else:
        return False


def is_valid_IP(ip: str):
    # identify if the IP is IPv4 or IPv6
    if (":") in ip and ip.count(":") == 7:
        return is_valid_IPv6(ip)
    elif "." in ip and ip.count(".") == 3:
        return is_valid_IPv4(ip)
    else:
        return False


# The following line calls the function which will print # value to the Console.
# This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(f"IP String {IPv4_STRING} is a valid IP Address:", is_valid_IP(IPv4_STRING))
print(
    f"IP String {IPv4_INVALID_STRING} is a valid IP Address:",
    is_valid_IP(IPv4_INVALID_STRING),
)
print(f"IP String {IPv6_STRING} is a valid IP Address:", is_valid_IP(IPv6_STRING))
print(
    f"IP String {IPv6_INVALID_STRING} is a valid IP Address:",
    is_valid_IP(IPv6_INVALID_STRING),
)
print(
    f"IP String {INVALID_IP_STRING} is a valid IP Address:",
    is_valid_IP(INVALID_IP_STRING),
)

#IP String 127.0.0.1 is a valid IP Address: True
#IP String 300.0.0.1 is a valid IP Address: False
#IP String 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid IP Address: True
#IP String 2001:0db8:85a3:0000:0000:8a2e:0370:7334:7334 is a valid IP Address: False
#IP String Error is a valid IP Address: False