from rpyc import Service
from rpyc.utils.server import ThreadedServer
from rpyc.core.service import SlaveService

# hostname有所变化，可以通过ipconfig在cmd进行查看
sr = ThreadedServer(SlaveService, hostname='192.168.11.36', port=9999, auto_register=False)
sr.start()
