runtime: python311 # or another supported version

instance_class: F2

env_variables:
  BUCKET_NAME: "example-gcs-bucket"

handlers:
# Matches requests to /images/... to files in static/images/...
- url: /images
  static_dir: static/images

- url: /.*
  secure: always
  redirect_http_response_code: 301
  script: auto
