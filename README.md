
<h1 align='center'>Scatterbrained</h1>
<p align='center'>Decentralized Federated Learning</p>
<p align='center'>
<a href="https://pypi.org/project/scatterbrained/"><img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/scatterbrained?style=for-the-badge"></a>
<a href="https://github.com/JHUAPL/scatterbrained"><img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/JHUAPL/scatterbrained?style=for-the-badge"></a>
<a href="https://www.apache.org/licenses/LICENSE-2.0"><img alt="GitHub" src="https://img.shields.io/github/license/JHUAPL/scatterbrained?style=for-the-badge"></a>
</p>


Scatterbrained makes it easy to build federated learning systems. In addition to traditional federated learning, Scatterbrained supports decentralized federated learning — a new, cooperative type of federated learning where the learning is done by a group of peers instead of by a centralized server. For more information, see our 2021 paper, [_Scatterbrained: A flexible and expandable pattern for decentralized machine learning_](#).

You can use your favorite machine learning frameworks alongside Scatterbrained, such as TensorFlow, SciKit-Learn, or PyTorch.

## Usage

For examples of how to get started using Scatterbrained, see the [Examples](examples/) directory.

## Installation

You can install Scatterbrained with pip:

```shell
pip install scatterbrained
```

If you would rather download and install from source, you can do so with the following:

```shell
git clone https://github.com/JHUAPL/scatterbrained.git
cd scatterbrained
```

You must first install the dependencies with:

```shell
pip3 install -r ./requirements/requirements.txt
```

And then you can install the package with:

```shell
pip3 install -e .
```

## License

The code in this repository is released under an Apache 2.0 license. For more information, see [LICENSE](LICENSE).

> Copyright 2021 The Johns Hopkins Applied Physics Laboratory
>
> Licensed under the Apache License, Version 2.0 (the "License");
> you may not use this file except in compliance with the License.
> You may obtain a copy of the License at
>
>   http://www.apache.org/licenses/LICENSE-2.0
>
> Unless required by applicable law or agreed to in writing, software
> distributed under the License is distributed on an "AS IS" BASIS,
> WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
> See the License for the specific language governing permissions and
> limitations under the License.
