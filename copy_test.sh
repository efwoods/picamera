#!/bin/sh
curl -X POST -u "apikey:EyXqAzJDlot3MJWc7nLSYHUqANe9jppChT9X8l8QyWNj" -F "images_file=@example.jpg" "https://gateway.watsonplatform.net/visual-recognition/api/v3/detect_faces?version=2018-03-19"
