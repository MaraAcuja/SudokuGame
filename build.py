#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.sphinx")


name = "SudokuGame"
default_task = "publish"


@init
def set_properties(project):
    project.depends_on('unittest')
    project.depends_on('numpy')
    project.set_property('sphinx_config_path', 'docs/')
    project.set_property('sphinx_source_dir', 'docs/source')
    project.set_property('sphinx_output_dir', 'docs/_build')
    project.set_property("coverage_break_build", False)

