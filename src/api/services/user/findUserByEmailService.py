from prisma import Prisma

async def findUserByEmailService(email):
    db = Prisma()
    await db.connect()



    user = await db.users.find_first(
    where={
        'email': email,
    })

    await db.disconnect()

    return user
  
