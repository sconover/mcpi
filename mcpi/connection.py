import socket
import select
import sys
from util import flatten_parameters_to_string

""" @author: Aron Nieminen, Mojang AB"""

class RequestError(Exception):
    pass

class Connection:
    """Connection to a Minecraft Pi game"""
    RequestFailed = "Fail"

    def __init__(self, address, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((address, port))
        self.lastSent = ""
        self.batch = False
        self.batchCommands = None

    def drain(self):
        """Drains the socket of incoming data"""
        while True:
            readable, _, _ = select.select([self.socket], [], [], 0.0)
            if not readable:
                break
            data = self.socket.recv(1500)
            e =  "Drained Data: <%s>\n"%data.strip()
            e += "Last Message: <%s>\n"%self.lastSent.strip()
            sys.stderr.write(e)

    def startBatch(self):
        self.batch = True
        self.batchCommands = []

    def endBatch(self):
        self.batch = False
        if len(self.batchCommands)>0:
            self._doSend("\n".join(self.batchCommands))

    def send(self, f, *data):
        """Sends data. Note that a trailing newline '\n' is added here"""
        s = "%s(%s)\n"%(f, flatten_parameters_to_string(data))
        if self.batch == True:
            self.batchCommands.append(s)
        else:
            self._doSend(s)

    def _doSend(self, s):
        self.drain()
        self.lastSent = s
        self.socket.sendall(s)

    def receive(self):
        """Receives data. Note that the trailing newline '\n' is trimmed"""
        s = self.socket.makefile("r").readline().rstrip("\n")
        if s == Connection.RequestFailed:
            raise RequestError("%s failed"%self.lastSent.strip())
        return s

    def sendReceive(self, *data):
        """Sends and receive data"""
        if self.batch == True:
            raise Exception("batches of sendReceive not yet supported")
        self.send(*data)
        return self.receive()
