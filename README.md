# python-gcp-sandbox
Try Google Cloud Platform APIs with Python


## Setup
```
$ git clone git@github.com:tayutaedomo/python-gcp-sandbox.git
$ cd python-gcp-sandbox
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

## Scripts
### scripts/youtube/search.py
```
$ export GCP_YOUTUBE_DEVELOPER_KEY=<Your developer key>
```

## scripts/cloud-storage/upload.py
```
$ scripts/cloud-storage/upload.py <Credential path> <Project ID> <Bucket name> <GCS path> <File path>
```
