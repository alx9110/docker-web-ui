import time
from rq import Queue
from redis import Redis
from tasks import count_words_at_url
redis_conn = Redis()
queue = Queue(connection=redis_conn)

job = queue.enqueue(count_words_at_url, 'http://ya.ru')
print(job.result)
time.sleep(4)
job_id = job.id
print(job.result)
# job.delete()
time.sleep(1)
job = queue.fetch_job(job_id)
print(job.result)
