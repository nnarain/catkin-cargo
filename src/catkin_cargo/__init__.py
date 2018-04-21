import os

from catkin_tools.execution.jobs import Job
from catkin_tools.execution.stages import CommandStage


def create_cargo_build_job(context, package, package_path, dependencies, **kwargs):
    # get build settings
    pkg_dir = os.path.join(context.source_space_abs, package_path)

    build_space = context.package_build_space(package)
    devel_space = context.package_devel_space(package)
    install_space = context.package_install_space(package)
    metadata_path = context.package_metadata_path(package)

    env = dict(os.environ)

    # create a cargo build command stage
    cargo_build_cmd = CommandStage(
        'cargo',
        ['cargo', 'build'],
        cwd=pkg_dir,
        env=env,
        shell=True
    )

    # add all stages
    stages = [
        cargo_build_cmd
    ]

    return Job(
        jid=package.name,
        deps=dependencies,
        env=env,
        stages=stages)    


description = dict(
    build_type='cargo',
    description='Build a rust package using Cargo',
    create_build_job=create_cargo_build_job
    #create_clean_job=...
)
