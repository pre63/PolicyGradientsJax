from setuptools import setup, find_packages

setup(
    name="policy_gradients_jax",
    version="0.1.0",
    description="On-Policy Policy Gradient Algorithms in JAX",
    author="Matt00n",
    author_email=None,
    url="https://github.com/pre63/PolicyGradientsJax",
    packages=find_packages(),
    install_requires=[
        "absl-py",
        "cloudpickle",
        "dataclasses",
        "flax",
        "mujoco-py",
        "gymnasium",
        "gymnasium[mujoco]",
        "jax",
        "numpy",
        "optax",
        "torch",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    include_package_data=True,
)
