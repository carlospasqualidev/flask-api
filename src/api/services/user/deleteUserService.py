from prisma import Prisma


async def deleteUserService(id):
    db = Prisma()
    await db.connect()

    await  db.users.delete(
        where={
            'id': id
        }
    )

    await db.disconnect()

    return  
