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
		print("-*-" * 5 + "getting tasks" + "-*-" * 5)
		resp = requests.get('http://jsonplaceholder.typicode.com/todos/')
		if resp.status_code != 200:
			print("Something is not right")
		tasks_data = json.loads(resp.text)
		for index, title in enumerate(tasks_data):
			print(str(index + 1) + " - " + title['title'])




	def get_task_details(self, task_id):
		print("-*-" * 5 + "get task detail" + "-*-" * 5)
		resp = requests.get('http://jsonplaceholder.typicode.com/todos/' + str(task_id))
		if resp.status_code != 200:
			print("Something is not right")
		task_data = json.loads(resp.text)
		if not task_data:
			print("Try again using a different id")
		print("Task id: "+str(task_data['id']))
		print("Title: " + task_data['title'])

	def edit_task_details(self, task_id, data):
		print("-*-" * 5 + "editting task detail" + "-*-" * 5)
		resp = requests.put('http://jsonplaceholder.typicode.com/todos/' + str(task_id), data=data)
		if resp.status_code == 200:
			task_details = json.loads(resp.text)
			print("Task {0} edited successfully".format(task_details['title']))
		else:
			print("Error occured editing task")
	
	def mark_finished(self):
		print("-" * 5 + "finished" + "-" * 5)