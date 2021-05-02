import json

import requests
uid= "8824"
token_id = "1coYz1QadIuDaIU2"
base_url = f"https://www.stands4.com/services/v2/lyrics.php?uid={uid}&tokenid={token_id}&term=forever%20young&artist=Alphaville&format=json"

respose = requests.get(base_url)

json.dumps(respose.json())


"""f = open(f"demofile2.json", "a")
f.write()
f.close()"""