For development it’s often convenient to run Kubernetes on your desktop.
Two popular ways to do this are with [Kubernetes
Minikube](https://kubernetes.io/docs/getting-started-guides/minikube/)
or [Kubernetes support in Docker for
Desktop](https://docs.docker.com/docker-for-mac/kubernetes/).

In this guide we’ll use Docker for Desktop.

# Install

Install [Docker for
Mac](https://docs.docker.com/docker-for-mac/install/) or [Docker for
Windows](https://docs.docker.com/docker-for-windows/install/).

Starting with version 18.06 Docker for Desktop includes Kubernetes
support.

# Enable Kubernetes Support

Enable [Kubernetes Support for
Mac](https://docs.docker.com/docker-for-mac/#kubernetes) or [Kubernetes
Support for
Windows](https://docs.docker.com/docker-for-windows/#kubernetes).

Once Kubernetes installation is complete, make sure you have your
context set correctly to use docker-for-desktop.

<div class="formalpara">

<div class="title">

Make sure K8s context is set to docker-for-desktop

</div>

``` bash
kubectl config get-contexts
kubectl config use-context docker-for-desktop
kubectl cluster-info
kubectl version
kubectl get nodes
```

</div>
