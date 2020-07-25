import os


def folder_deleter(folder_name: str, verbose_mode: bool = True) -> int:

    successfull_delete = 1
    if os.listdir(folder_name) == []:
        os.rmdir(folder_name)
        successfull_delete = 0
    else:
        if verbose_mode:
            print("The folder wasn't deleted because it was not empty")

    return successfull_delete


# folder_deleter("prueba")