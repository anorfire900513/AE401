from mcpi_e.minecraft import Minecraft
mc=Minecraft.create("127.0.0.1",4711,"Aphrodite32728")
t=0
while 1:
    t=t+1
    mc.postToChat("第%i次" % t)