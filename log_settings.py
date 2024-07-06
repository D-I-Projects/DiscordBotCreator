import os
import logging
import datetime

class logsettings:
    @staticmethod
    def log_settings():
        log_dir = os.path.join("Logs")
        try:
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
        except OSError as e:
            print(f"Error creating log directory: {e}")
            raise
        
        current_datetime = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        log_filename = os.path.join(log_dir, f"DiscordBotCreator_{current_datetime}.log")

        logger = logging.getLogger("DiscordBotCreator")
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        file_handler = logging.FileHandler(log_filename)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        return logger
