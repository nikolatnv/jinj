import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="../templates")   # directory containing template files


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/change_color")
def change_color(request: Request, data: dict):
    command_text = data['command_text']
    # Process command_text to get color name
    # you could use a switch/case or if/elif/else
    if command_text == 'green':
        color_name = '#008000'
    elif command_text == 'on':
        color_name = 'yellow'
    elif command_text == 'off':
        color_name = 'black'
    elif command_text == 'off':
        color_name = '#ffffff'
    elif command_text == 'red':
        color_name = '#ff0000'
    elif command_text == 'blue':
        color_name = '#0000ff'
    else:
        color_name = '#ffffff'
    return templates.TemplateResponse("index.html", {"request": request, "color_name": color_name})


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)

# Templates will be stored in the "templates" directory
# The "index.html" page
