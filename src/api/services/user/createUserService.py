from prisma import Prisma

async def createUserService(email, password):
    db = Prisma()
    await db.connect()


    user = await  db.users.create({
        "email": email,
        "password": password
    })

    await db.disconnect()

    return user
  
