from starlette.applications import Starlette
from starlette.exceptions import HTTPException
from starlette.templating import Jinja2Templates

from resume_builder.config import DEBUG, TEMPLATES_PATH
from resume_builder.exceptions import ResumeDoesNotExist, ResumeInvalidYaml
from resume_builder.utils import load_resume, template_exists

app = Starlette(debug=DEBUG)
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
    context["request"] = request
    return templates.TemplateResponse(f"{template}/index.html", context)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", reload=DEBUG)
