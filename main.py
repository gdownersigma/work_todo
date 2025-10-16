import argparse
from datetime import date


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
    make_task_parser.add_argument("-p", "--priority", required=True, type=int, choices=[
        1, 2, 3], help="priority of the task [1,2,3], 1 is low priority, 3 is high")
    make_task_parser.add_argument(
        "-d", "--deadline", required=False, default=None, help='Deadline: time until due in - days')

    # create the finish_task subcommand
    finish_task_parser = subparsers.add_parser(
        "finish", help="Finish a task of the provided name")
    finish_task_parser.add_argument(
        "-n", "--name", required=True, help="Name of the task to be finished")

    return master_parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    if args.command == "make":
        print(
            f"trying to create task named {args.name} with priority {args.priority} and a deadline of {args.deadline} days")
    elif args.command == "finish":
        print(
            f"trying to finish task named {args.name}")
