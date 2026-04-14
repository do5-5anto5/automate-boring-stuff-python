import ezsheets

ss = ezsheets.Spreadsheet('https://autbor.com/boringcoin')

sheet = ss.sheets[0]

accounts = {}

for row in sheet.getRows():
    sender = row[0]
    recipient = row[1]
    amount = int(row[2])

    if sender == 'PRE-MINE':
        # The 'PRE-MINE' sender invents money out of thin air
        accounts.setdefault(recipient, 0)
        accounts[recipient] += amount
    else:
        accounts.setdefault(sender, 0)
        accounts.setdefault(recipient, 0)
        accounts[sender] -= amount
        accounts[recipient] += amount

total = 0

for amount in accounts.values():
    total += amount

print(accounts)
print('Total Boringcoins: ' + str(total))
