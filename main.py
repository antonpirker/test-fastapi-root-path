from fastapi import FastAPI

import sentry_sdk
sentry_sdk.init(
    dsn="https://c65a02f670a844deac27c2b8373d8a45@o447951.ingest.sentry.io/4505160410333184",
    debug=True,
    release="0.0.0",
    traces_sample_rate=1.0, 
)

app = FastAPI(root_path="/api/v1")


@app.get("/{server_something}")
async def server_api(server_something):
    sentry_sdk.capture_message("Server received request %s" % server_something)

    1/0

    return {
        "given_by_you": server_something,
        "returned_by_server": server_something.upper(),
    }


@app.post("/post/{server_something}")
async def server_api_post(server_something):
    sentry_sdk.capture_message("Server received request %s" % server_something)

    1/0

    return {
        "given_by_you": server_something,
        "returned_by_server": server_something.upper(),
    }
