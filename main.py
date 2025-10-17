import argparse
from datetime import datetime, timedelta
import json

task_file = "tasks.json"


def open_file(file_name):
    # PARAM file_name: name of file to open
    # function opens a json file and returns the information inside
    try:
        with open(file_name) as f:
            return json.load(f)
    except FileNotFoundError:  # error if file is not found
        print("File not found.")
        exit()


def save_file(file_name):
    # PARAM file_name: name of file to open/save to
    # function to save recipes to file
    with open(file_name, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(name, priority, deadline, weight, filename):
    today = datetime.today()
    deadline = today + timedelta(days=deadline)
    task_object = {"name": name,
                   "priority": priority,
                   "weight": weight,
                   "deadline": deadline.strftime("%d-%m-%Y"),
                   "date": today.strftime("%d-%m-%Y")}
    tasks.append(task_object)
    save_file(filename)


def get_args():
    # creating the main parser
    master_parser = argparse.ArgumentParser()

    # creating subparsers
    subparsers = master_parser.add_subparsers(
        dest="command", required=True, help="Create help")  # add helpful help

    # create the make_task subcommand
    make_task_parser = subparsers.add_parser(
        "make", help="Makes a task with provided information")
    make_task_parser.add_argument(
        "-n", "--name", required=True, help="Name of the task to be created")
    make_task_parser.add_argument("-p", "--priority", type=int, choices=[
        1, 2, 3], help="priority of the task [1,2,3], 1 is low priority, 3 is high", default=2)
    make_task_parser.add_argument("-w", "--weight", type=int, choices=[
                                  1, 2, 3], help="How difficult a task is to determine its weight: [1,2,3], 1 is low priority, 3 is high.", default=2)
    make_task_parser.add_argument(
        "-d", "--deadline", default=None, type=int, help='Deadline: time until due in - days')

    # create the finish_task subcommand
    finish_task_parser = subparsers.add_parser(
        "finish", help="Finish a task of the provided name")
    finish_task_parser.add_argument(
        "-n", "--name", required=True, help="Name of the task to be finished")

    # create the view subcommand
    view_task_parser = subparsers.add_parser(
        "view", help="Outputs a to do list in order of priority, difficulty & deadline"
    )
    view_task_parser.add_argument(
        "-l", "--length", type=int, help="The length of the to do list", default=10)

    return master_parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    tasks = open_file(task_file)

    if args.command == "make":
        # print(
        # f"trying to create task named {args.name} with priority {args.priority} and a deadline of {args.deadline} days")
        add_task(args.name, args.priority,
                 args.deadline, args.weight, task_file)
    elif args.command == "finish":
        print(
            f"trying to finish task named {args.name}")
    elif args.command == "view":
        # print(f"Attempting to show a to-do list of {args.length} items.")
        print(tasks)
