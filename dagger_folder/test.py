"""Run tests for a single Python version."""

import sys

import anyio

import dagger


async def test():
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        # get reference to the local project
        src = client.host().directory(".")

        python = (
            client.container().from_("python:3.13.0a4-slim-bullseye")
            # mount cloned repository into image
            .with_directory("/src", src)
            # set current working directory for next commands
            .with_workdir("/src")
            # install test dependencies
            .with_exec(["pip", "install", "-r", "requirements.txt"])
            # run tests
            .with_exec(["pytest", "tests.py"])
        )

        # execute
        await python.sync()

    print("Tests succeeded!")


anyio.run(test)
