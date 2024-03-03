import subprocess
import threading


def ping(hostname):
    p = subprocess.Popen(["ping", hostname], stdout=subprocess.PIPE)
    sortie = p.communicate()[0].decode("CP850")
    print("😀" if(sortie.find(": octets=") != -1) else "😡", hostname)


def testIpsV1():  # sequentiel
    [ping("192.168.0." + str(i)) for i in range(0, 256)]


def testIpsV2():  # multithread
    allThreads = []
    for i in range(0, 256):
      th = threading.Thread(target=ping, args=("10.9.151." + str(i),))
      th.start()
      allThreads.append(th)
    [t.join() for t in allThreads]
    print("J'ai tout fini !")

def testIpsV3():
  class Pinger(threading.Thread):
    def __init__(self, hostname):
      threading.Thread.__init__(self)
      self.hostname = hostname

    def run(self):
      ping(self.hostname)

  allThreads = []
  for i in range(0, 256):
    th = Pinger("10.9.151." + str(i))
    th.start()
    allThreads.append(th)
  [t.join() for t in allThreads]
  print("J'ai tout fini !")

# testIpsV1()
#testIpsV2()
testIpsV3()
