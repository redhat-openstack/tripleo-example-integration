tcib
====

This folder should contain folders defining the services that can be built using
`openstack tripleo container image build`. To define containers that have a
parent and child relationship, simply put the child service containers within
the parent container's folder. For example...

```
.
├── example-service
│   └── example-service.yaml
├── parent-service
│   ├── child-service
│   │   └── child-service.yaml
│   └── parent-service.yaml
└── README.md
```

