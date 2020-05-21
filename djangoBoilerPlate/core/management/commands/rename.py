from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):  # class Command inherits from the BaseCommand.
    help = 'Rename a Django project'

    def add_arguments(self,parser):     # parser is used to add the argument into our command.
        parser.add_argument('new_project_name',type=str, help='The new Django project name')  # name of the project must be a string.
        
        #optional argument.
        #parser.add_argument('-p','--prefix')    # -p makes it optional.
    
    def handle(self,*args,**kwargs):    # *args and **kwargs(keyword) are used for variable arguments in function.
        new_project_name = kwargs['new_project_name']

        # logic for renaming the project.
        # here how to search a file and rename a specific part of it. It is done with the help of regular expressions.

        # in files_to_rename add the path of the file.
        files_to_rename = [
            'djangoBoilerPlate/settings/base.py',
            'djangoBoilerPlate/wsgi.py',
            'manage.py'
        ]

        # it is important to rename the files first then folder.
        folder_to_rename = 'djangoBoilerPlate'

        for f in files_to_rename:

            # reading the filedata
            with open(f,'r') as file:
                filedata = file.read()
            
            # replacing the filedata
            filedata = filedata.replace('demo',new_project_name)

            # writing the filedata to the file.
            with open(f,'w') as file:
                file.write(filedata)

        # for folder renaming.
        os.rename(folder_to_rename,new_project_name)

        # printing out the successful message to the console.
        self.stdout.write(self.style.SUCCESS('Project has been rename to  %s'% new_project_name))