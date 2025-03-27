import redis
import metaclass

class Database():
    def __init__():
        try:
            self.db = redis.Redis(decode_response=True)
        except Exception e:
            print(f"Error: {e.message}")

    def get_instance() -> Redis:
        return self.db


