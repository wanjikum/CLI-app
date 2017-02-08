
#!/usr/bin/venv python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive todo list command application.
Usage:
    app.py create_task <title>...
    app.py get_all_tasks
    app.py get_task_details <task_id>
    app.py edit_task_details <task_id> <title>...
    app.py mark_finished <task_id>
    app.py (-i | --interactive)
    app.py (-h | --help | --version)

"""
import os
import sys
import cmd
from docopt import docopt, DocoptExit
from functions import ToDoFunctions
function = ToDoFunctions()

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

def start():
    os.system("clear")
    intro = 'Welcome to my interactive program!'
    prompt = 'todo>>>'
    print(__doc__)



class ToDo(cmd.Cmd):
    intro = 'Welcome to my interactive program!'
    prompt = 'todo>>>'

    @docopt_cmd
    def do_create_task(self, arg):
        """Usage: create_task <title>..."""
        title = " ".join(arg["<title>"])
        data = {'title' : title}
        function.create_task(data)
        

    @docopt_cmd
    def do_get_all_tasks(self, arg):
        """Usage: get_all_tasks """
        function.get_all_tasks()

    @docopt_cmd
    def do_get_task_details(self, arg):
        """Usage: get_task_details <task_id>"""
        task_id = arg["<task_id>"]
        function.get_task_details(task_id)

    @docopt_cmd
    def do_edit_task_details(self, arg):
        """Usage: edit_task_details <task_id> <title>..."""
        task_id = arg["<task_id>"]
        title = " ".join(arg["<title>"])
        data = {'title': title}
        function.edit_task_details(task_id, data)

    @docopt_cmd
    def do_mark_finished(self, arg):
        """Usage: mark_finished <task_id>"""
        task_id = arg["<task_id>"]
        function.mark_finished(task_id)

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!', "cyan")
        exit()

opt = docopt(__doc__, sys.argv[1:])

if __name__ == "__main__":
    try:
        start()
        ToDo().cmdloop()
    except KeyboardInterrupt:
        os.system("clear")
        print('Application Exiting')