Scripts:
0-iam_betty: switches the current user to the user betty.
1-who_am_i:  prints the effective username of the current user.
2-groups: prints all the groups the current user is part of.
3-new_owner: changes the owner of the file hello to the user betty.
4-empty: creates an empty file called hello.
5-execute: adds execute permission to the owner of the file hello. The file hello will be in the working directory.
6-multiple_permissions: execute permission to the owner and the group owner, and read permission to other users, to the file hello. The file hello will be in the working directory
7-everybody: execution permission to the owner, the group owner and the other users, to the file hello.
8-James_Bond:  permission to the file hello as follows:
    Owner: no permission at all
    Group: no permission at all
    Other users: all the permissions
9-John_Doe: sets the mode of the file hello to this:

-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello

    The file hello will be in the working directory
    You are not allowed to use commas for this script
10-mirror_permissions: sets the mode of the file hello the same as olleh’s mode.

    The file hello will be in the working directory
    The file olleh will be in the working directory
11-directories_permissions: adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users.
12-directory_permissions: creates a directory called my_dir with permissions 751 in the working directory.
13-change_group: changes the group owner to school for the file hello.
