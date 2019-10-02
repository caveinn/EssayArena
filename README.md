# EssayArena
A backend that serves an essay writting site

The backend has several endpoinnts that will be highlighted bellow

**Auth**  
For authentication we have the `api/auth/` parent route
this is the extended to `/login/` and `/signup` for login and  
signup respectively

To signup you send a post request to `api/auth/signup/` with the following body

```
"password": <sufficiently secure password>,
"username": < a unique usename>,
"email": <your email adress>,
"role": <the role [CL for client or WR for writer]>
```

to login send post request to `api/auth/login/` with the following data
```
"email": <a registered email>
"password": <the valid password for the email>
```

**Orders**

Clients can access the `api/orders/` mother route

to create an order, post `api/orders/` with
```angular2
"title": <title of the order>,
"body": <body or details of the order>,
"cost": <your budget for the order>,
"files":["first", "second", "third"] <a list of files attached>
```

to list get `api/orders/`

to get one order `api/orders/<id>/`

to update an order update `api/orders/<id>/`


**Websocket**
There is a websocket intergrated for realtime updates for chances
in order and bids

to subscribe to the websocket for orders you need to access the url

`ws://127.0.0.1:8000/ws/orders/`
to subscribe to the websocket for bids you need to access the url

`ws://127.0.0.1:8000/ws/<order_id>/orders/bids/roomn_name`


***more under construction***
