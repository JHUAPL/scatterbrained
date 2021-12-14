# Installation Guide

Installing Scatterbrained on your development machine can be done either through pip or by downloading the source code and installing it locally.

## Pip-based Installation

```shell
pip install scatterbrained
```

This will automatically install the latest stable version of Scatterbrained, along with its dependencies. For a complete list of dependencies, see the `requirements/` directory in this repository.

## Source-based Installation

You can also clone the git repository and install Scatterbrained from source. In this case, you will also need to manually install the dependencies.

```shell
git clone https://github.com/JHUAPL/scatterbrained.git
cd scatterbrained

# Install dependencies:
pip install -r requirements/requirements.txt

# Install the library in "editable"/development mode:
pip install -e .
```

## Container-based Installation

It is also possible to install and Scatterbrained in a Docker container. This can be useful for running multiple instances of Scatterbrained on the same machine, for testing or benchmarking.

Docker-based instructions coming soon.

## Installation Troubleshooting

Click the carrot next to each question to see the full troubleshooting guide.

<details>
<summary><b>Errors when installing on Ubuntu ≤14</b></summary>

This is likely due to an older version of 0MQ installed with `apt-get`. If you're sure you don't have software that relies upon this older version, then run the following commands to remove the old version of 0MQ and install the latest version of 0MQ:

    sudo apt-get remove libzmq-dev python-zmq
</details>
