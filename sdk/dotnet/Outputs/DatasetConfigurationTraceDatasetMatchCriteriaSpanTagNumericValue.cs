// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Chronosphere.Outputs
{

    [OutputType]
    public sealed class DatasetConfigurationTraceDatasetMatchCriteriaSpanTagNumericValue
    {
        public readonly string Comparison;
        public readonly double Value;

        [OutputConstructor]
        private DatasetConfigurationTraceDatasetMatchCriteriaSpanTagNumericValue(
            string comparison,

            double value)
        {
            Comparison = comparison;
            Value = value;
        }
    }
}
