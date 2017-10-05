How to contribute

Extending the programs to every possible combination of hardware platform is what makes pyHoliday great. It's impractical to own all the various gadgets that could run pyHoliday and nor should you which is why Python was chosen to be the backbone of pyHoliday. I want to keep it as easy as possible to contribute changes or wholesale programs to get you up and running with your program/hardware. There are only a few guidelines I need contributors to follow to keep on keeping on!

pyHoliday vs Programs

Currently I have setup pyHoliday in a heavily manual process due to time and simplification of the process in regards to adding or removing programs. As the project and programs grow I anticipate scraping of a sorts the current programs and having pyHoliday give them as options. As an end-user selects that program it will reach back to the repository and grab the necessary files or some other combination (TBD).

For communication a Discord channel has been setup at https://discord.gg/6Na857j.

Getting Started

Make sure you have a GitHub account.
Create an issue, assuming one does not already exist.
Clearly describe the issue including steps to reproduce when it is a bug.
Make sure you fill in the earliest version that you know has the issue.
Fork the repository on GitHub.

Making Changes

Create a topic branch from where you want to base your work.

This is usually the master branch.
Only target release branches if you are certain your fix must be on that branch.
To quickly create a topic branch based on master, run git checkout -b fix/master/my_contribution master. Please avoid working directly on the master branch.
Make commits of logical units.

Check for unnecessary whitespace with git diff --check before committing.

Make sure your commit messages are in the proper format. If the commit addresses an issue filed in the GitHub project, start the first line of the commit with the issue number in parentheses.

    (pyHoliday-1234) Make the example in CONTRIBUTING imperative and concrete

    Without this patch applied the example commit message in the CONTRIBUTING
    document is not a concrete example. This is a problem because the
    contributor is left to imagine what the commit message should look like
    based on a description rather than an example. This patch fixes the
    problem by making the example concrete and imperative.

    The first line is a real-life imperative statement with a ticket number
    from our issue tracker. The body describes the behavior without the patch,
    why this is a problem, and how the patch fixes the problem when applied.
Make sure you have added the necessary tests for your changes.

Run all the tests to assure nothing else was accidentally broken.

It is the responsibility of contributors and code reviewers to ensure that all user-facing strings are marked in new PRs before merging.

Making Trivial Changes

Documentation

For changes of a trivial nature to comments and documentation, it is not always necessary to create a new issue. In this case, it is appropriate to start the first line of a commit with (docs) instead of an issue.

If an issue exists for the documentation commit, you can include it after the (docs) token.

    (docs)(DOCUMENT-000) Add docs commit example to CONTRIBUTING

    There is no example for contributing a documentation commit
    to the pyHoliday repository. This is a problem because the contributor
    is left to assume how a commit of this nature may appear.

    The first line is a real-life imperative statement with '(docs)' in
    place of what would have been the PUP project ticket number in a
    non-documentation related commit. The body describes the nature of
    the new documentation or comments added.
For commits that address trivial repository maintenance tasks or packaging issues, start the first line of the commit with (maint) or (packaging), respectively.

Submitting Changes

Push your changes to a topic branch in your fork of the repository.
Submit a pull request to the repository.
Update your issue to mark that you have submitted code and are ready for it to be reviewed (Status: Ready for Merge).
Include a link to the pull request in the issue.

Revert Policy

By running tests in advance and by engaging with peer review for prospective changes, your contributions have a high probability of becoming long lived parts of the the project. After being merged, the code will run through a series of testing pipelines on a large number of operating system environments. These pipelines can reveal incompatibilities that are difficult to detect in advance.

If the code change results in a test failure, we will make our best effort to correct the error. If a fix cannot be determined and committed within a few hours of its discovery, the commit(s) responsible may be reverted, at the discretion of the committer and pyHoliday maintainers. This action would be taken to help maintain passing states in our testing pipelines.

The original contributor will be notified of the revert in the issue associated with the change. A reference to the test(s) and operating system(s) that failed as a result of the code change will also be added to the issue. This test(s) should be used to check future submissions of the code to ensure the issue has been resolved.
