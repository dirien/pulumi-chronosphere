// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export class PagerdutyAlertNotifier extends pulumi.CustomResource {
    /**
     * Get an existing PagerdutyAlertNotifier resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PagerdutyAlertNotifierState, opts?: pulumi.CustomResourceOptions): PagerdutyAlertNotifier {
        return new PagerdutyAlertNotifier(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'chronosphere:index/pagerdutyAlertNotifier:PagerdutyAlertNotifier';

    /**
     * Returns true if the given object is an instance of PagerdutyAlertNotifier.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PagerdutyAlertNotifier {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PagerdutyAlertNotifier.__pulumiType;
    }

    public readonly basicAuthPassword!: pulumi.Output<string | undefined>;
    public readonly basicAuthUsername!: pulumi.Output<string | undefined>;
    public readonly bearerToken!: pulumi.Output<string | undefined>;
    public readonly class!: pulumi.Output<string | undefined>;
    public readonly client!: pulumi.Output<string | undefined>;
    public readonly clientUrl!: pulumi.Output<string | undefined>;
    public readonly component!: pulumi.Output<string | undefined>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly details!: pulumi.Output<{[key: string]: string} | undefined>;
    public readonly group!: pulumi.Output<string | undefined>;
    public readonly images!: pulumi.Output<outputs.PagerdutyAlertNotifierImage[] | undefined>;
    public readonly links!: pulumi.Output<outputs.PagerdutyAlertNotifierLink[] | undefined>;
    public readonly name!: pulumi.Output<string>;
    /**
     * @deprecated custom proxy URLs are not supported
     */
    public readonly proxyUrl!: pulumi.Output<string | undefined>;
    public readonly routingKey!: pulumi.Output<string | undefined>;
    public readonly sendResolved!: pulumi.Output<boolean | undefined>;
    public readonly serviceKey!: pulumi.Output<string | undefined>;
    public readonly severity!: pulumi.Output<string>;
    public readonly slug!: pulumi.Output<string>;
    public readonly tlsInsecureSkipVerify!: pulumi.Output<boolean | undefined>;
    public readonly url!: pulumi.Output<string>;

    /**
     * Create a PagerdutyAlertNotifier resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PagerdutyAlertNotifierArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PagerdutyAlertNotifierArgs | PagerdutyAlertNotifierState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as PagerdutyAlertNotifierState | undefined;
            resourceInputs["basicAuthPassword"] = state ? state.basicAuthPassword : undefined;
            resourceInputs["basicAuthUsername"] = state ? state.basicAuthUsername : undefined;
            resourceInputs["bearerToken"] = state ? state.bearerToken : undefined;
            resourceInputs["class"] = state ? state.class : undefined;
            resourceInputs["client"] = state ? state.client : undefined;
            resourceInputs["clientUrl"] = state ? state.clientUrl : undefined;
            resourceInputs["component"] = state ? state.component : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["details"] = state ? state.details : undefined;
            resourceInputs["group"] = state ? state.group : undefined;
            resourceInputs["images"] = state ? state.images : undefined;
            resourceInputs["links"] = state ? state.links : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["proxyUrl"] = state ? state.proxyUrl : undefined;
            resourceInputs["routingKey"] = state ? state.routingKey : undefined;
            resourceInputs["sendResolved"] = state ? state.sendResolved : undefined;
            resourceInputs["serviceKey"] = state ? state.serviceKey : undefined;
            resourceInputs["severity"] = state ? state.severity : undefined;
            resourceInputs["slug"] = state ? state.slug : undefined;
            resourceInputs["tlsInsecureSkipVerify"] = state ? state.tlsInsecureSkipVerify : undefined;
            resourceInputs["url"] = state ? state.url : undefined;
        } else {
            const args = argsOrState as PagerdutyAlertNotifierArgs | undefined;
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            if ((!args || args.severity === undefined) && !opts.urn) {
                throw new Error("Missing required property 'severity'");
            }
            if ((!args || args.url === undefined) && !opts.urn) {
                throw new Error("Missing required property 'url'");
            }
            resourceInputs["basicAuthPassword"] = args?.basicAuthPassword ? pulumi.secret(args.basicAuthPassword) : undefined;
            resourceInputs["basicAuthUsername"] = args ? args.basicAuthUsername : undefined;
            resourceInputs["bearerToken"] = args ? args.bearerToken : undefined;
            resourceInputs["class"] = args ? args.class : undefined;
            resourceInputs["client"] = args ? args.client : undefined;
            resourceInputs["clientUrl"] = args ? args.clientUrl : undefined;
            resourceInputs["component"] = args ? args.component : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["details"] = args ? args.details : undefined;
            resourceInputs["group"] = args ? args.group : undefined;
            resourceInputs["images"] = args ? args.images : undefined;
            resourceInputs["links"] = args ? args.links : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["proxyUrl"] = args ? args.proxyUrl : undefined;
            resourceInputs["routingKey"] = args ? args.routingKey : undefined;
            resourceInputs["sendResolved"] = args ? args.sendResolved : undefined;
            resourceInputs["serviceKey"] = args?.serviceKey ? pulumi.secret(args.serviceKey) : undefined;
            resourceInputs["severity"] = args ? args.severity : undefined;
            resourceInputs["slug"] = args ? args.slug : undefined;
            resourceInputs["tlsInsecureSkipVerify"] = args ? args.tlsInsecureSkipVerify : undefined;
            resourceInputs["url"] = args ? args.url : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["basicAuthPassword", "serviceKey"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(PagerdutyAlertNotifier.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering PagerdutyAlertNotifier resources.
 */
export interface PagerdutyAlertNotifierState {
    basicAuthPassword?: pulumi.Input<string>;
    basicAuthUsername?: pulumi.Input<string>;
    bearerToken?: pulumi.Input<string>;
    class?: pulumi.Input<string>;
    client?: pulumi.Input<string>;
    clientUrl?: pulumi.Input<string>;
    component?: pulumi.Input<string>;
    description?: pulumi.Input<string>;
    details?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    group?: pulumi.Input<string>;
    images?: pulumi.Input<pulumi.Input<inputs.PagerdutyAlertNotifierImage>[]>;
    links?: pulumi.Input<pulumi.Input<inputs.PagerdutyAlertNotifierLink>[]>;
    name?: pulumi.Input<string>;
    /**
     * @deprecated custom proxy URLs are not supported
     */
    proxyUrl?: pulumi.Input<string>;
    routingKey?: pulumi.Input<string>;
    sendResolved?: pulumi.Input<boolean>;
    serviceKey?: pulumi.Input<string>;
    severity?: pulumi.Input<string>;
    slug?: pulumi.Input<string>;
    tlsInsecureSkipVerify?: pulumi.Input<boolean>;
    url?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a PagerdutyAlertNotifier resource.
 */
export interface PagerdutyAlertNotifierArgs {
    basicAuthPassword?: pulumi.Input<string>;
    basicAuthUsername?: pulumi.Input<string>;
    bearerToken?: pulumi.Input<string>;
    class?: pulumi.Input<string>;
    client?: pulumi.Input<string>;
    clientUrl?: pulumi.Input<string>;
    component?: pulumi.Input<string>;
    description?: pulumi.Input<string>;
    details?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    group?: pulumi.Input<string>;
    images?: pulumi.Input<pulumi.Input<inputs.PagerdutyAlertNotifierImage>[]>;
    links?: pulumi.Input<pulumi.Input<inputs.PagerdutyAlertNotifierLink>[]>;
    name: pulumi.Input<string>;
    /**
     * @deprecated custom proxy URLs are not supported
     */
    proxyUrl?: pulumi.Input<string>;
    routingKey?: pulumi.Input<string>;
    sendResolved?: pulumi.Input<boolean>;
    serviceKey?: pulumi.Input<string>;
    severity: pulumi.Input<string>;
    slug?: pulumi.Input<string>;
    tlsInsecureSkipVerify?: pulumi.Input<boolean>;
    url: pulumi.Input<string>;
}
