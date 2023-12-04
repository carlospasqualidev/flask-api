from prisma import Prisma

async def findUserByIdService(id):
    db = Prisma()
    await db.connect()

    user = await db.users.find_first(
    where={
        'id': id,
    })

    await db.disconnect()

    return user
  
