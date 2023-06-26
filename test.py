from metaservicesynced.ejabber import *
import pprint
from core.config import EJ_SERVICE, EJ_HOST


data = {
    # "name": room_name,
    "service": EJ_SERVICE,
    # "host": EJ_HOST,
}
res = ej_execute("muc_online_rooms", data)
pprint.pprint(res.json())
