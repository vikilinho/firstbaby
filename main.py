from fastapi import FastAPI
from fastapi import Body


from random import randrange
from registration import Registration


app = FastAPI()

# Define a model for the body of the registration request


users_details = [{"fullName": "Victor ogundola", "age": 28, "email": "dvicxy@gmail.com", "sex": "male",
                  "userID": 1, }, {"fullName": "Andy Ayo", "age": 25, "email": "vic@gmail.com", "sex": "male", "userID": 2, }]

# Define a model for the body of the login request


@app.post("/login")
async def login():
    return {"message": "Welcome"}


@app.post("/register")
async def register(registration: Registration):
    userdata = registration.dict()  # convert the registration object to a dictionary
    userdata["userID"] = randrange(1, 100000)  # generate a random userID
    users_details.append(userdata)
    return {"data": userdata}

 # get users details


@app.get("/user_details")
async def details():

    return {"data": users_details}

# fetch the last user details


@app.get("/user_detail/last_user")
async def last_user_details():

    last_user = users_details[len(users_details)-1]
    print(last_user)
    return {"data": last_user}

# get individual user details by passing the user id.


@app.get("/user_detail/{userID}")
async def user_details(userID: int):
    for user in users_details:
        if user["userID"] == userID:
            return {"data": user}
    return {"message": "User not found"}
