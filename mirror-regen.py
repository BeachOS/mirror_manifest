#!/usr/bin/env python3

import os
import sys
try:
    from gitlab import Gitlab
except ImportError:
    print("Please install the python-gitlab package via pip3")
    exit(1)
e = os.environ.copy()
# Environment variables for gitlab username and api token
try:
    p = e["GITLAB_TOKEN"]
except KeyError:
    print("Please set the GITLAB_TOKEN environment variable")
    exit(1)

GITLAB_GROUP_ID = 3642190

gl = Gitlab(f'https://gitlab.com', p)
gl_group = gl.groups.get(GITLAB_GROUP_ID)
projects = gl_group.projects.list(all=True, archived=False, visibility="public", include_subgroups=True)

file = open("default.xml", "w")
file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
file.write("<manifest>\n")
file.write("\n")
file.write("  <remote  name=\"gitlab\"\n")
file.write("           fetch=\"..\" />\n")
file.write("\n")
file.write("  <default revision=\"master\"\n")
file.write("           remote=\"gitlab\"\n")
file.write("           sync-j=\"4\" />\n")
file.write("\n")

repos = []

for repo in projects:
    repos.append(repo.path_with_namespace)

for repo in sorted(repos):
    file.write("  <project name=\"" + repo + "\" />\n")

file.write("</manifest>\n")
file.close()
