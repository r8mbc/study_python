# https://www.hackerrank.com/challenges/validating-postalcode/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

regex_integer_in_range = r"^(\d)(\d){5}$"  # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"  # Do not delete 'r'.


import re

P = input()

print(
    bool(re.match(regex_integer_in_range, P))
    and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2
)
