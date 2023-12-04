from prisma import Prisma

async def updateUserService(id,email, password):
    db = Prisma()
    await db.connect()

    user = await  db.users.update(
        data={  
            "email": email,
            "password": password,
        },
        where={
            'id': id
        }
    )

    await db.disconnect()

    return user
  
