import os
import requests
import json
"""Todo Consoleapp functions"""
class ToDoFunctions():
	"""A class consumes api that uses http verbs"""
	def create_task(self, data):
		print("<"+ "--"* 5 + "creating task" + "--" * 5 + ">")
		resp = requests.post('http://jsonplaceholder.typicode.com/todos/', data=data) 
		if resp.status_code == 201:
			task_details = json.loads(resp.text)
			print("Task {0} created successfully".format(task_details['title']))


	def get_all_tasks(self):
		print("-" * 5 + "getting tasks" + "-" * 5)

	def get_task_details(self):
		print("-" * 5 + "get task detail" + "-" * 5)

	def edit_task_details(self):
		print("-" * 5 + "editting task detail" + "-" * 5)
	
	def mark_finished(self):
		print("-" * 5 + "finished" + "-" * 5)