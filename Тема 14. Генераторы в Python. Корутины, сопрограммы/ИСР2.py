# Разработать программу, позволяющую генерировать уникальные идентификаторы: UUID

import random
from hashlib import md5
import datetime

def get_uuid():
    hl1 = md5()
    hl1.update(str(datetime.datetime.now()).encode("iso-8859-1"))

    hl2 = md5()
    hl2.update(str(random.randint(0,1e8)).encode("iso-8859-1"))

    dg = hl1.hexdigest()+hl2.hexdigest()

    return f"{dg[0:8]}-{dg[8:12]}-{dg[12:16]}-{dg[-16:-12]}-{dg[-12:]}"

uuids = []

result = get_uuid()
uuids.append(result)
print(result)