import re

phone_numbers = [
    "(123) 456-7890",
    "1234567890",
    "123.456.7890",
    "+1 123 456-7890"
]

class PhoneFormatter:
    def __init__(self):
        self.r = re.compile(r"\d")

    def pretty_format(self, phone_number):
        phone_numbers = self.r.findall(phone_number)
        area_code = "".join(phone_numbers[-10:-7])
        first_3 = "".join(phone_numbers[-7:-4])
        last_4 = "".join(phone_numbers[-4:len(phone_numbers)])
        return f"({area_code}) {first_3}-{last_4}"

p = PhoneFormatter()
print(list(map(p.pretty_format, phone_numbers)))
