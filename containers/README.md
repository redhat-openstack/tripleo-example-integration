Container Builds
================

Checkout this [guide][1] for further inforomation on extending tripleo-containers.

[1]: https://docs.openstack.org/project-deploy-guide/tripleo-docs/latest/deployment/3rd_party.html#extend-tripleo-containers

Example build
-------------

Here is an example tripleo container image build command for use with this
folder.

```
openstack tripleo container image build \
        --namespace example-service \
        --prefix foobar- \
        --config-file containers/examples-containers.yaml \
        --config-path containers/
```
