import os

from starlette.applications import Starlette
from starlette.exceptions import HTTPException
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from resume_builder.config import DEBUG, RESUMES_PATH, TEMPLATES_PATH
from resume_builder.exceptions import ResumeDoesNotExist, ResumeInvalidYaml
from resume_builder.utils import load_resume, template_exists

routes = [
    Mount("/static/resumes", app=StaticFiles(directory=RESUMES_PATH), name="resumes"),
    Mount(
        "/static/templates", app=StaticFiles(directory=TEMPLATES_PATH), name="templates"
    ),
]

app = Starlette(routes=routes, debug=DEBUG)
templates = Jinja2Templates(directory=TEMPLATES_PATH)


@app.route("/{resume}", methods=("GET",))
def view_resume(request):
    resume = request.path_params["resume"]
    try:
        context = load_resume(resume)
    except ResumeDoesNotExist:
        raise HTTPException(404, "Not found")
    except ResumeInvalidYaml:
        raise HTTPException(500, "YAML file error")
    try:
        template = context.pop("template")
    except KeyError:
        raise HTTPException(500, "Missing template")
    if not template_exists(template):
        raise HTTPException(400, "Template not found")
    picture = context.pop("picture", None)
    if picture:
        context["picture"] = os.path.join("/", resume, picture)
    context["request"] = request
    return templates.TemplateResponse(f"{template}/index.html", context)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", reload=DEBUG)
