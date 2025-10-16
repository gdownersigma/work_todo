import argparse
from datetime import date
# creating the main parser
master_parser = argparse.ArgumentParser()

# creating subparsers
subparsers = master_parser.add_subparsers(
    dest="command", required=True, help="Create help")  # add helpful help

# create the make_task subcommand
make_task_parser = subparsers.add_parser(
    "make", help="Makes a task with provided information")
make_task_parser.add_argument(
    "-n", "--name", required=True, help="Name of the task")
make_task_parser.add_argument("-p", "--priority", required=True, type=int, choices=[
                              1, 2, 3], help="priority of the task [1,2,3], 1 is low priority, 3 is high")
make_task_parser.add_argument(
    "-d", "--deadline", required=False, default=None, help='Deadline: time until due in - days')

args = master_parser.parse_args()

if args.command == "make":
    print(
        f"trying to create task named {args.name} with priority {args.priority} and deadline {args.deadline} days")
