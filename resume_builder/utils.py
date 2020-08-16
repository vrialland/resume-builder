import base64
import logging
import os
import yaml

from resume_builder.config import RESUMES_PATH, TEMPLATES_PATH
from resume_builder.exceptions import ResumeDoesNotExist, ResumeInvalidYaml


logger = logging.getLogger(__file__)


def template_exists(name):
    filename = f"{TEMPLATES_PATH}/{name}/index.html"
    return os.path.isfile(filename)


def get_resumes():
    for elem in os.listdir(RESUMES_PATH):
        if not os.path.isdir(elem):
            continue
        if os.path.exists(f"{elem}/data.yml"):
            yield os.path.basename(elem)


def get_resume_path(name):
    return f"{RESUMES_PATH}/{name}/data.yml"


def get_resume_picture_path(name, picture):
    return f"{RESUMES_PATH}/{name}/{picture}"


def resume_exists(name):
    return os.path.isfile(get_resume_path(name))


def load_resume(name):
    if not resume_exists(name):
        raise ResumeDoesNotExist()
    try:
        with open(get_resume_path(name)) as f:
            return yaml.load(f, Loader=yaml.BaseLoader)
    except Exception as e:
        logger.exception(e)
        raise ResumeInvalidYaml()
