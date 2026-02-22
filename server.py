from fastapi import FastAPI,Query
from .client.rq_client import queue
from .queues.worker import proceesquery
from dotenv import load_dotenv
load_dotenv()


app=FastAPI()

@app.get('/')
def root():
 return{"status":'Server is up and running'}

@app.post('/chat')
def chat(
        query:str=Query(...,description="THe chat query of user")
):
    job=queue.enqueue(proceesquery,query)

    return {"status":"queued","job_id":job.id}
@app.get('/job-status')
def get_result(
        job_id:str=Query(...,description="JobID")
):
    job=queue.fetch_job(job_id=job_id)
    result=job.return_value()

    return {"result":result}
