# Getting Started with Scatterbrained

This is a quickstart tutorial for the Scatterbrained federated learning library. It will assume that you have already installed the library and have a working, high-level understanding of federated learning.

* For installation instructions, see [Installation](../installation/README.md).
* For a refresher on federated learning, see this [Wikipedia article](https://en.wikipedia.org/wiki/Federated_learning).

## Step 1: Building a model

For this example, we're going to build a basic linear regression model using `torch`. (You can also use other machine learning frameworks, such as TensorFlow or sklearn!) We'll load a simple built-in dataset, and train a linear regression model on it.


```python
import sklearn.datasets
from sklearn.model_selection import train_test_split

import torch
import torch.nn as nn
from torch import optim

# Load the data
X, y = sklearn.datasets.load_diabetes(return_X_y=True)

# Generate train/test splits
(X_train, X_val, y_train, y_val) = train_test_split(
    X, y, test_size=0.2
)

# Create the data loaders for torch
train = DataLoader(
    TensorDataset(
        torch.from_numpy(X_train), torch.from_numpy(y_train)
    ),
    batch_size=32, shuffle=True
)
val = DataLoader(
    TensorDataset(
        torch.from_numpy(X_val), torch.from_numpy(y_val)
    ),
    batch_size=32, shuffle=True
)


# Create the model
model = nn.Linear(X_train.shape[1], 1)
create_optimizer = lambda model: optim.AdamW(model.parameters())
```

In the codeblock above, we've created a model just like we would in a traditional ML pipeline. We've also created a function that returns an optimizer. So far, we're not doing anything "FL-flavored": This is just plain old ML.

## Step 2: Training the model

It's now time to introduce the Scatterbrained library. Training a model is still quite simple:

```python
import scatterbrained as sb

NUM_EPOCHS = 10

# Create a new scatterbrained Node to hold all of the logic
# for a federated learning compute node:
async with sb.Node() as node:

    # Create a new Namespace. This is a unique identifier
    # shared by all nodes in the same FL community. Other
    # nodes on the same network that know this name can join
    # your FL cluster:

    async with node.namespace(
        "MyFirstNamespace", model, create_optimizer
    ) as ns:

        # Finally we can ask scatterbrained to perform the
        # training loop for us in a background thread:
        await ns.train(NUM_EPOCHS, trainloader, validloader)

        # At the same time, we can also serve our node's
        # resources to other nodes on the network:
        await ns.serve()

```

## Step 3: Joining the cluster

From another machine on the same network (or the same machine on a different port), you can join the cluster by running the following code.

Unlike the code blocks above, where we built up a file gradually, this is all the code you need to run from your second machine:

```python
import scatterbrained as sb

async with sb.Node() as node:
    async with node.join("MyFirstNamespace") as ns:
        await ns.sync_model() # This line is different!
        await ns.serve()
```

Wow, that's succinct! Let's take a look at what's happening behind the scenes when we run this code.

First, we create a new scatterbrained Node, just like before. And just like in the first example, we create a new Namespace with the same name, so that the nodes know they're allowed to talk to each other. (A sb.Node can't cooperatively learn with a Node training a different model, so we use the Namespace to indicate to the Node that this networked peer is speaking the same language — i.e., using the same model.)

But here we don't specify any training data or model architecture: Instead, we use the `sync_model` method so that this node can download the model from another peer Node on the network. This means that you can use Scatterbrained to quickly transit a model from one machine to another. (In other words, your models will always be in sync, with a single node serving as the source of truth.)

## Next Steps

In this tutorial, we've covered the basics of using Scatterbrained to train a model. But there are many other features that you can use to tailor your decentralized federated learning code. For example,

* You can emulate traditional, centralized federated learning if you want a single machine to serve as an authority
* You can train a model on multiple machines in parallel with different datasets
* You can specify different optimizers for different Nodes
* You can change your network topology so that nodes can communicate with only certain peers, and will ignore others
* You can design custom network topologies so that information can only flow in certain directions
