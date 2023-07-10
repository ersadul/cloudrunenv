# docker build -t nama_image:tag .

# gcloud builds submit \
#    --tag gcr.io/$GOOGLE_CLOUD_PROJECT/{containername:tag}

gcloud builds submit \
  --tag gcr.io/$GOOGLE_CLOUD_PROJECT/flask-app:0.1

