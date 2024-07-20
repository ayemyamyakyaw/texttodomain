import re

# Input string
input_text = """
google.com, facebook.com, youtube.com
"""

# Extract domains
domains = re.findall(r'https?://(www\.)?([^/]+)', input_text)
domains = set([domain[1] for domain in domains])

# Alternatively, split by comma and remove subdirectories
domains = set([re.split(r'/+', domain.strip())[0] for domain in input_text.split(',')])

# Print each domain on a new line
for domain in sorted(domains):
    print(domain)
