from vec3 import Vec3

class Entity:
    """Represents a unique entity in the minecraft world"""
    def __init__(self, type, uuid):
        self.type = type
        self.uuid = uuid
