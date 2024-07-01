# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['VictoropsAlertNotifierArgs', 'VictoropsAlertNotifier']

@pulumi.input_type
class VictoropsAlertNotifierArgs:
    def __init__(__self__, *,
                 api_key: pulumi.Input[str],
                 name: pulumi.Input[str],
                 routing_key: pulumi.Input[str],
                 api_url: Optional[pulumi.Input[str]] = None,
                 basic_auth_password: Optional[pulumi.Input[str]] = None,
                 basic_auth_username: Optional[pulumi.Input[str]] = None,
                 bearer_token: Optional[pulumi.Input[str]] = None,
                 custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 entity_display_name: Optional[pulumi.Input[str]] = None,
                 message_type: Optional[pulumi.Input[str]] = None,
                 monitoring_tool: Optional[pulumi.Input[str]] = None,
                 proxy_url: Optional[pulumi.Input[str]] = None,
                 send_resolved: Optional[pulumi.Input[bool]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 state_message: Optional[pulumi.Input[str]] = None,
                 tls_insecure_skip_verify: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a VictoropsAlertNotifier resource.
        """
        pulumi.set(__self__, "api_key", api_key)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "routing_key", routing_key)
        if api_url is not None:
            pulumi.set(__self__, "api_url", api_url)
        if basic_auth_password is not None:
            pulumi.set(__self__, "basic_auth_password", basic_auth_password)
        if basic_auth_username is not None:
            pulumi.set(__self__, "basic_auth_username", basic_auth_username)
        if bearer_token is not None:
            pulumi.set(__self__, "bearer_token", bearer_token)
        if custom_fields is not None:
            pulumi.set(__self__, "custom_fields", custom_fields)
        if entity_display_name is not None:
            pulumi.set(__self__, "entity_display_name", entity_display_name)
        if message_type is not None:
            pulumi.set(__self__, "message_type", message_type)
        if monitoring_tool is not None:
            pulumi.set(__self__, "monitoring_tool", monitoring_tool)
        if proxy_url is not None:
            warnings.warn("""custom proxy URLs are not supported""", DeprecationWarning)
            pulumi.log.warn("""proxy_url is deprecated: custom proxy URLs are not supported""")
        if proxy_url is not None:
            pulumi.set(__self__, "proxy_url", proxy_url)
        if send_resolved is not None:
            pulumi.set(__self__, "send_resolved", send_resolved)
        if slug is not None:
            pulumi.set(__self__, "slug", slug)
        if state_message is not None:
            pulumi.set(__self__, "state_message", state_message)
        if tls_insecure_skip_verify is not None:
            pulumi.set(__self__, "tls_insecure_skip_verify", tls_insecure_skip_verify)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="routingKey")
    def routing_key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "routing_key")

    @routing_key.setter
    def routing_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "routing_key", value)

    @property
    @pulumi.getter(name="apiUrl")
    def api_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "api_url")

    @api_url.setter
    def api_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_url", value)

    @property
    @pulumi.getter(name="basicAuthPassword")
    def basic_auth_password(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "basic_auth_password")

    @basic_auth_password.setter
    def basic_auth_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "basic_auth_password", value)

    @property
    @pulumi.getter(name="basicAuthUsername")
    def basic_auth_username(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "basic_auth_username")

    @basic_auth_username.setter
    def basic_auth_username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "basic_auth_username", value)

    @property
    @pulumi.getter(name="bearerToken")
    def bearer_token(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "bearer_token")

    @bearer_token.setter
    def bearer_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bearer_token", value)

    @property
    @pulumi.getter(name="customFields")
    def custom_fields(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "custom_fields")

    @custom_fields.setter
    def custom_fields(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "custom_fields", value)

    @property
    @pulumi.getter(name="entityDisplayName")
    def entity_display_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "entity_display_name")

    @entity_display_name.setter
    def entity_display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "entity_display_name", value)

    @property
    @pulumi.getter(name="messageType")
    def message_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "message_type")

    @message_type.setter
    def message_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message_type", value)

    @property
    @pulumi.getter(name="monitoringTool")
    def monitoring_tool(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "monitoring_tool")

    @monitoring_tool.setter
    def monitoring_tool(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "monitoring_tool", value)

    @property
    @pulumi.getter(name="proxyUrl")
    def proxy_url(self) -> Optional[pulumi.Input[str]]:
        warnings.warn("""custom proxy URLs are not supported""", DeprecationWarning)
        pulumi.log.warn("""proxy_url is deprecated: custom proxy URLs are not supported""")

        return pulumi.get(self, "proxy_url")

    @proxy_url.setter
    def proxy_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "proxy_url", value)

    @property
    @pulumi.getter(name="sendResolved")
    def send_resolved(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "send_resolved")

    @send_resolved.setter
    def send_resolved(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "send_resolved", value)

    @property
    @pulumi.getter
    def slug(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "slug")

    @slug.setter
    def slug(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "slug", value)

    @property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "state_message")

    @state_message.setter
    def state_message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state_message", value)

    @property
    @pulumi.getter(name="tlsInsecureSkipVerify")
    def tls_insecure_skip_verify(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "tls_insecure_skip_verify")

    @tls_insecure_skip_verify.setter
    def tls_insecure_skip_verify(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "tls_insecure_skip_verify", value)


@pulumi.input_type
class _VictoropsAlertNotifierState:
    def __init__(__self__, *,
                 api_key: Optional[pulumi.Input[str]] = None,
                 api_url: Optional[pulumi.Input[str]] = None,
                 basic_auth_password: Optional[pulumi.Input[str]] = None,
                 basic_auth_username: Optional[pulumi.Input[str]] = None,
                 bearer_token: Optional[pulumi.Input[str]] = None,
                 custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 entity_display_name: Optional[pulumi.Input[str]] = None,
                 message_type: Optional[pulumi.Input[str]] = None,
                 monitoring_tool: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 proxy_url: Optional[pulumi.Input[str]] = None,
                 routing_key: Optional[pulumi.Input[str]] = None,
                 send_resolved: Optional[pulumi.Input[bool]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 state_message: Optional[pulumi.Input[str]] = None,
                 tls_insecure_skip_verify: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering VictoropsAlertNotifier resources.
        """
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)
        if api_url is not None:
            pulumi.set(__self__, "api_url", api_url)
        if basic_auth_password is not None:
            pulumi.set(__self__, "basic_auth_password", basic_auth_password)
        if basic_auth_username is not None:
            pulumi.set(__self__, "basic_auth_username", basic_auth_username)
        if bearer_token is not None:
            pulumi.set(__self__, "bearer_token", bearer_token)
        if custom_fields is not None:
            pulumi.set(__self__, "custom_fields", custom_fields)
        if entity_display_name is not None:
            pulumi.set(__self__, "entity_display_name", entity_display_name)
        if message_type is not None:
            pulumi.set(__self__, "message_type", message_type)
        if monitoring_tool is not None:
            pulumi.set(__self__, "monitoring_tool", monitoring_tool)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if proxy_url is not None:
            warnings.warn("""custom proxy URLs are not supported""", DeprecationWarning)
            pulumi.log.warn("""proxy_url is deprecated: custom proxy URLs are not supported""")
        if proxy_url is not None:
            pulumi.set(__self__, "proxy_url", proxy_url)
        if routing_key is not None:
            pulumi.set(__self__, "routing_key", routing_key)
        if send_resolved is not None:
            pulumi.set(__self__, "send_resolved", send_resolved)
        if slug is not None:
            pulumi.set(__self__, "slug", slug)
        if state_message is not None:
            pulumi.set(__self__, "state_message", state_message)
        if tls_insecure_skip_verify is not None:
            pulumi.set(__self__, "tls_insecure_skip_verify", tls_insecure_skip_verify)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter(name="apiUrl")
    def api_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "api_url")

    @api_url.setter
    def api_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_url", value)

    @property
    @pulumi.getter(name="basicAuthPassword")
    def basic_auth_password(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "basic_auth_password")

    @basic_auth_password.setter
    def basic_auth_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "basic_auth_password", value)

    @property
    @pulumi.getter(name="basicAuthUsername")
    def basic_auth_username(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "basic_auth_username")

    @basic_auth_username.setter
    def basic_auth_username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "basic_auth_username", value)

    @property
    @pulumi.getter(name="bearerToken")
    def bearer_token(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "bearer_token")

    @bearer_token.setter
    def bearer_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bearer_token", value)

    @property
    @pulumi.getter(name="customFields")
    def custom_fields(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "custom_fields")

    @custom_fields.setter
    def custom_fields(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "custom_fields", value)

    @property
    @pulumi.getter(name="entityDisplayName")
    def entity_display_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "entity_display_name")

    @entity_display_name.setter
    def entity_display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "entity_display_name", value)

    @property
    @pulumi.getter(name="messageType")
    def message_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "message_type")

    @message_type.setter
    def message_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message_type", value)

    @property
    @pulumi.getter(name="monitoringTool")
    def monitoring_tool(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "monitoring_tool")

    @monitoring_tool.setter
    def monitoring_tool(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "monitoring_tool", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="proxyUrl")
    def proxy_url(self) -> Optional[pulumi.Input[str]]:
        warnings.warn("""custom proxy URLs are not supported""", DeprecationWarning)
        pulumi.log.warn("""proxy_url is deprecated: custom proxy URLs are not supported""")

        return pulumi.get(self, "proxy_url")

    @proxy_url.setter
    def proxy_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "proxy_url", value)

    @property
    @pulumi.getter(name="routingKey")
    def routing_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "routing_key")

    @routing_key.setter
    def routing_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "routing_key", value)

    @property
    @pulumi.getter(name="sendResolved")
    def send_resolved(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "send_resolved")

    @send_resolved.setter
    def send_resolved(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "send_resolved", value)

    @property
    @pulumi.getter
    def slug(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "slug")

    @slug.setter
    def slug(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "slug", value)

    @property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "state_message")

    @state_message.setter
    def state_message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state_message", value)

    @property
    @pulumi.getter(name="tlsInsecureSkipVerify")
    def tls_insecure_skip_verify(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "tls_insecure_skip_verify")

    @tls_insecure_skip_verify.setter
    def tls_insecure_skip_verify(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "tls_insecure_skip_verify", value)


class VictoropsAlertNotifier(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 api_url: Optional[pulumi.Input[str]] = None,
                 basic_auth_password: Optional[pulumi.Input[str]] = None,
                 basic_auth_username: Optional[pulumi.Input[str]] = None,
                 bearer_token: Optional[pulumi.Input[str]] = None,
                 custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 entity_display_name: Optional[pulumi.Input[str]] = None,
                 message_type: Optional[pulumi.Input[str]] = None,
                 monitoring_tool: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 proxy_url: Optional[pulumi.Input[str]] = None,
                 routing_key: Optional[pulumi.Input[str]] = None,
                 send_resolved: Optional[pulumi.Input[bool]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 state_message: Optional[pulumi.Input[str]] = None,
                 tls_insecure_skip_verify: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Create a VictoropsAlertNotifier resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VictoropsAlertNotifierArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a VictoropsAlertNotifier resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param VictoropsAlertNotifierArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VictoropsAlertNotifierArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 api_url: Optional[pulumi.Input[str]] = None,
                 basic_auth_password: Optional[pulumi.Input[str]] = None,
                 basic_auth_username: Optional[pulumi.Input[str]] = None,
                 bearer_token: Optional[pulumi.Input[str]] = None,
                 custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 entity_display_name: Optional[pulumi.Input[str]] = None,
                 message_type: Optional[pulumi.Input[str]] = None,
                 monitoring_tool: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 proxy_url: Optional[pulumi.Input[str]] = None,
                 routing_key: Optional[pulumi.Input[str]] = None,
                 send_resolved: Optional[pulumi.Input[bool]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 state_message: Optional[pulumi.Input[str]] = None,
                 tls_insecure_skip_verify: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VictoropsAlertNotifierArgs.__new__(VictoropsAlertNotifierArgs)

            if api_key is None and not opts.urn:
                raise TypeError("Missing required property 'api_key'")
            __props__.__dict__["api_key"] = None if api_key is None else pulumi.Output.secret(api_key)
            __props__.__dict__["api_url"] = api_url
            __props__.__dict__["basic_auth_password"] = None if basic_auth_password is None else pulumi.Output.secret(basic_auth_password)
            __props__.__dict__["basic_auth_username"] = basic_auth_username
            __props__.__dict__["bearer_token"] = bearer_token
            __props__.__dict__["custom_fields"] = custom_fields
            __props__.__dict__["entity_display_name"] = entity_display_name
            __props__.__dict__["message_type"] = message_type
            __props__.__dict__["monitoring_tool"] = monitoring_tool
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["proxy_url"] = proxy_url
            if routing_key is None and not opts.urn:
                raise TypeError("Missing required property 'routing_key'")
            __props__.__dict__["routing_key"] = routing_key
            __props__.__dict__["send_resolved"] = send_resolved
            __props__.__dict__["slug"] = slug
            __props__.__dict__["state_message"] = state_message
            __props__.__dict__["tls_insecure_skip_verify"] = tls_insecure_skip_verify
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["apiKey", "basicAuthPassword"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(VictoropsAlertNotifier, __self__).__init__(
            'chronosphere:index/victoropsAlertNotifier:VictoropsAlertNotifier',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_key: Optional[pulumi.Input[str]] = None,
            api_url: Optional[pulumi.Input[str]] = None,
            basic_auth_password: Optional[pulumi.Input[str]] = None,
            basic_auth_username: Optional[pulumi.Input[str]] = None,
            bearer_token: Optional[pulumi.Input[str]] = None,
            custom_fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            entity_display_name: Optional[pulumi.Input[str]] = None,
            message_type: Optional[pulumi.Input[str]] = None,
            monitoring_tool: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            proxy_url: Optional[pulumi.Input[str]] = None,
            routing_key: Optional[pulumi.Input[str]] = None,
            send_resolved: Optional[pulumi.Input[bool]] = None,
            slug: Optional[pulumi.Input[str]] = None,
            state_message: Optional[pulumi.Input[str]] = None,
            tls_insecure_skip_verify: Optional[pulumi.Input[bool]] = None) -> 'VictoropsAlertNotifier':
        """
        Get an existing VictoropsAlertNotifier resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VictoropsAlertNotifierState.__new__(_VictoropsAlertNotifierState)

        __props__.__dict__["api_key"] = api_key
        __props__.__dict__["api_url"] = api_url
        __props__.__dict__["basic_auth_password"] = basic_auth_password
        __props__.__dict__["basic_auth_username"] = basic_auth_username
        __props__.__dict__["bearer_token"] = bearer_token
        __props__.__dict__["custom_fields"] = custom_fields
        __props__.__dict__["entity_display_name"] = entity_display_name
        __props__.__dict__["message_type"] = message_type
        __props__.__dict__["monitoring_tool"] = monitoring_tool
        __props__.__dict__["name"] = name
        __props__.__dict__["proxy_url"] = proxy_url
        __props__.__dict__["routing_key"] = routing_key
        __props__.__dict__["send_resolved"] = send_resolved
        __props__.__dict__["slug"] = slug
        __props__.__dict__["state_message"] = state_message
        __props__.__dict__["tls_insecure_skip_verify"] = tls_insecure_skip_verify
        return VictoropsAlertNotifier(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Output[str]:
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter(name="apiUrl")
    def api_url(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "api_url")

    @property
    @pulumi.getter(name="basicAuthPassword")
    def basic_auth_password(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "basic_auth_password")

    @property
    @pulumi.getter(name="basicAuthUsername")
    def basic_auth_username(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "basic_auth_username")

    @property
    @pulumi.getter(name="bearerToken")
    def bearer_token(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "bearer_token")

    @property
    @pulumi.getter(name="customFields")
    def custom_fields(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "custom_fields")

    @property
    @pulumi.getter(name="entityDisplayName")
    def entity_display_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "entity_display_name")

    @property
    @pulumi.getter(name="messageType")
    def message_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "message_type")

    @property
    @pulumi.getter(name="monitoringTool")
    def monitoring_tool(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "monitoring_tool")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="proxyUrl")
    def proxy_url(self) -> pulumi.Output[Optional[str]]:
        warnings.warn("""custom proxy URLs are not supported""", DeprecationWarning)
        pulumi.log.warn("""proxy_url is deprecated: custom proxy URLs are not supported""")

        return pulumi.get(self, "proxy_url")

    @property
    @pulumi.getter(name="routingKey")
    def routing_key(self) -> pulumi.Output[str]:
        return pulumi.get(self, "routing_key")

    @property
    @pulumi.getter(name="sendResolved")
    def send_resolved(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "send_resolved")

    @property
    @pulumi.getter
    def slug(self) -> pulumi.Output[str]:
        return pulumi.get(self, "slug")

    @property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "state_message")

    @property
    @pulumi.getter(name="tlsInsecureSkipVerify")
    def tls_insecure_skip_verify(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "tls_insecure_skip_verify")

