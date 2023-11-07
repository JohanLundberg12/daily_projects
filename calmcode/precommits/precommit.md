### Install

```
pip install pre-commit
```

```
pre-commit sample-config > .pre-commit-config.yaml
```

```
pre-commit install
```

### Usage
```
git add readme_with_errors.md
```
```
gcmsg "add readme file"
```

Output of gcmsg:
'''
[INFO] Initializing environment for https://github.com/pre-commit/pre-commit-hooks.
[INFO] Installing environment for https://github.com/pre-commit/pre-commit-hooks.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
Trim Trailing Whitespace.................................................Failed
- hook id: trailing-whitespace
- exit code: 1
- files were modified by this hook

Fixing calmcode/precommits/readme_with_errors.md
'''
We see that it modifies the file. We now need to add it and commit again.

```
ga readme_with_errors.md
gcmsg "readme"
```

'''
Trim Trailing Whitespace.................................................Passed
Fix End of Files.........................................................Passed
Check Yaml...........................................(no files to check)Skipped
Check for added large files..............................................Passed
[main dd45322] readme
 1 file changed, 3 insertions(+)
 create mode 100644 calmcode/precommits/readme_with_errors.md
'''


### adding new hooks

Go to: https://pre-commit.com/hooks.html to see more hooks.
After adding new hooks to your .pre-commit-config.yaml file, run:
```
pre-commit install
```

Some hooks are hosted on github/gitlab. For those, we need to add it to
our .pre-commit-config.yaml file like this:
'''
-   repo: https://github.com/PyCQA/flake8
    rev: 34cbf8e
    hooks:
    -   id: flake8
''' where the rev is the commit-sha that we need to find on github/gitlab.

### Other

Some files/errors will not be changed by pre-commit, i.e. settings.json.
This we must fix manually.


Spelling can be fixed using a hook such as:

-   repo: https://github.com/codespell-project/codespell
    rev: v1.16.0
    hooks:
    -   id: codespell
        name: codespell
        description: Checks for common misspellings in text files.
        entry: codespell readme_with_errors.md settings.json code.py
        language: python
        types: [text]

However, note that it is not perfect. It can however, be used for many types of files.


### autoupdate

It is good to update the hooks in the .pre-commit-config.yaml as they get updated.
We can do that with:
```
pre-commit autoupdate
```

Note that this will alter the file.
