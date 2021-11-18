from fastapi import FastAPI, Response, status, HTTPException
from fastapi import Body


from random import randrange
from registration import Registration
from login import Login


app = FastAPI()

# Define a model for the body of the registration request


users_details = [{"fullName": "Victor ogundola", "age": 28, "email": "dvicxy@gmail.com", "sex": "male",
                  "userID": 1, }, {"fullName": "Andy Ayo", "age": 25, "email": "vic@gmail.com", "sex": "male", "userID": 2, }]

# Define a model for the body of the login request


@app.post("/login", status_code=200,)
async def login(login: Login):

    return {"message": "Welcome"}


@app.post("/register", status_code=201)
async def register(registration: Registration):
    userdata = registration.dict()  # convert the registration object to a dictionary
    userdata["userID"] = randrange(1, 100000)  # generate a random userID
    users_details.append(userdata)
    return {"data": userdata}

 # get users details


@app.get("/user_details")
async def details():

    return {"data": users_details}

# method for finding the index of the list


def find_index(userID):
    for index, user in enumerate(users_details):
        if user["userID"] == userID:
            return index


# method for updating the user details
@app.put("/user_details/{userID}")
async def update_user(userID: int, registration: Registration):
    index = find_index(userID)
    if index is None:
        raise HTTPException(status_code=404, detail="User not found")
    userdata = registration.dict()
    users_details[index] = userdata
    return {"data": userdata}


# delete user details
@app.delete("/user_detail/delete/{userID}", status_code=204,)
async def delete_user_details(userID: int):
    index = find_index(userID)
    if index is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"post with userID: {userID}  does not exist")
    users_details.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# fetch the last user details


@app.get("/user_detail/last_user")
async def last_user_details():

    last_user = users_details[len(users_details)-1]

    return {"data": last_user}

# get individual user details by passing the user id.


@app.get("/user_detail/{userID}")
async def user_details(userID: int):
    for user in users_details:
        if user["userID"] == userID:
            return {"data": user}
        raise HTTPException(status_code=404, detail="User not found")
