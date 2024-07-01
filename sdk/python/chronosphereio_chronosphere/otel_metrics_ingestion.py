# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['OtelMetricsIngestionArgs', 'OtelMetricsIngestion']

@pulumi.input_type
class OtelMetricsIngestionArgs:
    def __init__(__self__, *,
                 resource_attributes: Optional[pulumi.Input['OtelMetricsIngestionResourceAttributesArgs']] = None):
        """
        The set of arguments for constructing a OtelMetricsIngestion resource.
        """
        if resource_attributes is not None:
            pulumi.set(__self__, "resource_attributes", resource_attributes)

    @property
    @pulumi.getter(name="resourceAttributes")
    def resource_attributes(self) -> Optional[pulumi.Input['OtelMetricsIngestionResourceAttributesArgs']]:
        return pulumi.get(self, "resource_attributes")

    @resource_attributes.setter
    def resource_attributes(self, value: Optional[pulumi.Input['OtelMetricsIngestionResourceAttributesArgs']]):
        pulumi.set(self, "resource_attributes", value)


@pulumi.input_type
class _OtelMetricsIngestionState:
    def __init__(__self__, *,
                 resource_attributes: Optional[pulumi.Input['OtelMetricsIngestionResourceAttributesArgs']] = None):
        """
        Input properties used for looking up and filtering OtelMetricsIngestion resources.
        """
        if resource_attributes is not None:
            pulumi.set(__self__, "resource_attributes", resource_attributes)

    @property
    @pulumi.getter(name="resourceAttributes")
    def resource_attributes(self) -> Optional[pulumi.Input['OtelMetricsIngestionResourceAttributesArgs']]:
        return pulumi.get(self, "resource_attributes")

    @resource_attributes.setter
    def resource_attributes(self, value: Optional[pulumi.Input['OtelMetricsIngestionResourceAttributesArgs']]):
        pulumi.set(self, "resource_attributes", value)


class OtelMetricsIngestion(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resource_attributes: Optional[pulumi.Input[pulumi.InputType['OtelMetricsIngestionResourceAttributesArgs']]] = None,
                 __props__=None):
        """
        Create a OtelMetricsIngestion resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[OtelMetricsIngestionArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a OtelMetricsIngestion resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param OtelMetricsIngestionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OtelMetricsIngestionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resource_attributes: Optional[pulumi.Input[pulumi.InputType['OtelMetricsIngestionResourceAttributesArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OtelMetricsIngestionArgs.__new__(OtelMetricsIngestionArgs)

            __props__.__dict__["resource_attributes"] = resource_attributes
        super(OtelMetricsIngestion, __self__).__init__(
            'chronosphere:index/otelMetricsIngestion:OtelMetricsIngestion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            resource_attributes: Optional[pulumi.Input[pulumi.InputType['OtelMetricsIngestionResourceAttributesArgs']]] = None) -> 'OtelMetricsIngestion':
        """
        Get an existing OtelMetricsIngestion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OtelMetricsIngestionState.__new__(_OtelMetricsIngestionState)

        __props__.__dict__["resource_attributes"] = resource_attributes
        return OtelMetricsIngestion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="resourceAttributes")
    def resource_attributes(self) -> pulumi.Output[Optional['outputs.OtelMetricsIngestionResourceAttributes']]:
        return pulumi.get(self, "resource_attributes")

