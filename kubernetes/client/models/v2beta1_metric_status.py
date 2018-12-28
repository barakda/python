# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.11.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V2beta1MetricStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'external': 'V2beta1ExternalMetricStatus',
        'object': 'V2beta1ObjectMetricStatus',
        'pods': 'V2beta1PodsMetricStatus',
        'resource': 'V2beta1ResourceMetricStatus',
        'type': 'str'
    }

    attribute_map = {
        'external': 'external',
        'object': 'object',
        'pods': 'pods',
        'resource': 'resource',
        'type': 'type'
    }

    def __init__(self, external=None, object=None, pods=None, resource=None, type=None):
        """
        V2beta1MetricStatus - a model defined in Swagger
        """

        self._external = None
        self._object = None
        self._pods = None
        self._resource = None
        self._type = None
        self.discriminator = None

        if external is not None:
          self.external = external
        if object is not None:
          self.object = object
        if pods is not None:
          self.pods = pods
        if resource is not None:
          self.resource = resource
        self.type = type

    @property
    def external(self):
        """
        Gets the external of this V2beta1MetricStatus.
        external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).

        :return: The external of this V2beta1MetricStatus.
        :rtype: V2beta1ExternalMetricStatus
        """
        return self._external

    @external.setter
    def external(self, external):
        """
        Sets the external of this V2beta1MetricStatus.
        external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).

        :param external: The external of this V2beta1MetricStatus.
        :type: V2beta1ExternalMetricStatus
        """

        self._external = external

    @property
    def object(self):
        """
        Gets the object of this V2beta1MetricStatus.
        object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object).

        :return: The object of this V2beta1MetricStatus.
        :rtype: V2beta1ObjectMetricStatus
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this V2beta1MetricStatus.
        object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object).

        :param object: The object of this V2beta1MetricStatus.
        :type: V2beta1ObjectMetricStatus
        """

        self._object = object

    @property
    def pods(self):
        """
        Gets the pods of this V2beta1MetricStatus.
        pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value.

        :return: The pods of this V2beta1MetricStatus.
        :rtype: V2beta1PodsMetricStatus
        """
        return self._pods

    @pods.setter
    def pods(self, pods):
        """
        Sets the pods of this V2beta1MetricStatus.
        pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value.

        :param pods: The pods of this V2beta1MetricStatus.
        :type: V2beta1PodsMetricStatus
        """

        self._pods = pods

    @property
    def resource(self):
        """
        Gets the resource of this V2beta1MetricStatus.
        resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the \"pods\" source.

        :return: The resource of this V2beta1MetricStatus.
        :rtype: V2beta1ResourceMetricStatus
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """
        Sets the resource of this V2beta1MetricStatus.
        resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the \"pods\" source.

        :param resource: The resource of this V2beta1MetricStatus.
        :type: V2beta1ResourceMetricStatus
        """

        self._resource = resource

    @property
    def type(self):
        """
        Gets the type of this V2beta1MetricStatus.
        type is the type of metric source.  It will be one of \"Object\", \"Pods\" or \"Resource\", each corresponds to a matching field in the object.

        :return: The type of this V2beta1MetricStatus.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V2beta1MetricStatus.
        type is the type of metric source.  It will be one of \"Object\", \"Pods\" or \"Resource\", each corresponds to a matching field in the object.

        :param type: The type of this V2beta1MetricStatus.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V2beta1MetricStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
