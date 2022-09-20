# inferencer

## How to launch local on your own machine

Start web server on [localhost:3000](http://127.0.0.1:3000)
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
docker run -d -p 3000:3000 <IMAGE_ID>
```

#

Example of request:
```curl
curl 'http://<ENDPOINT>/classify-image' \
  -H 'Accept: */*' \
  -H 'Access-Control-Allow-Origin: *' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  --data-raw '{"image": <BASE64_IMAGE>}'
  --compressed \
  --insecure
```
