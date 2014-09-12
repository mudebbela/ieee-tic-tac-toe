Introduction
============

Welcome to the CSU IEEE Tic-Tac-Toe Repository!

We will use this repository to collectively create a game of
[Tic-Tac-Toe](http://en.wikipedia.org/wiki/Tic-tac-toe) using the Python
programming language.

Instructions
============

You will be paired with a partner to do "Pair Programming". This means that
with one computer, you will take turns with your partner operating the
keyboard. The person that isn't using the keyboard will help the person program
by reviewing the code, suggesting ways to do things, discussing the code
structure with the typer, or trying out code on their computer, etc.

Each pair of programmers will be responsible for implementing one function that
is part of the total Tic-Tac-Toe program.

First go to http://www.github.com/moorepants/ieee-tic-tac-toe and press the
"Fork" button in the top right of the window. This will copy my git repository
to your Github account. You should now see a repository at
http://www.github.com/<your-username>/ieee-tic-tac-toe.

Now you need to copy your Fork down to your computer using the git clone
command so you can edit the files on your computer. Open a terminal window (or
Git bash)

```bash
$ git clone https://github.com/<your-username>/ieee-tic-tac-toe.git
```

**Be sure to not clone from the moorepants username!**

This creates a new directory in the current working directory. Now change
directory into the repository.

```bashsession
$ cd ieee-tic-tac-toe
```

Make a branch to contain your work:

```bashsession
$ git branch my_branch
$ git checkout my_branch
```

Now you are ready to edit your files.

You will be assigned one of the functions in the `tic_tac_toe.py` file and it
will be you and your partner's responsibility to get that function working as
specified.

To check if your function passes the test you can import the test function for
your function in the Python interpreter and run the test. This shows how to
test the `print_board` function.

```bashsession
$ python
```

```pythonconsole
>>> from test_tic_tac_toe import test_print_board
>>> test_print_board()
```

You can also run all the tests from the terminal with:

```bashsession
$ python test_tic_tac_toe.py
```

And you will see an output like:

```
The test_print_board failed.
The test_get_player_token_choice failed.
The test_who_goes_first failed.
The test_get_player_move failed.
The test_get_computer_move failed.
The test_is_space_free failed.
The test_is_there_a_win failed.
The test_get_play_again failed.
The test_is_board_full failed.
```

If you get an error message then you need to improve your function. If there is
no output, then your function is ready to be merged into the main repository!

Once you have the function working as desired then you should commit your
changes to git on your computer, for example to commit the changes to the
`tic_tac_toe.py` file:

```bashsession
$ git commit tic_tac_toe.py -m "Implemented the XXXXX function, test passes."
```

Now that you've committed the changes to your branch on your computer you can
send them up to Github so that we can get the change merged into the main
repository:

```bashsession
$ git push origin my_branch
```

Now go to the repository on your Github account (i.e. under your username).

You should see a new bar across the screen asking if you want to submit a pull
request. Click the green button to submit a pull request to the main
repository.

At this point you should find a person from another team to review the pull
request that you made. Once they approve the code, get Jason's attention and he
can merge the pull request into the main repository.

Getting changes other people made to the repository
---------------------------------------------------

First make sure you are on the master branch. We will use the master branch of
your fork on your computer to manage pull in changes from the main repository.

```bashsession
$ git checkout master
```

Now we will add a remote repository URL so that you can connect to the main
repository and pull changes from that.

```bashsession
$ git remote add main_repo https://github.com/moorepants/ieee-tic-tac-toe.git
```

Now you can use the ``git pull`` command to bring down the changes:

```bashsession
$ git pull main_repo master
```

This will make the master branch on your computer reflect the master branch on
the main repository on Github. You should do this periodically to get the
changes from your pull requests and from other pull requests. At some point,
once all the functions are done, you will have a working tic-tac-toe game!
