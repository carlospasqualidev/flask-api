from prisma import Prisma

async def createMusicService(dance,energy,key,speech,acoustic,instrumental,time,name,popularity,userId):
    db = Prisma()
    await db.connect()

    music = await  db.musics.create({      
        "dance": dance,
        "energy": energy,
        "key": key,
        "speech": speech,
        "acoustic": acoustic,
        "instrumental": instrumental,
        "time": time,
        "name":name,
        "popularity":popularity,
        "userId":userId,
    })

    await db.disconnect()

    return {
        "id": music.id,
        "dance": float(music.dance),
        "energy":float(music.energy),
        "key":float(music.key),
        "speech":float(music.speech),
        "acoustic": float(music.acoustic),
        "instrumental":float(music.instrumental),
        "time": float(music.time),
        "name": music.name,
        "popularity":float(music.popularity),
        "userId":userId
    }
  
