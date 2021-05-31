import json

# terminal output colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def judge(problem_list, requested_desc: str):
    for i in problem_list:
        for j in problem_list[i]:
            if j['topic'].find(requested_desc) != -1:
                for k in j['options']:
                    if k[:1] == j['answer']:
                        print(f"{bcolors.OKGREEN}{k[3:]}{bcolors.ENDC}")
                return
    print(f"{bcolors.FAIL}Not Found{bcolors.ENDC}")


def review_problem(problem):
    print(problem['topic'])
    for i in problem['options']:
        print(i)
    answer = input("Please fill in your answer: ")
    if answer.lower() == problem['answer'].lower():
        print(f"{bcolors.OKGREEN}Correct!{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}Not correct. Correct answer: {problem['answer']}{bcolors.ENDC}")
    print('')


with open('problem_list.json') as f:
    problem_list = json.load(f)
    command = input("Welcome to this project. Please choose [R]eview, [C]heck_problem: ")
    if command == 'R' or command == 'r':
        chapter = input("Please choose the chapter: ")
        for i in problem_list[chapter]:
            review_problem(i)
    elif command == 'C' or command == 'c':
        while True:
        	requested_desc = input("Paste your problem description here: ")
        	judge(problem_list, requested_desc)
