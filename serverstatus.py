from mcstatus import MinecraftServer

try:
    server = MinecraftServer("ip adress of server", 25565)

    status = server.status()
    online = status.players.online

    print(f"there are currently {online}/{status.players.max} players online on {status.description}\n")
    print("version: " + status.version.name)
    print(f"ping: {status.latency} ms\n")

    if(online != 0):
        print("players online: ")
        for i in status.players.sample:
            print(i.name)
except:
    print("server is offline")


input()
