import http.client

conn = http.client.HTTPSConnection("yandextranslatezakutynskyv1.p.rapidapi.com")

payload = "lang=en-es&text=rough"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'X-RapidAPI-Key': "b8b6ebeed5msh8fb6e21c0169f10p12d9fdjsn058326a42489",
    'X-RapidAPI-Host': "YandexTranslatezakutynskyV1.p.rapidapi.com"
}

conn.request("POST", "/translate", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))