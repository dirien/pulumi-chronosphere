// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Chronosphere.Inputs
{

    public sealed class DatasetConfigurationTraceDatasetMatchCriteriaArgs : global::Pulumi.ResourceArgs
    {
        [Input("spans")]
        private InputList<Inputs.DatasetConfigurationTraceDatasetMatchCriteriaSpanArgs>? _spans;
        public InputList<Inputs.DatasetConfigurationTraceDatasetMatchCriteriaSpanArgs> Spans
        {
            get => _spans ?? (_spans = new InputList<Inputs.DatasetConfigurationTraceDatasetMatchCriteriaSpanArgs>());
            set => _spans = value;
        }

        [Input("trace")]
        public Input<Inputs.DatasetConfigurationTraceDatasetMatchCriteriaTraceArgs>? Trace { get; set; }

        public DatasetConfigurationTraceDatasetMatchCriteriaArgs()
        {
        }
        public static new DatasetConfigurationTraceDatasetMatchCriteriaArgs Empty => new DatasetConfigurationTraceDatasetMatchCriteriaArgs();
    }
}
