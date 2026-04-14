import ezsheets, sys

ss = ezsheets.Spreadsheet('1eYLqkmdZFQRQrSm3mJyBvkMrIcmnbCfLNBa92FO-LEg')
sheet = ss.sheets[0]

if len(sys.argv) < 4:
    print("Usage: python exercises\\google-sheets\\fake-blockchain\\add-boringcoin-transaction.py sender recipient amount")
    sys.exit()

sender, recipent, amount = sys.argv[1:]

sheet[1, sheet.rowCount] = sender
sheet[2, sheet.rowCount] = recipent
sheet[3, sheet.rowCount] = amount