from typing import Any

from Cython.Build import cythonize
from setuptools.command.build_ext import build_ext
from setuptools.extension import Extension

ext_modules = [
    Extension(
        "demo.core",
        sources=["lib/core.pyx", "lib/libcore.cpp"],
        language="c++",
        extra_compile_args=["-std=c++17"],
        extra_link_args=["-std=c++17"],
    ),
]


def build(setup_kwargs: dict[str, Any]):
    setup_kwargs.update(
        {
            "ext_modules": cythonize(ext_modules),
            "cmdclass": {"build_ext": build_ext},
        }
    )
