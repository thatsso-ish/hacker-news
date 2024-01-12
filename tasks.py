from invoke import task

@task
def spec(ctx):
    ctx.run("pytest")

@task
def rubocop(ctx):
    ctx.run("flake8 || true")

@task(default=True, pre=[rubocop, spec])
def default(ctx):
    pass
