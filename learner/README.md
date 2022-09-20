# learner

## How to launch local on your own machine

Start web server on [localhost:3001](http://127.0.0.1:3001)
```bash
    uvicorn main:app --reload
```

#

## How to launch with docker

Build image based on Dockerfile
```
docker build .
```

Run container locally
```
docker run -d -p 3001:3001 <IMAGE_ID>
```

#

Example of request for downloading init image data set:
```curl
curl 'http://<ENDPOINT>/download-image-set' \
  -X 'POST' \
  -H 'Accept: */*' \
  -H 'Access-Control-Allow-Origin: *' \
  -H 'Connection: keep-alive' \
  -H 'Content-Length: 0' \
  -H 'Content-Type: application/json' \
  -H 'Origin: null' \
  --compressed \
  --insecure
```

Example of request for starting the learner:
```curl
curl 'http://<ENDPOINT>/export-model' \
  -X 'POST' \
  -H 'Accept: */*' \
  -H 'Access-Control-Allow-Origin: *' \
  -H 'Connection: keep-alive' \
  -H 'Content-Length: 0' \
  -H 'Content-Type: application/json' \
  -H 'Origin: null' \
  --compressed \
  --insecure
```
