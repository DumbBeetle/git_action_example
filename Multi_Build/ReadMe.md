### Build specific stage
docker build --target builder -t flask-app . 
docker build -t flask-app . 

### Run the pod
docker run -it --rm -p 8080:8000 flask-app

### Override the STAGE ENV
docker run -it --rm -p 8080:8000 -e STAGE=Override flask-app:latest

### cleanup
docker rmi flask-app