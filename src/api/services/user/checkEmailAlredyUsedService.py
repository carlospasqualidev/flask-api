from prisma import Prisma

async def checkEmailAlredyUsedService(email, id = None):
    db = Prisma()
    await db.connect()


    where = {
        'email': email,
    }

    if id is not None:
     where={
        'email': email,
        'id': {
            'not': id
        }
    }
    

    user = await db.users.find_first(where=where)
        
    await db.disconnect()

    return user
  
