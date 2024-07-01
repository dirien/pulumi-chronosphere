// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Chronosphere.Inputs
{

    public sealed class TraceTailSamplingRulesRuleFilterSpanGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("duration")]
        public Input<Inputs.TraceTailSamplingRulesRuleFilterSpanDurationGetArgs>? Duration { get; set; }

        [Input("error")]
        public Input<Inputs.TraceTailSamplingRulesRuleFilterSpanErrorGetArgs>? Error { get; set; }

        [Input("matchType")]
        public Input<string>? MatchType { get; set; }

        [Input("operation")]
        public Input<Inputs.TraceTailSamplingRulesRuleFilterSpanOperationGetArgs>? Operation { get; set; }

        [Input("parentOperation")]
        public Input<Inputs.TraceTailSamplingRulesRuleFilterSpanParentOperationGetArgs>? ParentOperation { get; set; }

        [Input("parentService")]
        public Input<Inputs.TraceTailSamplingRulesRuleFilterSpanParentServiceGetArgs>? ParentService { get; set; }

        [Input("service")]
        public Input<Inputs.TraceTailSamplingRulesRuleFilterSpanServiceGetArgs>? Service { get; set; }

        [Input("spanCount")]
        public Input<Inputs.TraceTailSamplingRulesRuleFilterSpanSpanCountGetArgs>? SpanCount { get; set; }

        [Input("tag")]
        private InputList<Inputs.TraceTailSamplingRulesRuleFilterSpanTagGetArgs>? _tag;
        public InputList<Inputs.TraceTailSamplingRulesRuleFilterSpanTagGetArgs> Tag
        {
            get => _tag ?? (_tag = new InputList<Inputs.TraceTailSamplingRulesRuleFilterSpanTagGetArgs>());
            set => _tag = value;
        }

        [Input("tags")]
        private InputList<Inputs.TraceTailSamplingRulesRuleFilterSpanTagGetArgs>? _tags;
        [Obsolete(@"`tags` is deprecated, use `tag` instead.")]
        public InputList<Inputs.TraceTailSamplingRulesRuleFilterSpanTagGetArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.TraceTailSamplingRulesRuleFilterSpanTagGetArgs>());
            set => _tags = value;
        }

        public TraceTailSamplingRulesRuleFilterSpanGetArgs()
        {
        }
        public static new TraceTailSamplingRulesRuleFilterSpanGetArgs Empty => new TraceTailSamplingRulesRuleFilterSpanGetArgs();
    }
}
