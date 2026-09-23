# AI DISCLOSURE

I recognize that I am submitting this late, only realising my error after the comments from assignment 1 came through, I hope this does not affect evaluation

## Q1
Here I used AI to create app.py and understand the parts of the API call, usage of BaseModel to validate entries. Also had a brief look at the documentation at fastapi.tiangolo.com. Also used it to generate the Dockerfiles for the naive and multi-stage builds, which I later went through and understood.

## Q2
Redis was implemented with the help of LLMs. Also used it to understand the role of docker-compose in relaying commands between the api and redis-server(noticed that I used a different name as suggested in the assignment now for the redis:7-alpine image). Had some issues showing the timing, before I used it to debug that the url was wrong and it was interpreting 2 requests every time. After that, cleared cache and was able to get the results required.

## Q3
Used it to generate 8 shard csvs. Followed by understanding the .yaml file and the different arguments that the Job uses. Finally cleared doubts regarding the mechanism of the downward API.

## Q4
Used to generate the deployment.yaml file. Couldn't debug why kubectl rollout history showed no changes in my terminal, although the change to including the version was done in the FastAPI url of healthz.
