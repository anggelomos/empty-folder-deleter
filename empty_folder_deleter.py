import os
import sys

try:
    path = sys.argv[1]
except IndexError:
    path = "."

def folder_deleter(folder_name: str, verbose_mode: bool = True) -> bool:
    """Delete a folder if it is empty, if the folder is deleted successfully it returns 0 otherwise returns 1

    Parameters
    ----------
    folder_name : str
        The name of the folder to be deleted
    verbose_mode : bool, optional
        Variable to activate the prints in the function, by default True

    Returns
    -------
    successfull_delete : bool
        If the folder is deleted successfully it returns 0 otherwise returns 1
    """
    
    successfull_delete = 1
    if os.listdir(folder_name) == []:
        os.rmdir(folder_name)
        successfull_delete = 0
    else:
        if verbose_mode:
            print("The folder wasn't deleted because it was not empty")

    return successfull_delete

