# RASA FRENCH VOCAL BOT PROTOTYPE

This project consists of building an End-to-end vocal bot using rasa, fastapi and react.js.

## Prerequisites
python == 3.8.x
Node.js == v16.x
npm == 8.11.0


## Setup environments

- Clone the repository in your project folder
- Install pipenv for python virtual environment management [link](https://pipenv.pypa.io/en/latest/)
- Create python virtual env and install all python dependencies list in the `Pipfile` run the following command
```
pipenv install
```

- Go to the frontend directory
- Install node packages dependencies run the following command
```
npm install
```

## Steps to launch

Now, we have to respectively start the rasa server in the backend folder, the api server in the voice-api folder and launch the react.js server in the frontend to use the app.

1. Run rasa server

- Go to the backend directory
- Open a new terminal
- Then run the following command

```
rasa run -m models --enable-api --cors '*' --port 5002
```

2. Run voice-api server

- Go to the voice-api directory
- Open a new terminal
- Then run the following command

```
uvicorn src.main:app
```

2. Run react server

- Go to the frontend directory
- Open a new terminal
- Then run the following command

```
npm start
```

## How to use
After launching the react server, go to localhost:3000 in your browser.
Then, enjoy :sunglasses: !
