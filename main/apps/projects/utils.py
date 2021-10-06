from typing import List


def get_users_for_project(project) -> List:
    user_list = [project.owner]

    if project.supplier:
        for sup_user in project.supplier.owners.all():
            user_list.append(sup_user)

    if project.consultant:
        for sup_user in project.consultant.owners.all():
            user_list.append(sup_user)

    return user_list
