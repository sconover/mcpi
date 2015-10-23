from connection import Connection
from vec3 import Vec3
from event import BlockEvent, ChatEvent
from block import Block
from entity import Entity
import math
from util import flatten, dict_to_api_string

""" Minecraft PI low level api v0.1_1

    Note: many methods have the parameter *arg. This solution makes it
    simple to allow different types, and variable number of arguments.
    The actual magic is a mix of flatten_parameters() and __iter__. Example:
    A Cube class could implement __iter__ to work in Minecraft.setBlocks(c, id).

    (Because of this, it's possible to "erase" arguments. CmdPlayer removes
     entityId, by injecting [] that flattens to nothing)

    @author: Aron Nieminen, Mojang AB

    Updated to included additional functionality provided by RaspberryJuice:
    - getBlocks() : implemented
    - .create() : can now accept "name" (player name) for use in multiplayer
    - CmdPositioner.getDirection
    - CmdPositioner.getPitch
    - CmdPositioner.getRotation
    - getPlayerEntityId
    - CmdEvents.pollChatPosts
    """


def intFloor(*args):
    return [int(math.floor(x)) for x in flatten(args)]

class CmdPositioner:
    """Methods for setting and getting positions"""
    def __init__(self, connection, packagePrefix):
        self.conn = connection
        self.pkg = packagePrefix

    def getPos(self, id):
        """Get entity position (entityId:int) => Vec3"""
        s = self.conn.sendReceive(self.pkg + ".getPos", id)
        return Vec3(*map(float, s.split(",")))

    def setPos(self, id, *args):
        """Set entity position (entityId:int, x,y,z)"""
        self.conn.send(self.pkg + ".setPos", id, args)

    def getTilePos(self, id):
        """Get entity tile position (entityId:int) => Vec3"""
        s = self.conn.sendReceive(self.pkg + ".getTile", id)
        return Vec3(*map(int, s.split(",")))

    def getTilePosV2(self, id):
        """Get entity tile position (entityId:int) => Vec3"""
        s = self.conn.sendReceive("v2." + self.pkg + ".getTile", id)
        return Vec3(*map(int, s.split(",")))

    def setTilePos(self, id, *args):
        """Set entity tile position (entityId:int) => Vec3"""
        self.conn.send(self.pkg + ".setTile", id, intFloor(*args))

    def getDirection(self, id):
        """Get entity direction (entityId:int) => Vec3"""
        s = self.conn.sendReceive(self.pkg + ".getDirection", id)
        return Vec3(*map(float, s.split(",")))

    def getRotation(self, id):
        """get entity rotation (entityId:int) => float"""
        return float(self.conn.sendReceive(self.pkg + ".getRotation", id))

    def getPitch(self, id):
        """get entity pitch (entityId:int) => float"""
        return float(self.conn.sendReceive(self.pkg + ".getPitch", id))

    def setting(self, setting, status):
        """Set a player setting (setting, status). keys: autojump"""
        self.conn.send(self.pkg + ".setting", setting, 1 if bool(status) else 0)


class CmdEntity(CmdPositioner):
    """Methods for entities"""
    def __init__(self, connection):
        CmdPositioner.__init__(self, connection, "entity")

    def spawnV2(self,x,y,z,entity_type_name,**kwargs):
        """Spawn entity (x,y,z,entity_type_name)"""
        property_str = None
        if len(kwargs) > 0:
            property_str = dict_to_api_string(kwargs)
        result = None
        if property_str == None:
            result = self.conn.sendReceive("v2.entity.spawn", x, y, z, entity_type_name)
        else:
            result = self.conn.sendReceive("v2.entity.spawn", x, y, z, entity_type_name, property_str)
        parts = result.split(":")
        return Entity(parts[0], parts[1])

    def startTaskV2(self,entity_uuid,task_name):
        """Start a task for a living entity (such as 'sit') (entity_uuid, task_name)"""
        self.conn.send("v2.entity.living.startTask", entity_uuid, task_name)

    def resetTaskV2(self,entity_uuid,task_name):
        """Reset ('un-start') a task for a living entity (such as 'sit') (entity_uuid, task_name)"""
        self.conn.send("v2.entity.living.resetTask", entity_uuid, task_name)

    def getAllInBoundingCube(self,
        x1, y1, z1,
        x2, y2, z2):
        """Fetch all entities that are within the bounding cube (entity_uuid, task_name)..."""
        result = self.conn.sendReceive("v2.entity.getAllInBoundingCube",
            x1, y1, z1,
            x2, y2, z2)
        entities_parsed = map(lambda str: str.split(":"), result.split(","))
        return map(lambda parsed: Entity(parsed[0], parsed[1]), entities_parsed)

class CmdPlayer(CmdPositioner):
    """Methods for the host (Raspberry Pi) player"""
    def __init__(self, connection, name=None):
        CmdPositioner.__init__(self, connection, "player")
        self.conn = connection
        self.name = name

    def getPos(self):
        return CmdPositioner.getPos(self, self.name)
    def setPos(self, *args):
        return CmdPositioner.setPos(self, self.name, args)
    def getTilePos(self):
        return CmdPositioner.getTilePos(self, self.name)
    def getTilePos(self):
        return CmdPositioner.getTilePosV2(self, self.name)
    def setTilePos(self, *args):
        return CmdPositioner.setTilePos(self, self.name, args)
    def getDirection(self):
        return CmdPositioner.getDirection(self, self.name)
    def getRotation(self):
        return CmdPositioner.getRotation(self, self.name)
    def getPitch(self):
        return CmdPositioner.getPitch(self, self.name)

class CmdCamera:
    def __init__(self, connection):
        self.conn = connection

    def setNormal(self, *args):
        """Set camera mode to normal Minecraft view ([entityId])"""
        self.conn.send("camera.mode.setNormal", args)

    def setFixed(self):
        """Set camera mode to fixed view"""
        self.conn.send("camera.mode.setFixed")

    def setFollow(self, *args):
        """Set camera mode to follow an entity ([entityId])"""
        self.conn.send("camera.mode.setFollow", args)

    def setPos(self, *args):
        """Set camera entity position (x,y,z)"""
        self.conn.send("camera.setPos", args)


class CmdEvents:
    """Events"""
    def __init__(self, connection):
        self.conn = connection

    def clearAll(self):
        """Clear all old events"""
        self.conn.send("events.clear")

    def pollBlockHits(self):
        """Only triggered by sword => [BlockEvent]"""
        s = self.conn.sendReceive("events.block.hits")
        events = [e for e in s.split("|") if e]
        return [BlockEvent.Hit(*map(int, e.split(","))) for e in events]

    def pollChatPosts(self):
        """Triggered by posts to chat => [ChatEvent]"""
        s = self.conn.sendReceive("events.chat.posts")
        events = [e for e in s.split("|") if e]
        return [ChatEvent.Post(int(e[:e.find(",")]), e[e.find(",") + 1:]) for e in events]

class Minecraft:
    """The main class to interact with a running instance of Minecraft Pi."""
    def __init__(self, connection, name=None):
        self.conn = connection

        self.camera = CmdCamera(connection)
        self.entity = CmdEntity(connection)
        self.player = CmdPlayer(connection, name)
        self.events = CmdEvents(connection)

    def getBlock(self, *args):
        """Get block (x,y,z) => id:int"""
        return int(self.conn.sendReceive("world.getBlock", intFloor(args)))

    def getBlockWithData(self, *args):
        """Get block with data (x,y,z) => Block"""
        ans = self.conn.sendReceive("world.getBlockWithData", intFloor(args))
        return Block(*map(int, ans.split(",")))
    """
        @TODO
    """
    def getBlocks(self, *args):
        """Get a cuboid of blocks (x0,y0,z0,x1,y1,z1) => [id:int]"""
        s = self.conn.sendReceive("world.getBlocks", intFloor(args))
        return map(int, s.split(","))

    def setBlock(self, *args):
        """Set block (x,y,z,id,[data])"""
        self.conn.send("world.setBlock", intFloor(args))

    def setBlockV2(self,x,y,z,type_name,**kwargs):
        """Set block (x,y,z,type_name,property_value...)"""
        property_str = None
        if len(kwargs) > 0:
            property_str = dict_to_api_string(kwargs)
        if property_str == None:
            self.conn.send("v2.world.setBlock", x, y, z, type_name)
        else:
            self.conn.send("v2.world.setBlock", x, y, z, type_name, property_str)

    def setBlocks(self, *args):
        """Set a cuboid of blocks (x0,y0,z0,x1,y1,z1,id,[data])"""
        self.conn.send("world.setBlocks", intFloor(args))

    def getHeight(self, *args):
        """Get the height of the world (x,z) => int"""
        return int(self.conn.sendReceive("world.getHeight", intFloor(args)))

    def getPlayerEntityIds(self):
        """Get the entity ids of the connected players => [id:int]"""
        ids = self.conn.sendReceive("world.getPlayerIds")
        return map(int, ids.split("|"))

    def getPlayerEntityId(self, name):
        """Get the entity id of the named player => [id:int]"""
        return int(self.conn.sendReceive("world.getPlayerId", name))

    def saveCheckpoint(self):
        """Save a checkpoint that can be used for restoring the world"""
        self.conn.send("world.checkpoint.save")

    def restoreCheckpoint(self):
        """Restore the world state to the checkpoint"""
        self.conn.send("world.checkpoint.restore")

    def postToChat(self, msg):
        """Post a message to the game chat"""
        self.conn.send("chat.post", msg)

    def setting(self, setting, status):
        """Set a world setting (setting, status). keys: world_immutable, nametags_visible"""
        self.conn.send("world.setting", setting, 1 if bool(status) else 0)

    def startBatch(self):
        self.conn.startBatch()

    def endBatch(self):
        self.conn.endBatch()

    @staticmethod
    def create(address = "localhost", port = 4711, name = None):
        return Minecraft(Connection(address, port), name)


if __name__ == "__main__":
    mc = Minecraft.create()
    mc.postToChat("Hello, Minecraft!")
