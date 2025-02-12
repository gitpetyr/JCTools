import socket,datetime,time,os,logging

print("CWD:"+os.getcwd())
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)
# logFormatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logFormatter = logging.Formatter('')
logFile = logging.FileHandler(f"KeyLog{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.log")
logFile.setLevel(logging.DEBUG)
logFile.setFormatter(logFormatter)
logger.addHandler(logFile)
logger.info("Init logger")

# print(socket.gethostbyname(""))


sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

ip=socket.gethostbyname(socket.gethostname())
port=50601

sock.bind(("",port))

while True:
    try:
        data,addr=sock.recvfrom(1048576)
        nowtime=datetime.datetime.now().strftime("%Y/%m/%d-%H:%M:%S:%f")
        msg=f"[{nowtime}:FROM{str(addr)} ] == {data.decode("utf-8")}"
        print(msg)
        logger.info(msg)
    except Exception as e:
        msg=str(e)
        print(e)
    finally:
        continue