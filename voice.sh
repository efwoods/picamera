#!/bin/sh
echo $1
curl -X POST -u "63348a74-f75b-43b7-b08f-f3c9a68aa8f8:Ghj7Uejo5XFB" --header "Content-Type: application/json" --header "Accept: audio/wav" --data "{\"text\":\"Hey there \"}" --output hello_world.wav "https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize?voice=en-US_AllisonVoice"

