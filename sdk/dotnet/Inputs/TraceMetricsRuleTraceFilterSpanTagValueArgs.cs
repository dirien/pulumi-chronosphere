// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Chronosphere.Inputs
{

    public sealed class TraceMetricsRuleTraceFilterSpanTagValueArgs : global::Pulumi.ResourceArgs
    {
        [Input("inValues")]
        private InputList<string>? _inValues;
        public InputList<string> InValues
        {
            get => _inValues ?? (_inValues = new InputList<string>());
            set => _inValues = value;
        }

        [Input("match")]
        public Input<string>? Match { get; set; }

        [Input("value")]
        public Input<string>? Value { get; set; }

        public TraceMetricsRuleTraceFilterSpanTagValueArgs()
        {
        }
        public static new TraceMetricsRuleTraceFilterSpanTagValueArgs Empty => new TraceMetricsRuleTraceFilterSpanTagValueArgs();
    }
}
