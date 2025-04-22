# Medium: Build a class-based logging system that supports multiple backends: Console, File, and (later) Email—without touching the original logger.
class LoggingSystem:
  def system_log(self):
    raise NotImplementedError

class Console(LoggingSystem):
  def system_log(self, message):
    print(f"[Console] {message}")

class File(LoggingSystem):
  def system_log(self, message):
    print(f"[File] {message}")

class Email(LoggingSystem):
  def system_log(self, message):
    print(f"[Email] {message}")
  
log = Console()
log.system_log("Logging is console")