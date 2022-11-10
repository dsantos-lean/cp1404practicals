"""
CP1404 Do-from-scratch exercise
Project Management Program
Estimated Time:
Actual Time:
"""
from datetime import datetime
from project import Project

def main():
    """Read file of programming language details, save as objects, display."""
    projects = []
    display_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            """Load projects from file"""
            load_projects(projects)
        elif choice == "S":
            print("Load projects")
            save_projects(projects)
        elif choice == "D":
            """Display incomplete and complete projects"""
            projects.sort()
            display_incomplete_projects(projects)
            display_completed_projects(projects)
        elif choice == "F":
            """Filter and display only projects that start after user inputted date"""
            filter_projects(projects)
        elif choice == "A":
            """Add new project into projects list"""
            print("Let's add a new project")
            add_new_project(projects)
        elif choice == "U":
            """Choose and modify an existing project"""
            for i, project in enumerate(projects):
                print(i, project)
            update_project(projects)
        display_menu()
        choice = input(">>> ").upper()


def filter_projects(projects):
    """Filter projects by date"""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    formatted_date = datetime.strptime(date_string, '%d/%m/%Y').date()
    filtered_projects = [project for project in projects if
                         datetime.strptime(project.start_date, "%d/%m/%Y").date() >= formatted_date]
    filtered_projects.sort()
    for item in filtered_projects:
        print(item)


def add_new_project(projects):
    """Add new project from user input"""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = int(input("Percent complete: "))
    projects_to_add = Project(name, start_date, priority, cost_estimate, percent_complete)
    projects.append(projects_to_add)


def update_project(projects):
    """Update existing project details"""
    project_index = int(input("Project choice: "))
    print(projects[project_index])
    try:
        new_percentage = int(input("New Percentage: "))
        projects[project_index].completion_percentage = new_percentage
    except ValueError:
        pass
    try:
        new_priority = int(input("New Priority: "))
        projects[project_index].priority = new_priority
    except ValueError:
        pass


def display_incomplete_projects(projects):
    """Display incomplete projects"""
    print("Incomplete projects:")
    incomplete_projects = [project for project in projects if not project.is_completed()]
    for items in incomplete_projects:
        print(f" {items}")


def display_completed_projects(projects):
    """Display completed projects"""
    print("Completed projects: ")
    completed_projects = [project for project in projects if project.is_completed()]
    for items in completed_projects:
        print(f" {items}")


def display_menu():
    """Display menu"""
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("= (F)ilter projects by date")
    print("= (A)dd new project")
    print("= (U)pdate project")
    print("= (Q)uit")


def load_projects(projects):
    """Process input file into a list of projects"""
    # filename = input("Input file: ")  # projects.txt
    in_file = open("projects.txt", 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('\t')
        project = Project(parts[0], parts[1], parts[2], float(parts[3]), int(parts[4]))
        projects.append(project)
    in_file.close()


def save_projects(projects):
    """Write new projects list to projects.txt file"""
    filename = input("Output file: ")
    out_file = open(filename, "w")
    for project in projects:
        print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}", file=out_file)
    out_file.close()



main()
