import os
import atexit

lockname = "pushsmstimeing.lock"

def init():
    try:
        os.open(lockname, os.O_CREAT|os.O_EXCL)
        import atexit
        atexit.register(lambda : os.remove(lockname))
    except Exception, e:
        raise e

