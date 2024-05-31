from fastapi import FastAPI
from routes.todos_routes import todo_api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from all origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
app.include_router(todo_api_router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)