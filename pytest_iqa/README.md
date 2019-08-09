# IQAInstance
IQAInstance is used as a helper that can process an ansible inventory file
and instantiate messaging components defined through the nodes.

The following sections explain what variables must be defined in the inventory
file to associate a given node with one of the supported messaging components.

## Defining messaging components on Ansible inventory files
Tables below demonstrate the allowed variable list needed by IQAInstance class, so it can load the Ansible inventory file, loading all components properly.

We are not considering the standard ansible variables, like ansible_host, ansible_connection and etc (which must be defined if using Ansible purely).

***Notes:***
1. If the host is defined in the inventory file with an ansible_connection = docker, then a ServiceDocker instance will be instantiated and used in the related Server instance.
2. When running a “Server” component (Router or Broker) inside a container, you must set its executor variable to “docker” as well (meaning start/stop of the related component will be done by starting/stopping its related container)


## Client variables
| Variable name  | Sample value | Description |
|----------------|--------------|-------------|
|	component      | client       | Type of component that will be instantiated by IQAInstance (client, router or broker) |
|	implementation | java, python or nodejs| The instance that will be created using Client Command Factory |

## Router variables
| Variable name |	Sample value | Description |
|---------------|--------------|-------------|
|	component | router | Type of component that will be instantiated by IQAInstance |
|	implementation | dispatch | (***Optional***) Supported implementation of a router component (default and only available is dispatch) |
|	router_port | 5672 | Listener port that can be used to query the router (QDManage and QDStat) |
|	router_config | /etc/qpid-dispatch/qdrouterd.conf | A configuration file that can be parsed (future usage) |
|	service |	qdrouterd | Name of systemd/initd service that can be used to control the router instance. A service variable is only expected when running in a VM or Bare Metal (not in a container). If the executor is set to docker, then service name is irrelevant. |
|	user | admin@interconnect | The user needed to authenticate on router listener
|	password | password | Password for provided user |
|	pem_file | /router-crt.pem | A fully qualified filename for public key file needed to authenticate with the router |
|	key_file | /router-key.pem | A fully qualified filename for the private key file needed to authenticate with the router |
|	key_password | password | Password needed to read the private key |
|	executor | ansible (default)<br>docker<br>ssh<br>local<br>kubernetes | Defines the executor instance that will be used to execute commands on the given node. |

## Broker variables
| Variable name |	Sample value |	Description |
|-|-|-|
|	component |	broker |	Type of component that will be instantiated by IQAInstance (client, router or broker) |
|	broker_name |	broker1 |	Name of the broker instance (usually defined on broker.xml). It is needed when invoking Jolokia APIs. |
|	broker_path | /opt/broker1 |	A path where the broker instance is installed into. |
|	broker_web_port | 8161 |	Port where console and Jolokia API are running, so the internal component can query/manage the broker. |
|	broker_user |	admin (default) |	Username needed to communicate with the broker management API |
|	broker_password |	admin (default) |	Password for the provided broker_user. |
|	implementation |	artemis |	(Optional) Supported implementation of a broker component (default and only available is Artemis) |
| artemis_port |	61616 |	Default port to use for all messaging |
|	broker_service_user |	jamq |	User to operate artemis `service`|


# Executor variables per implementation

## Executor: ansible (default)
| Variable name |	Sample value |	Description |
|-|-|-|
|	executor_module (not useful for inventory files) |	ping |	You can specify a custom module to be used  when executing commands via ansible. If you do so (usually internally only, not on inventory definition) |
|	executor_docker_host |	10.0.0.100 |	You can specify a remote host that will be used by ansible to run commands on a remote container. If you have a client component running in a remote machine and you want to execute commands with ansible, you can set this up. |

## Executor: docker
| Variable name |	Sample value |	Description |
|-|-|-|
|	executor_docker_user |	root |	The user to be used when running commands on a related container
| executor_docker_host | 10.0.0.100 |	You can specify a remote host that will be used by docker to run commands on a remote container. If you have a client component running in a remote machine and you want to execute commands with docker, you can set this up. |
|	executor_docker_network |	bridge (default) |	The network name where a container is running. It is useful for determining the correct IP address for the running container. Just set it if you are using a custom docker network. |

## Executor: ssh
| Variable name |	Sample value |	Description
|-|-|-|
|	executor_hostname |	10.0.0.1 |	The hostname to be used within the ssh command
|	executor_port |	22 (default) |	The TCP port to use
|	executor_user |	root |	Username to be used in the ssh command
|	executor_ssl_private_key |	/root/my-key.pem |	The fully qualified filename for the private key used to authenticate

## Executor: kubernetes
| Variable name |	Sample value |	Description
|-|-|-
|	executors_kubernetes_config |	$HOME/.kube/config |	Kubernetes config file
|	executor_kubernetes_namespace |	default |	Namespace to use when querying for POD to run your command (Default: default)
|	executor_kubernetes_selector | |	The selector that can be used to identify the pod or deployment containing Pods.
|	executor_kubernetes_context | | If your client credentials are already defined in your config file, provide the context name.
|	executor_kubernetes_host | | If you do not want to use a context, you can provide the host (URL) for your cluster. The executor_kubernetes_token is also required if you are not using a context. Example: https://192.168.42.99:8443
|	executor_kubernetes_token | | If you do not want to use a context, you can provide a valid Token to use for authentication and authorization. The executor_kubernetes_host is also required when a token is defined.
