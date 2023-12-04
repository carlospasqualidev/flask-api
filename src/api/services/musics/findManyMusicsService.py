from prisma import Prisma

async def findManyMusicsService(id):
    db = Prisma()
    await db.connect()

    musics = await db.musics.find_many(
        where={
            'userId': id,
        }
    )

    await db.disconnect()

    return musics
  
