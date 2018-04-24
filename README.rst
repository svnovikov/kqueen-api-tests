Overview
--------

Functional API tests for KQueen (Kubernetes cluster manager) https://github.com/Mirantis/kqueen

Requirements
------------

-  Python v3.6 and higher.
-  Pip v3 and higher.
-  Docker stable release (v17.03 and higher is preferable).
-  Docker-compose stable release (v1.16.0 and higher is preferable).

  For Ubuntu 16.04 required packages are: libsasl2-dev python-dev libldap2-dev libssl-dev
  For Fedora: openldap-devel

Howto run tests
---------------

Fill the config file `kqueen_api_tests/config.yaml` and execute the following command:

    ::

      pytest
