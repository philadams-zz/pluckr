from fabric.api import local


def distribution_register():
    local('python setup.py register')

def distribution_prepare():
    local('python setup.py sdist')

def distribution_distribute():
    local('python setup.py sdist upload')
