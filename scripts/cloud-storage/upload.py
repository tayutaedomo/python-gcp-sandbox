"""
  Reference: https://qiita.com/Hyperion13fleet/items/594c15ac24f149ab73c9
"""
import sys
from google.cloud import storage as gcs
from google.oauth2 import service_account


if __name__ == '__main__':
  key_path = sys.argv[1]
  project_id = sys.argv[2]
  bucket_name = sys.argv[3]
  gcs_path = sys.argv[4]
  local_path = sys.argv[5]

  credential = service_account.Credentials.from_service_account_file(key_path)
  client = gcs.Client(project_id, credentials=credential)
  bucket = client.get_bucket(bucket_name)
  blob_gcs = bucket.blob(gcs_path)
  blob_gcs.upload_from_filename(local_path)
