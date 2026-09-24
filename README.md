# Greeter

This is a small Python web application that displays a greeting message.

The application uses Python's built-in http.server module and runs on port 8080.

## Build Docker Image

```bash
docker build -t greeter:1.0 .
```

## Run Docker Container

```bash
docker run -d --name greeter-container -p 8080:8080 greeter:1.0
```

Open the application in a browser:

http://localhost:8080
