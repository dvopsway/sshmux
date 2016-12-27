## Contributer's Guide

Thanks for your interest in the project! We welcome pull requests from
developers of all skill levels. To get started, simply fork the master branch
on GitHub to your personal account and then clone the fork into your
development environment.

Padmakar Ojha (**dvopsway** on github) is the original creator of the
SSHmux projet, and currently maintains the project along with Rob Haverkamp (**rjrhaverkamp** on GitHub and Twitter).

Please don't hesitate to reach out if you have any questions, or just need a
little help getting started.

### Pull Requests

Before submitting a pull request, please ensure you have added or updated tests as appropriate, and that all existing tests still pass with your changes on both Python 2 and Python 3. Please also ensure that your coding style follows PEP 8.


### Test coverage

Pull requests won't be merged when test coverage decreases. This helps ensure the quality of the project. To check coverage before submitting a pull request:

```bash
$ COVERAGE_FILE=.coverage_ssh coverage run tests/test_ssh.py
$ COVERAGE_FILE=.coverage_validations coverage run tests/test_validations.py
$ coverage combine .coverage_ssh .coverage_validations
```

### Code style rules

* always follow the [Google styleguide](http://google.github.io/styleguide/pyguide.html)
* Docstrings are required for classes, attributes, methods, and functions.
* Please try to be consistent with the way existing docstrings are formatted. In particular, note the use of single vs. double backticks as follows:
    * Double backticks
        * Inline code
        * Variables
        * Types
        * Decorators
    * Single backticks
        * Methods
        * Params
        * Attributes
* Format non-trivial comments using your GitHub nick and one of these prefixes:
    * TODO(rjrhaverkamp): Clean up this part of the code
    * NOTE(rjrhaverkamp): remeber, 1+1=2
    * PERF(rjrhaverkamp): blazingly fast!
* When catching exceptions, name the variable `ex`.
* Use whitespace to separate logical blocks of code and to improve readability.
* No single-character variable names except for trivial indexes when looping,
or in mathematical expressions implementing well-known formulas.
* Heavily document code that is especially complex and/or clever.
* When in doubt, optimize for readability.

### Commit Message Format

SSHmux's commit message format looks like AngularJS's style guide, reproduced here for convenience, with some minor edits for clarity.

Each commit message consists of a **header**, a **body** and a **footer**. The header has a special format that includes a **type** and a **subject**:

```
<type>: <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

No line may exceed 100 characters. This makes it easier to read the message on GitHub as well as in various git tools.

#####  Type
Must be one of the following:

* **feat**: A new feature
* **fix**: A bug fix
* **docs**: Documentation only changes
* **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
* **refactor**: A code change that neither fixes a bug or adds a feature
* **perf**: A code change that improves performance
* **test**: Adding missing tests
* **chore**: Changes to the build process or auxiliary tools and libraries such as documentation generation

##### Subject
The subject contains succinct description of the change:

* use the imperative, present tense: "change" not "changed" nor "changes"
* don't capitalize first letter
* no dot (.) at the end

##### Body
Just as in the **subject**, use the imperative, present tense: "change" not "changed" nor "changes"The body should include the motivation for the change and contrast this with previous behavior.

##### Footer
The footer should contain any information about **Breaking Changes** and is also the place to reference GitHub issues that this commit **Closes**.

so a `commit` might be done like this:  `git commit -m "feat: add multiprocessing" -m "Execute command on multiple servers at the same time to increase performance" -m "breaks password support, closes #25"`