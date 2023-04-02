import os

import uvicorn
from fastapi import APIRouter, FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from services.home_activities import HomeActivities
from services.user_activities import UserActivities
from services.create_activity import CreateActivity
from services.create_reply import CreateReply
from services.search_activities import SearchActivities
from services.message_groups import MessageGroups
from services.messages import Messages
from services.notifications_activities import NotificationsActivities
from services.create_message import CreateMessage
from services.show_activity import ShowActivities

app = FastAPI()
frontend = os.getenv("FRONTEND_URL")
backend = os.getenv("BACKEND_URL")
origins = [frontend, backend]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter(prefix="/api", tags=["api"])


@router.get("/message_groups")
def data_message_groups():
    user_handle = "andrewbrown"
    model = MessageGroups.run(user_handle=user_handle)
    if model["errors"] is not None:
        return model["errors"], 422
    else:
        return model["data"], 200


@router.get("/messages/{handle}")
def data_messages(handle: str, user_receiver_handle: str):
    model = Messages.run(
        user_sender_handle=handle, user_receiver_handle=user_receiver_handle
    )
    if model["errors"] is not None:
        return JSONResponse(content=model["errors"], status_code=422)
    else:
        return JSONResponse(content=model["data"], status_code=200)


@router.post("/messages")
def data_create_message(user_receiver_handle: str, message: str):
    user_sender_handle = "andrewbrown"

    model = CreateMessage.run(
        message=message,
        user_sender_handle=user_sender_handle,
        user_receiver_handle=user_receiver_handle,
    )
    if model["errors"] is not None:
        return JSONResponse(content=model["errors"], status_code=422)

    return JSONResponse(content=model["data"], status_code=200)


@router.get("/activities/home")
def data_home():
    data = HomeActivities.run()
    return JSONResponse(content=data, status_code=200)


@router.get("/activities/notifications/home")
def data_notifications():
    data = NotificationsActivities.run()
    return JSONResponse(content=data, status_code=200)


@router.get("/activities/{handle}")
def data_handle(handle: str):
    model = UserActivities.run(handle)
    if model["errors"] is not None:
        return JSONResponse(content=model["errors"], status_code=422)
    return JSONResponse(content=model["data"], status_code=200)


@router.get("/activities/search")
def data_search(term: str):
    model = SearchActivities.run(term)
    if model["errors"] is not None:
        return JSONResponse(content=model["errors"], status_code=422)

    return JSONResponse(content=model["data"], status_code=200)


@router.post("/activities")
def data_activities(message: str, ttl: int):
    user_handle = "andrewbrown"
    model = CreateActivity.run(message, user_handle, ttl)
    if model["errors"] is not None:
        return JSONResponse(content=model["errors"], status_code=422)
    return model["data"], 200


@router.get("/activities/{activity_uuid}")
def data_show_activity(activity_uuid: str):
    data = ShowActivities.run(activity_uuid=activity_uuid)
    return JSONResponse(content=data, status_code=200)


@router.post("/activities/<string:activity_uuid>/reply")
def data_activities_reply(activity_uuid: str, message: str):
    user_handle = "andrewbrown"
    model = CreateReply.run(message, user_handle, activity_uuid)
    if model["errors"] is not None:
        return JSONResponse(content=model["errors"], status_code=422)

    return JSONResponse(content=model["data"], status_code=200)


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8004)
