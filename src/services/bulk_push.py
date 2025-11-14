from utils.logger import get_logger

logger = get_logger("bulk-push")

class BulkPush:
    def __init__(self, push_function):
        self.push_function = push_function

    def run(self, services: list):
        results = []
        logger.info("Starting bulk service push operation")

        for svc in services:
            try:
                logger.info(f"Pushing service {svc['service_id']}")
                result = self.push_function(svc)
                results.append({"service_id": svc["service_id"], "status": "success", "output": result})
            except Exception as e:
                logger.error(f"Failed to push service {svc['service_id']}: {e}")
                results.append({"service_id": svc["service_id"], "status": "failed", "error": str(e)})

        return results
