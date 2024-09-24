import re


phone_numbers = [
    "(123) 456-7890",
    "1234567890",
    "123.456.7890",
    "+1 123 456-7890"
]

new_mumbers = []

R = re.compile(r"\d")

for number in phone_numbers:
    digits = R.findall(number)

    area_code = "".join(digits[-10:-7])
    first_3 = "".join(digits[-7:-4])
    last_4 = "".join(digits[-4:len(digits)])

    pretty_format = f"({area_code}) {first_3}-{last_4}"
    new_mumbers.append(pretty_format)

print(new_mumbers)
