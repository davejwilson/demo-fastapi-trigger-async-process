from fastapi import FastAPI

import threading
import time

app = FastAPI()

def thread_function(name):
    print( 'Thread {}: is writing to data lake'.format(name) )
    # simluate writing to the lake
    time.sleep(5)
    print( "Thread {}: finished writing to data lake".format(name) )

@app.get("/predict")
def log_model_prediction():
    print("entering logging api")

    # trigger the data lake writing
    x = threading.Thread(target=thread_function, args=(1,))
    x.start()

    print("exiting logging api")
    return {"prediction": "The world will end on 70 days"}
