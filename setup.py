import sys

import os
from pathlib import Path
from setuptools import setup

py2exe_build = False
py2app_build = False

if "py2exe" in sys.argv:
    try:
        import py2exe

        py2exe_build = True
    except ImportError:
        print("Cannot find py2exe")
elif "py2app" in sys.argv:
    py2app_build = True

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

test_requirements = [
    'pytest',
    'pytest-cov',
    'pytest-faulthandler',
    'pytest-mock'
]

import kuberider

app_name = kuberider.__appname__
version = kuberider.__version__
description = kuberider.__description__

dist_dir = Path(os.getcwd()).joinpath('dist').as_posix()

APP = ['kuberider/main.py']

if py2app_build:
    py2app_options = {
        'iconfile': 'packaging/data/icons/kuberider.icns'
    }

    extra_options = dict(
        app=APP,
        options={'py2app': py2app_options},
    )
else:
    extra_options = dict()

setup(
    name=app_name,
    version=version,
    description=description,
    author="nmn",
    author_email='info@deskriders.dev',
    url='https://github.com/namuan/kube-rider',
    packages=[
        'kuberider',
        'kuberider.core',
        'kuberider.domain',
        'kuberider.entities',
        'kuberider.events',
        'kuberider.generated',
        'kuberider.images',
        'kuberider.presenters',
        'kuberider.settings',
        'kuberider.themes',
        'kuberider.ui',
        'kuberider.widgets'
    ],
    package_data={
        'kuberider.images': ['*.png'],
        'kuberider.themes': ['*.qss', '*.css']
    },
    entry_points={
        'gui_scripts': [
            'context=kuberider.main:main'
        ]
    },
    install_requires=requirements,
    zip_safe=False,
    keywords='Desktop Kubernetes Client',
    test_suite='tests',
    tests_require=test_requirements,
    **extra_options
)

if py2app_build:
    print('*** Removing unused Qt frameworks ***')
    framework_dir = os.path.join(dist_dir, "kuberider.app/Contents/Resources/lib/python{0}.{1}/PyQt5/Qt/lib".format(
        sys.version_info.major, sys.version_info.minor))
    frameworks = [
        'QtDeclarative.framework',
        'QtHelp.framework',
        'QtMultimedia.framework',
        'QtScript.framework',
        'QtScriptTools.framework',
        'QtSql.framework',
        'QtDesigner.framework',
        'QtTest.framework',
        'QtWebKit.framework',
        'QtXMLPatterns.framework',
        'QtCLucene.framework',
        'QtBluetooth.framework',
        'QtConcurrent.framework',
        'QtMultimediaWidgets.framework',
        'QtPositioning.framework',
        'QtQml.framework',
        'QtQuick.framework',
        'QtQuickWidgets.framework',
        'QtSensors.framework',
        'QtSerialPort.framework',
        'QtWebChannel.framework',
        'QtWebKitWidgets.framework',
        'QtWebSockets.framework']

    for framework in frameworks:
        for root, dirs, files in os.walk(os.path.join(framework_dir, framework)):
            for file in files:
                os.remove(os.path.join(root, file))
