import datetime


def policy():
    china_now = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    if china_now.time() <= datetime.time(12, 00):
        return True
    else:
        return False
