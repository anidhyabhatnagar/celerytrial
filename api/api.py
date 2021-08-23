from flask import Flask, request, jsonify
from tasks import get_stats
from tasks import text_reverse
from reverse_task import text_reverse
from db.db_connection import DBConnection
from db.db_api_operation import DBAPIOperations


api = Flask(__name__)
db_con = DBConnection("../.ini")


@api.before_request
def before_request():
    if request.method == 'OPTIONS':
        return jsonify({}), 200


@api.errorhandler(500)
def internal_error(error):
    return jsonify({"msg": "Internal Server Error", "status": 500}), 500


@api.errorhandler(400)
def bad_request(error):
    return jsonify({"msg": "Bad Request", "status": 400}), 400


@api.errorhandler(404)
def not_found(error):
    return jsonify({"msg": "Not Found", "status": 404}), 404


@api.route('/submit_data/', methods=['POST'])
def submit_data():
    content = request.json
    text = content.get("text")
    job_id = get_stats.delay(text)
    jid = job_id.id
    return jsonify({"job_id": jid, "status": "Job Submitted"})


@api.route('/get_results/', methods=['POST'])
def get_results():
    content = request.json
    job_id = content.get("job_id")
    db_op = DBAPIOperations(connection=db_con)
    result = db_op.get_celery_task_result(job_id=job_id)
    print(result)
    return jsonify(result)


@api.route('/reverse/', methods=['POST'])
def reverse():
    content = request.json
    text = content.get("text")
    job_id = text_reverse.delay(text)
    jid = job_id.id
    return jsonify({"job_id": jid, "status": "Job Submitted"})


if __name__ == '__main__':
    api.run(host="0.0.0.0", debug=True)
