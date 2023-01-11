data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designations = []
codes = []
for i in data:
    if i[0] == '0':
        codes.append(i)
    else:
        designations.append(i)
operators = dict()
i = 0
while i < len(codes):
    operators[designations[i]] = {codes[i]}
    i += 1

del operators["Katel"]
del operators["Fonex"]

operators["O!"].add('0700')
operators["Megacom"].add('0999')
operators["Beeline"].add('0222')
operators["Beeline"].add('0777')
operators["Megacom"].add('0555')
operators["O!"].add('0500')
for i in operators:
    print(f'{i} - {operators[i]}')
