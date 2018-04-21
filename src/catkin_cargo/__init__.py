def create_cargo_build_job(context, package, package_path, dependencies, **kwargs):
    pass


description = dict(
    build_type='cargo',
    description='Build a rust package using Cargo',
    create_build_job=create_cargo_build_job
)
