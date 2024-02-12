import menu.scripts
import feedback.scripts as logs

logs.enable_logging()
menu.scripts.show()
logs.send_log_file()

