import re

input_text = """
google.com, facebook.com, youtube.com
"""

domains = re.findall(r'https?://(www\.)?([^/]+)', input_text)
domains = set([domain[1] for domain in domains])

domains = set([re.split(r'/+', domain.strip())[0] for domain in input_text.split(',')])

# Print
for domain in sorted(domains):
    print(domain)
