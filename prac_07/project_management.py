"""
CP1404 Do-from-scratch exercise
Project Management Program
Estimated Time:
Actual Time:
"""
from project import Project


def main():
    """Read file of programming language details, save as objects, display."""
    projects = []
    display_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":  # TODO error-checking
            load_projects(projects)
        elif choice == "S":  # TODO save to list, (Prompt the user for a filename to save projects to and save them)
            print("Load projects")
            save_projects(projects)
        elif choice == "D":  # DONE
            projects.sort()
            display_incomplete_projects(projects)
            display_completed_projects(projects)
        elif choice == "F":  # filter projects by date, (Ask the user for a date and display only projects that start after that date, sorted by date)
            pass
        elif choice == "A":  # add new project, (Ask the user for the inputs and add a new project to memory)
            pass
        elif choice == "U":  # update project, (Choose a project, then modify the completion % and/or priority - leave blank to retain existing values)
            pass
        display_menu()
        choice = input(">>> ").upper()
    # max_length = max([len(project.name) for project in projects])
    # for project in projects:
    #     # Removed __str__ method from Project class for this to work
    #     print(f"{project.name}, {project.start_date}, {project.priority}, {project.cost_estimate}, {project.completion_percentage}")


def display_incomplete_projects(projects):
    print("Incomplete projects:")
    incomplete_projects = [project for project in projects if not project.is_completed()]
    for items in incomplete_projects:
        print(f" {items}")


def display_completed_projects(projects):
    print("Completed projects: ")
    completed_projects = [project for project in projects if project.is_completed()]
    for items in completed_projects:
        print(f" {items}")


def display_menu():
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
    # Check how to add header
    for project in projects:
        # Edit formatting
        print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}", file=out_file)
    out_file.close()


# x = Project("X project", 12/12/2022, 10, 600.0, 99)
#
# def run_tests():
#     """Test different age and vintage status outputs"""
#     print(f"{x.name} {x.is_completed()}")



main()
# run_tests()