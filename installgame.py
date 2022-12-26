from git import Repo
import os
directory = os.getcwd()
Repo.clone_from("https://github.com/formercornet/turtleracing.git", "{0}/turtlegame".format(directory))