from django.shortcuts import render
import os
import subprocess


def UpdateView(request):
    git_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    git_pull = ['git', 'pull']

    subprocess.check_output(git_pull, cwd=git_dir, universal_newlines=True)
