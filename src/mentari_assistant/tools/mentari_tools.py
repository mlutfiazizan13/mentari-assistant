import os
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import requests



class MyCustomTool(BaseTool):
    # name: str = "Name of my tool"
    # description: str = (
    #     "Clear description for what this tool is useful for, your agent will need this information to use it."
    # )
    # args_schema: Type[BaseModel] = MyCustomToolInput

    # def _run(self, argument: str) -> str:
    #     # Implementation goes here
    #     return "this is an example of a tool output, ignore it and move along."

    
    def __init__(self):
    
        self.token = self.login(os.environ.MENTARI_USERNAME, os.environ.MENTARI_PASSWORD); 

    def login(self, username: str, password: str) -> str:
        url = os.environ.MENTARI_API_URL + "/login"
        response = requests.post(url, json={"username": username, "password": password})
        response.raise_for_status()
        return response.json()["access_token"]
    
    
    def user_course(self) -> dict:
        url = os.environ.MENTARI_API_URL + "/user-course"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.token}"})
        response.raise_for_status()
        return response.json()
    
    
    def course_detail(self, course_id: str) -> dict:
        url = os.environ.MENTARI_API_URL + f"/user-course/{course_id}"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.token}"})
        response.raise_for_status()
        return response.json()
    
    
    def quiz_start(self, course_id: str) -> dict:
        url = os.environ.MENTARI_API_URL + f"/quiz/start/{course_id}"
        request_body = {
            "id_trx_course_sub_section": course_id,
            "reset": 1
        }
        response = requests.get(url, json=request_body, headers={"Authorization": f"Bearer {self.token}"})
        response.raise_for_status()
        return response.json()
    
    def quiz_question(self, quiz_id: str) -> dict:
        url = os.environ.MENTARI_API_URL + f"/quiz/soal/{quiz_id}"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.token}"})
        response.raise_for_status()
        return response.json()
    
    
    