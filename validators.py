def validate_email(address):
    import re
    return bool(re.match(r'[^@]+@[^@]+\.[^@]+', address))
