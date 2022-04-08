# https://www.hackerrank.com/challenges/validating-credit-card-number/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

import re


for _ in range(int(input())):
    try:
        code = input()
        assert re.match(r"^[456]", code)

        # with '-'
        if len(code) == 19:
            code = code.split("-")
            for i in code:
                assert len(i) == 4
            code = "".join(code)

        assert not re.search(r"(.)\1{3,}", code)
        assert re.match(r"\d", code)
        assert len(code) == 16
        print("Valid")

    except:
        print("Invalid")
