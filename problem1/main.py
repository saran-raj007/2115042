from fastapi import FastAPI
import requests

evenurl="http://20.244.56.144/test/even"
randurl="http://20.244.56.144/test/rand"
primeurl="http://20.244.56.144/test/primes"
fiburl="http://20.244.56.144/test/fibo"




headers = {
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzE4ODYwMTI1LCJpYXQiOjE3MTg4NTk4MjUsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjY2YWQ2Y2Q1LTJjYmMtNGFiOS05MDc4LTQzOThlY2NiMGMyOSIsInN1YiI6IjIxMTUwNDJAbmVjLmVkdS5pbiJ9LCJjb21wYW55TmFtZSI6IlNSIGNvbXBhbnkiLCJjbGllbnRJRCI6IjY2YWQ2Y2Q1LTJjYmMtNGFiOS05MDc4LTQzOThlY2NiMGMyOSIsImNsaWVudFNlY3JldCI6Ikp3bFlET1dZa1h4ZkppTVoiLCJvd25lck5hbWUiOiJTYXJhbnJhaiBLIiwib3duZXJFbWFpbCI6IjIxMTUwNDJAbmVjLmVkdS5pbiIsInJvbGxObyI6IjIxMTUwNDIifQ.DSGGB_Z2stGo7WmeXnFaLXti3U6nSBHJDLhZyN_HFlU',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

app=FastAPI()
window=[]


@app.get("/number/e")
def avgnum():
    response=requests.get(evenurl,headers=headers)
    print(response)
    
    server_res=response.numbers
    prev_window=window
    for i in server_res:
        if len(window)==10:
            window.pop(0)
        window.append(i)
    avg=int((sum(window)/len(window)))
    return{
        "numbers" :server_res,
        "windowPrevState": prev_window,
        "windowCurrState" :window,
        "avg" :avg
    }
    


@app.get("/number/p")
def avgnum():
    response=requests.get(primeurl,headers=headers)
    print(response)
    
    server_res=response.numbers
    prev_window=window
    for i in server_res:
        if len(window)==10:
            window.pop(0)
        window.append(i)
    avg=int((sum(window)/len(window)))
    return{
        "numbers" :server_res,
        "windowPrevState": prev_window,
        "windowCurrState" :window,
        "avg" :avg
    }
    

@app.get("/number/r")
def avgnum():
    response=requests.get(randurl,headers=headers)
    print(response)
    
    server_res=response.numbers
    prev_window=window
    for i in server_res:
        if len(window)==10:
            window.pop(0)
        window.append(i)
    avg=int((sum(window)/len(window)))
    return{
        "numbers" :server_res,
        "windowPrevState": prev_window,
        "windowCurrState" :window,
        "avg" :avg
    }
    

@app.get("/number/f")
def avgnum():
    response=requests.get(fiburl,headers=headers)
    print(response)
    
    server_res=response.numbers
    prev_window=window
    for i in server_res:
        if len(window)==10:
            window.pop(0)
        window.append(i)
    avg=int((sum(window)/len(window)))
    return{
        "numbers" :server_res,
        "windowPrevState": prev_window,
        "windowCurrState" :window,
        "avg" :avg
    }