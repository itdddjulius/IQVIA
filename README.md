# IQVIA - PYTHON Technical Test
---

DrugDev Technical Test

The goal of this exercise is to build a fully functional API application using best
practices and reusable code.

# Rules
Your application must use the Flask web framework and the SQLAlchemy
library for interacting with the database.

You may use the built-in development server and SQLite as the database
engine.

You are free to use any other libraries you like. All dependencies should be
installable via pip and listed in a requirements.txt file.

You should include unit tests.

# Task
# Step 1: 
Create a small contact management API with the following

# functionality:
- List all contacts
- Find a contact by username
- Create a new contact
- Update a contact
- Delete a contact

At a minimum, the Contact model consists of a username, first name and
last name. You may add any other columns necessary to implement the
required functionality.

# Step 2: 
As a second step, extend your application to support email
addresses.

Introduce a new Email model and allow a Contact to have multiple email
addresses. Adjust the endpoints above to return emails in their output and
accept emails as input as you see fit.

# Step 3: 
Use Celery to add asynchronous functionality to your application.
- Implement a task that creates a Contact with random data every 15
seconds.

- Implement a task that removes Contacts older than 1 minute.
For convenience, use Redis as your Celery broker and assume it will be
installed and running on the test machine.
================================================

================ IQVIA - Technical Test ===============
The goal of this exercise is to build a fully functional API application using best
practices and reusable code.
Rules
Your application must use the Flask web framework and the SQLAlchemy
library for interacting with the database.
You may use the built-in development server and SQLite as the database
engine.
You are free to use any other libraries you like. All dependencies should be
installable via pip and listed in a requirements.txt file.
You should include unit tests.
Task
Step 1: Create a small contact management API with the following
functionality:
- List all contacts
- Find a contact by username
- Create a new contact
- Update a contact
- Delete a contact
At a minimum, the Contact model consists of a username, first name and
last name. You may add any other columns necessary to implement the
required functionality.
Step 2: As a second step, extend your application to support email
addresses.
Introduce a new Email model and allow a Contact to have multiple email
addresses. Adjust the endpoints above to return emails in their output and
accept emails as input as you see fit.
Step 3: Use Celery to add asynchronous functionality to your application.
- Implement a task that creates a Contact with random data every 15
seconds.
- Implement a task that removes Contacts older than 1 minute.
For convenience, use Redis as your Celery broker and assume it will be
installed and running on the test machine.
================================================================================

ubuntu@DESKTOP-D7QB2EH:/mnt/c/Users/user/Desktop/JO/My Clients/IQVIA$ sudo apt-get install python3.6
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following package was automatically installed and is no longer required:
  libuv1
Use 'sudo apt autoremove' to remove it.
The following additional packages will be installed:
  libpython3.6-minimal libpython3.6-stdlib python3.6-minimal
Suggested packages:
  python3.6-venv python3.6-doc binfmt-support
The following NEW packages will be installed:
  libpython3.6-minimal libpython3.6-stdlib python3.6 python3.6-minimal
0 upgraded, 4 newly installed, 0 to remove and 11 not upgraded.
Need to get 4,481 kB of archives.
After this operation, 23.0 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial/main amd64 libpython3.6-minimal amd64 3.6.8-1~16.04.york1 [578 kB]
Get:2 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial/main amd64 python3.6-minimal amd64 3.6.8-1~16.04.york1 [1,689 kB]
Get:3 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial/main amd64 libpython3.6-stdlib amd64 3.6.8-1~16.04.york1 [1,968 kB]
Get:4 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial/main amd64 python3.6 amd64 3.6.8-1~16.04.york1 [246 kB]
Fetched 4,481 kB in 4s (906 kB/s)
Selecting previously unselected package libpython3.6-minimal:amd64.
(Reading database ... 156696 files and directories currently installed.)
Preparing to unpack .../libpython3.6-minimal_3.6.8-1~16.04.york1_amd64.deb ...
Unpacking libpython3.6-minimal:amd64 (3.6.8-1~16.04.york1) ...
Selecting previously unselected package python3.6-minimal.
Preparing to unpack .../python3.6-minimal_3.6.8-1~16.04.york1_amd64.deb ...
Unpacking python3.6-minimal (3.6.8-1~16.04.york1) ...
Selecting previously unselected package libpython3.6-stdlib:amd64.
Preparing to unpack .../libpython3.6-stdlib_3.6.8-1~16.04.york1_amd64.deb ...
Unpacking libpython3.6-stdlib:amd64 (3.6.8-1~16.04.york1) ...
Selecting previously unselected package python3.6.
Preparing to unpack .../python3.6_3.6.8-1~16.04.york1_amd64.deb ...
Unpacking python3.6 (3.6.8-1~16.04.york1) ...
Processing triggers for man-db (2.7.5-1) ...
Processing triggers for gnome-menus (3.13.3-6ubuntu3.1) ...
Processing triggers for desktop-file-utils (0.22-1ubuntu5.2) ...
Processing triggers for bamfdaemon (0.5.3~bzr0+16.04.20180209-0ubuntu1) ...
Rebuilding /usr/share/applications/bamf-2.index...
Processing triggers for mime-support (3.59ubuntu1) ...
Setting up libpython3.6-minimal:amd64 (3.6.8-1~16.04.york1) ...
Setting up python3.6-minimal (3.6.8-1~16.04.york1) ...
Setting up libpython3.6-stdlib:amd64 (3.6.8-1~16.04.york1) ...
Setting up python3.6 (3.6.8-1~16.04.york1) ...
ubuntu@DESKTOP-D7QB2EH:/mnt/c/Users/user/Desktop/JO/My Clients/IQVIA$ python3.6 -V
Python 3.6.8
================================================================================

ubuntu@DESKTOP-D7QB2EH:/mnt/c/Users/user/Desktop/JO/My Clients/IQVIA$ sudo apt-get update
Hit:1 http://archive.ubuntu.com/ubuntu xenial InRelease
Hit:2 http://archive.ubuntu.com/ubuntu xenial-updates InRelease
Hit:3 http://archive.ubuntu.com/ubuntu xenial-backports InRelease
Hit:4 http://security.ubuntu.com/ubuntu xenial-security InRelease
Hit:6 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial InRelease
Hit:7 http://ppa.launchpad.net/webupd8team/java/ubuntu xenial InRelease
Hit:8 https://deb.nodesource.com/node_6.x xenial InRelease
Ign:9 https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 InRelease
Hit:10 https://dl.yarnpkg.com/debian stable InRelease
Hit:11 https://artifacts.elastic.co/packages/6.x/apt stable InRelease
Ign:12 https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.2 InRelease
Ign:13 https://packages.graylog2.org/repo/debian stable InRelease
Hit:14 https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 Release
Hit:15 https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.2 Release
Hit:16 https://packages.graylog2.org/repo/debian stable Release
Get:5 http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist InRelease [158 kB]
Err:5 http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist InRelease
  Clearsigned file isn't valid, got 'NOSPLIT' (does the network require authentication?)
Fetched 158 kB in 17s (9,274 B/s)
Reading package lists... Done
W: Target Packages (multiverse/binary-amd64/Packages) is configured multiple times in /etc/apt/sources.list.d/mongodb-org-4.0.list:1 and /etc/apt/sources.list.d/mongodb.list:1
W: Target Packages (multiverse/binary-all/Packages) is configured multiple times in /etc/apt/sources.list.d/mongodb-org-4.0.list:1 and /etc/apt/sources.list.d/mongodb.list:1
W: Target Translations (multiverse/i18n/Translation-en_US) is configured multiple times in /etc/apt/sources.list.d/mongodb-org-4.0.list:1 and /etc/apt/sources.list.d/mongodb.list:1
W: Target Translations (multiverse/i18n/Translation-en) is configured multiple times in /etc/apt/sources.list.d/mongodb-org-4.0.list:1 and /etc/apt/sources.list.d/mongodb.list:1
W: Target DEP-11 (multiverse/dep11/Components-amd64.yml) is configured multiple times in /etc/apt/sources.list.d/mongodb-org-4.0.list:1 and /etc/apt/sources.list.d/mongodb.list:1
W: Target DEP-11-icons (multiverse/dep11/icons-64x64.tar) is configured multiple times in /etc/apt/sources.list.d/mongodb-org-4.0.list:1 and /etc/apt/sources.list.d/mongodb.list:1
E: Failed to fetch http://downloads-distro.mongodb.org/repo/ubuntu-upstart/dists/dist/InRelease  Clearsigned file isn't valid, got 'NOSPLIT' (does the network require authentication?)
E: Some index files failed to download. They have been ignored, or old ones used instead.
W: Target Packages (multiverse/binary-amd64/Packages) is configured multiple times in /etc/apt/sources.list.d/mongodb-org-4.0.list:1 and /etc/apt/sources.list.d/mongodb.list:1
W: Target Packages (multiverse/binary-all/Packages) is configured multiple times in /etc/apt/sources.list.d/mongodb-org-4.0.list:1 and /etc/apt/sources.list.d/mongodb.list:1
W: Target Translations (multiverse/i18n/Translation-en_US) is configured multiple times in /etc/apt/sources.list.d/mongodb-org-4.0.list:1 and /etc/apt/sources.list.d/mongodb.list:1
W: Target Translations (multiverse/i18n/Translation-en) is configured multiple times in /etc/apt/sources.list.d/mongodb-org-4.0.list:1 and /etc/apt/sources.list.d/mongodb.list:1
W: Target DEP-11 (multiverse/dep11/Components-amd64.yml) is configured multiple times in /etc/apt/sources.list.d/mongodb-org-4.0.list:1 and /etc/apt/sources.list.d/mongodb.list:1
W: Target DEP-11-icons (multiverse/dep11/icons-64x64.tar) is configured multiple times in /etc/apt/sources.list.d/mongodb-org-4.0.list:1 and /etc/apt/sources.list.d/mongodb.list:1
================================================================================


ubuntu@DESKTOP-D7QB2EH:/mnt/c/Users/user/Desktop/JO/My Clients/IQVIA$ sudo apt autoremove
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages will be REMOVED:
  libuv1
0 upgraded, 0 newly installed, 1 to remove and 11 not upgraded.
After this operation, 170 kB disk space will be freed.
Do you want to continue? [Y/n] y
(Reading database ... 157450 files and directories currently installed.)
Removing libuv1:amd64 (1.8.0-1) ...
Processing triggers for libc-bin (2.23-0ubuntu11) ...
ubuntu@DESKTOP-D7QB2EH:/mnt/c/Users/user/Desktop/JO/My Clients/IQVIA$
================================================================================


ubuntu@DESKTOP-D7QB2EH:/mnt/c/Users/user/Desktop/JO/My Clients/IQVIA$ sudo apt install python-pip
Reading package lists... Done
Preparing to unpack .../python-pip-whl_8.1.1-2ubuntu0.4_all.deb ...
Unpacking python-pip-whl (8.1.1-2ubuntu0.4) ...
Selecting previously unselected package python-pip.
Preparing to unpack .../python-pip_8.1.1-2ubuntu0.4_all.deb ...
Unpacking python-pip (8.1.1-2ubuntu0.4) ...
Selecting previously unselected package python-pkg-resources.
Preparing to unpack .../python-pkg-resources_20.7.0-1_all.deb ...
Unpacking python-pkg-resources (20.7.0-1) ...
Selecting previously unselected package python-setuptools.
Preparing to unpack .../python-setuptools_20.7.0-1_all.deb ...
Unpacking python-setuptools (20.7.0-1) ...
Selecting previously unselected package python-wheel.
Preparing to unpack .../python-wheel_0.29.0-1_all.deb ...
Unpacking python-wheel (0.29.0-1) ...
Processing triggers for man-db (2.7.5-1) ...
Setting up libpython2.7-dev:amd64 (2.7.12-1ubuntu0~16.04.8) ...
Setting up libpython-dev:amd64 (2.7.12-1~16.04) ...
Setting up libpython-all-dev:amd64 (2.7.12-1~16.04) ...
Setting up python-all (2.7.12-1~16.04) ...
Setting up python2.7-dev (2.7.12-1ubuntu0~16.04.8) ...
Setting up python-dev (2.7.12-1~16.04) ...
Setting up python-all-dev (2.7.12-1~16.04) ...
Setting up python-pip-whl (8.1.1-2ubuntu0.4) ...
Setting up python-pip (8.1.1-2ubuntu0.4) ...
Setting up python-pkg-resources (20.7.0-1) ...
Setting up python-setuptools (20.7.0-1) ...
Setting up python-wheel (0.29.0-1) ...
ubuntu@DESKTOP-D7QB2EH:/mnt/c/Users/user/Desktop/JO/My Clients/IQVIA$
================================================================================

ubuntu@DESKTOP-D7QB2EH:/mnt/c/Users/user/Desktop/JO/My Clients/IQVIA$ pip install --upgrade pip
Collecting pip
  Downloading https://files.pythonhosted.org/packages/30/db/9e38760b32e3e7f40cce46dd5fb107b8c73840df38f0046d8e6514e675a1/pip-19.2.3-py2.py3-none-any.whl (1.4MB)
    100% |¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦| 1.4MB 489kB/s
Installing collected packages: pip
Successfully installed pip-19.2.3
ubuntu@DESKTOP-D7QB2EH:/mnt/c/Users/user/Desktop/JO/My Clients/IQVIA$
================================================================================

ubuntu@DESKTOP-D7QB2EH:/mnt/c/Users/user/Desktop/JO/My Clients/IQVIA$ mkdir contact_service_flask
ubuntu@DESKTOP-D7QB2EH:/mnt/c/Users/user/Desktop/JO/My Clients/IQVIA$ ls -altr
total 42524
drwxrwxrwx 1 ubuntu ubuntu     4096 Sep 17 10:51 ..
-rwxrwxrwx 1 ubuntu ubuntu    16078 Sep 17 10:51 Technical Test.docx
-rwxrwxrwx 1 ubuntu ubuntu 43512424 Sep 17 11:37 materials-master.zip
-rwxrwxrwx 1 ubuntu ubuntu    11370 Sep 17 12:03 info.ifo
drwxrwxrwx 1 ubuntu ubuntu     4096 Sep 17 12:04 contact_service_flask
drwxrwxrwx 1 ubuntu ubuntu     4096 Sep 17 12:04 .
ubuntu@DESKTOP-D7QB2EH:/mnt/c/Users/user/Desktop/JO/My Clients/IQVIA$ cd contact*
ubuntu@DESKTOP-D7QB2EH:/mnt/c/Users/user/Desktop/JO/My Clients/IQVIA/contact_service_flask$
================================================================================






