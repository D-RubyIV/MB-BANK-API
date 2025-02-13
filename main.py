import json
import requests


url = "https://online.mbbank.com.vn/api/retail-transactionms/transactionms/get-account-transaction-history"
accountNo = "010268850000"
fromDate = "06/02/2025"
toDate = "13/02/2025"

payload = {
    "accountNo": accountNo,
    "fromDate": fromDate,
    "toDate": toDate,
    "sessionId": sessionId,
    "refNo": refNo,
    "deviceIdCommon": deviceIdCommon
}
headers = {
    "authority": "online.mbbank.com.vn",
    "method": "POST",
    "path": "/api/retail-transactionms/transactionms/get-account-transaction-history",
    "scheme": "https",
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "app": "MB_WEB",
    "authorization":authorization ,
    "content-type": "application/json; charset=UTF-8",
    "origin": "https://online.mbbank.com.vn",
    "priority": "u=1, i",
    "referer": "https://online.mbbank.com.vn/information-account/source-account",
    "refno":refNo,
    "sec-ch-ua":'"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"',
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":'"Windows"',
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-origin",
    "deviceid": deviceIdCommon,
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
}
response = requests.post(
    url=url,
    headers=headers,
    data=json.dumps(payload)
)
print(json.dumps(response.json(), indent=4))