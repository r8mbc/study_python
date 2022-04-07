# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem?isFullScreen=true


def fun(s):
    # return True if s is a valid email, else return False
    import re

    return bool(re.match(r"^[\w\-]+@[a-zA-Z0-9]+\.[a-zA-Z]{,3}$", s))


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == "__main__":
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
