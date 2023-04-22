from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open('./data.json', 'r') as file:
        data = json.load(file)
    return data

@app.get("/")
def get_data():
    data = load_data()
    return data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
