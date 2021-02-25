from zebrok.worker import WorkerInitializer

worker = WorkerInitializer(auto_discover=True)
worker.start()