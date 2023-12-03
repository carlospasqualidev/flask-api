from prisma import Prisma

async def checkEmailAlredyUsedService(email):
    db = Prisma()
    await db.connect()



    user = await db.users.find_first(
    where={
        'email': email,
    })

    if (user):
        raise ValueError("Email já cadastrado")

    await db.disconnect()

    return user
  
