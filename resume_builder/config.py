from starlette.config import Config

config = Config(".env")

DEBUG = config("DEBUG", default=False)
TEMPLATES_PATH = config("TEMPLATES_PATH")
RESUMES_PATH = config("RESUMES_PATH")
