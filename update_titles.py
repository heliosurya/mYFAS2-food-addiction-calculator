import re, os

# Run from the project root
files = [
    ('Yale-Food-Addiction-Scale-2.0-Full-25-Item.html',
     'Yale Food Addiction Scale 2.0 (Full 25-Item)',
     'Yale Food Addiction Scale 2.0 - full 25-item assessment based on DSM-5 criteria'),
    ('YFAS-C-2.0-Children-18-Item.html',
     'Yale Food Addiction Scale for Children 2.0 (18-Item)',
     'Yale Food Addiction Scale for Children 2.0 - 18-item version'),
    ('dYFAS-C-2.0-Dimensional-15-Item.html',
     'Dimensional YFAS-C 2.0 (15-Item)',
     'Dimensional Yale Food Addiction Scale for Children 2.0 - 15-item'),
    ('mYFAS-C-2.0-Children-13-Item.html',
     'Modified YFAS-C 2.0 (13-Item)',
     'Modified Yale Food Addiction Scale for Children 2.0 - 13-item'),
    ('AEFS-Anticipated-Effects-of-Food.html',
     'Anticipated Effects of Food Scale (AEFS)',
     'Anticipated Effects of Food Scale - food expectancies for highly processed foods'),
    ('ProWS-Highly-Processed-Food-Withdrawal.html',
     'Highly Processed Food Withdrawal Scale (ProWS)',
     'Highly Processed Food Withdrawal Scale (ProWS) - 31-item assessment'),
    ('mYFAS-2.0-Brief-13-Item.html',
     'Modified YFAS 2.0 (13-Item)',
     'Modified Yale Food Addiction Scale 2.0 - brief 13-item version'),
]

for filename, new_title, new_desc in files:
    with open(filename, 'r') as f:
        content = f.read()

    content = re.sub(r'<title>.*?</title>', '<title>' + new_title + '</title>', content, flags=re.DOTALL)
    content = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="' + new_desc + '. Source: https://sites.lsa.umich.edu/fastlab/yale-food-addiction-scale/">', content)

    with open(filename, 'w') as f:
        f.write(content)

    print('Updated: ' + filename)
print('Done')
