import logging
from zebrok.worker import WorkerInitializer

logger = logging.getLogger(__name__)

logger.info("Initializing Workers")
worker = WorkerInitializer(auto_discover=True)
worker.start()