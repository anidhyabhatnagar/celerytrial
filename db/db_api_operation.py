

class DBAPIOperations:
    def __init__(self, connection):
        self.db = connection.get_db()

    def get_celery_task_result(self, job_id):
        try:
            print(job_id)
            result = self.db.celery_taskmeta.find({"_id": str(job_id)}, {"status": 1, "result": 1})
            print(result[0])
            if result[0].get("status") == "SUCCESS":
                return result[0].get("result")
            else:
                return {"status": "IN PROGRESS", "message": "Please try after some time"}
        except Exception as e:
            print("Exception in get_celery_task_result: {}".format(e))
            return {"status": "NOT FOUND", "message": "Job ID does not exist."}
