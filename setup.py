from setuptools import setup, find_packages

setup(
    name='catkin-cargo',
    version='0.0.1',
    author='Natesh Narain',
    author_email='nnaraindev@gmail.com',
    description='catkin build type for cargo packages',
    licence='MIT',
    keywords='catkin rust cargo ros',

    package_dir = {'':'src'},
    packages=['catkin_cargo'],

    install_requires=['catkin_pkg'],

    entry_points = {
        'catkin_tools.jobs': [
            'cargo = catkin_cargo.description'
        ]
    }
)