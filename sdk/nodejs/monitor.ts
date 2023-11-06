// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export class Monitor extends pulumi.CustomResource {
    /**
     * Get an existing Monitor resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MonitorState, opts?: pulumi.CustomResourceOptions): Monitor {
        return new Monitor(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'chronosphere:index/monitor:Monitor';

    /**
     * Returns true if the given object is an instance of Monitor.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Monitor {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Monitor.__pulumiType;
    }

    public readonly annotations!: pulumi.Output<{[key: string]: string} | undefined>;
    public readonly bucketId!: pulumi.Output<string | undefined>;
    public readonly collectionId!: pulumi.Output<string | undefined>;
    public readonly interval!: pulumi.Output<string | undefined>;
    public readonly labels!: pulumi.Output<{[key: string]: string} | undefined>;
    public readonly name!: pulumi.Output<string>;
    public readonly notificationPolicyId!: pulumi.Output<string | undefined>;
    public readonly query!: pulumi.Output<outputs.MonitorQuery>;
    public readonly schedule!: pulumi.Output<outputs.MonitorSchedule | undefined>;
    public readonly seriesConditions!: pulumi.Output<outputs.MonitorSeriesConditions>;
    public readonly signalGrouping!: pulumi.Output<outputs.MonitorSignalGrouping | undefined>;
    public readonly slug!: pulumi.Output<string>;

    /**
     * Create a Monitor resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MonitorArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: MonitorArgs | MonitorState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as MonitorState | undefined;
            resourceInputs["annotations"] = state ? state.annotations : undefined;
            resourceInputs["bucketId"] = state ? state.bucketId : undefined;
            resourceInputs["collectionId"] = state ? state.collectionId : undefined;
            resourceInputs["interval"] = state ? state.interval : undefined;
            resourceInputs["labels"] = state ? state.labels : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["notificationPolicyId"] = state ? state.notificationPolicyId : undefined;
            resourceInputs["query"] = state ? state.query : undefined;
            resourceInputs["schedule"] = state ? state.schedule : undefined;
            resourceInputs["seriesConditions"] = state ? state.seriesConditions : undefined;
            resourceInputs["signalGrouping"] = state ? state.signalGrouping : undefined;
            resourceInputs["slug"] = state ? state.slug : undefined;
        } else {
            const args = argsOrState as MonitorArgs | undefined;
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            if ((!args || args.query === undefined) && !opts.urn) {
                throw new Error("Missing required property 'query'");
            }
            if ((!args || args.seriesConditions === undefined) && !opts.urn) {
                throw new Error("Missing required property 'seriesConditions'");
            }
            resourceInputs["annotations"] = args ? args.annotations : undefined;
            resourceInputs["bucketId"] = args ? args.bucketId : undefined;
            resourceInputs["collectionId"] = args ? args.collectionId : undefined;
            resourceInputs["interval"] = args ? args.interval : undefined;
            resourceInputs["labels"] = args ? args.labels : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["notificationPolicyId"] = args ? args.notificationPolicyId : undefined;
            resourceInputs["query"] = args ? args.query : undefined;
            resourceInputs["schedule"] = args ? args.schedule : undefined;
            resourceInputs["seriesConditions"] = args ? args.seriesConditions : undefined;
            resourceInputs["signalGrouping"] = args ? args.signalGrouping : undefined;
            resourceInputs["slug"] = args ? args.slug : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Monitor.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Monitor resources.
 */
export interface MonitorState {
    annotations?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    bucketId?: pulumi.Input<string>;
    collectionId?: pulumi.Input<string>;
    interval?: pulumi.Input<string>;
    labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    name?: pulumi.Input<string>;
    notificationPolicyId?: pulumi.Input<string>;
    query?: pulumi.Input<inputs.MonitorQuery>;
    schedule?: pulumi.Input<inputs.MonitorSchedule>;
    seriesConditions?: pulumi.Input<inputs.MonitorSeriesConditions>;
    signalGrouping?: pulumi.Input<inputs.MonitorSignalGrouping>;
    slug?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Monitor resource.
 */
export interface MonitorArgs {
    annotations?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    bucketId?: pulumi.Input<string>;
    collectionId?: pulumi.Input<string>;
    interval?: pulumi.Input<string>;
    labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    name: pulumi.Input<string>;
    notificationPolicyId?: pulumi.Input<string>;
    query: pulumi.Input<inputs.MonitorQuery>;
    schedule?: pulumi.Input<inputs.MonitorSchedule>;
    seriesConditions: pulumi.Input<inputs.MonitorSeriesConditions>;
    signalGrouping?: pulumi.Input<inputs.MonitorSignalGrouping>;
    slug?: pulumi.Input<string>;
}
