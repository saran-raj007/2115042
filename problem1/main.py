from fastapi import FastAPI
import requests

# evenurl="http://20.244.56.144/test/even"
# randurl="http://20.244.56.144/test/rand"
# primeurl="http://20.244.56.144/test/primes"
# fiburl="http://20.244.56.144/test/fibo"




# headers = {
#     'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzE4ODY2NDM4LCJpYXQiOjE3MTg4NjYxMzgsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjY2YWQ2Y2Q1LTJjYmMtNGFiOS05MDc4LTQzOThlY2NiMGMyOSIsInN1YiI6IjIxMTUwNDJAbmVjLmVkdS5pbiJ9LCJjb21wYW55TmFtZSI6IlNSIGNvbXBhbnkiLCJjbGllbnRJRCI6IjY2YWQ2Y2Q1LTJjYmMtNGFiOS05MDc4LTQzOThlY2NiMGMyOSIsImNsaWVudFNlY3JldCI6Ikp3bFlET1dZa1h4ZkppTVoiLCJvd25lck5hbWUiOiJTYXJhbnJhaiBLIiwib3duZXJFbWFpbCI6IjIxMTUwNDJAbmVjLmVkdS5pbiIsInJvbGxObyI6IjIxMTUwNDIifQ.UNyUeLJL3yvaXJZrfN9L-7wdDZ68HsIWnv9A88olI7w',
    
# }


app=FastAPI()

window=[]


@app.get("/number/e")
def avgnum():
   
    
   
    server_res=[26,
        28,
        30,
        32,
        34]
    prev_window=window.copy()
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
    
    
    
    server_res=[47,
        53,
        59,
        61,
        67]
    prev_window=window.copy()
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
    
    
    server_res=[22,
        20,
        9,
        6,
        15,
        12,
        2,
        19,
        25,
        7,
        4]
    prev_window=window.copy()
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
    
    server_res=[377,
        610,
        987,
        1597,
        2584,
        4181,
        6765,
        10946,
        17711,
        28657,
        46368]
    prev_window=window.copy()
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