#!/bin/bash

#Delete any existing directory with the same name
#This is helpful if you are testing the script because otherwise you'll have to manually delete the folder everytime
#Code commented for now because it is the final tested version
# rm -rf "task1"

#create new directory:
mkdir task1
cd task1

#initialize repo:
git init
for i in `seq 1 5`;
do
	touch "file_$i"
	git add "file_$i"
	git commit -m "adding file $i"
done

#go to first commit, creat branch and add 3:
git checkout HEAD~4
git checkout -b feature
for i in `seq 6 8`;
do
	touch "file_$i"
	git add "file_$i"
	git commit -m "adding file $i"
done

#rebase 4 and 5 to feature:
git rebase --onto feature master~2 master

#Move to the old commit using HEAD@{X}. use reflog to find the X
#git reflog show  #to be run only once to determine X
git checkout HEAD@{11}

#create a branch and add commit 9
git checkout -b debug
touch "file_9"
git add "file_9"
git commit -m "adding file 9"

#Amend the commit 9 to contain file7
git checkout feature file_7
git commit --amend --no-edit

#view the final tree. This is not required for the homework but helps view the final structure of the repository.
git log --graph --oneline master feature debug