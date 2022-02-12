# fastapi-chat-redis
A mook chat application to broadcast messages using Redis

Use docker to create a redis container
then run the following command to start the redis container

[]: # docker run -d -p 6379:6379 --name redis redis

After that run the following command to start the chat application

[]: # uvicorn app:app --reload

Next run the following command to start the chat client

[]: # python3 -m http.server --directory . 9000

    
    []: # Language: python
    []: # Path: app.py

that's all folks!
