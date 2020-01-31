import serial, requests, json, time

verdieping = {"1":"0", "2": "0", "3": "0", "4": "0"}

url = "https://huparkingappapi.azurewebsites.net/api/parkingspots"
data = {"PlekId":0, "Verdieping": 0, "Bezet": False}
headers = {"apiKey": "abcdef123456", "Content-Type": "application/JSON"}

print(requests.put(url, data=json.dumps(data), headers=headers).text)

arduino = serial.Serial('COM5', 115200, timeout=.1)
arduion1 = serial.Serial('COM4', 115200, timeout=.1)
while True:
    data = arduino.readline().decode("utf-8")
    data1 = arduion1.readline().decode("utf-8")
    if data and data1:
        bezet = data.split(",")
        bezet1 = data1.split(",")
        print(data)
        print(data1)
        # verdieping[bezet1[0]] = bezet1[1]
        if bezet[0][-1] == " ":
            bezet[0] = int(bezet[0])
            bezet[0] = str(bezet[0])
        if bezet1[0][-1] == " ":
            bezet1[0] = int(bezet1[0])
            bezet1[0] = str(bezet1[0])
        # print(bezet[1])
        # print(verdieping[bezet[0]])
        if bezet[0] == "1":
            if bezet[1] == "0":
                data = {"PlekId": 0, "Verdieping": 0, "Bezet": False}
                print(data)
                print(requests.put(url, data=json.dumps(data), headers=headers).text)
            else:
                data = {"PlekId": 0, "Verdieping": 0, "Bezet": True}
                print(data)
                print(requests.put(url, data=json.dumps(data), headers=headers).text)
        elif bezet[0] == "2":
            if bezet[1] == "0":
                data = {"PlekId": 1, "Verdieping": 0, "Bezet": False}
                print(data)
                print(requests.put(url, data=json.dumps(data), headers=headers).text)
            else:
                data = {"PlekId": 1, "Verdieping": 0, "Bezet": True}
                print(data)
                print(requests.put(url, data=json.dumps(data), headers=headers).text)
        if bezet1[0] == "3":
            if bezet1[1] == "0":
                data = {"PlekId": 2, "Verdieping": 0, "Bezet": False}
                print(data)
                print(requests.put(url, data=json.dumps(data), headers=headers).text)
            else:
                data = {"PlekId": 2, "Verdieping": 0, "Bezet": True}
                print(data)
                print(requests.put(url, data=json.dumps(data), headers=headers).text)
        elif bezet1[0] == "4":
            if bezet1[1] == "0":
                data = {"PlekId": 3, "Verdieping": 0, "Bezet": False}
                print(data)
                print(requests.put(url, data=json.dumps(data), headers=headers).text)
            else:
                data = {"PlekId": 3, "Verdieping": 0, "Bezet": True}
                print(data)

                print(requests.put(url, data=json.dumps(data), headers=headers).text)
