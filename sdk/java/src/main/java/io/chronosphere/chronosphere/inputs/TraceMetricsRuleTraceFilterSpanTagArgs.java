// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package io.chronosphere.chronosphere.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import io.chronosphere.chronosphere.inputs.TraceMetricsRuleTraceFilterSpanTagNumericValueArgs;
import io.chronosphere.chronosphere.inputs.TraceMetricsRuleTraceFilterSpanTagValueArgs;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class TraceMetricsRuleTraceFilterSpanTagArgs extends com.pulumi.resources.ResourceArgs {

    public static final TraceMetricsRuleTraceFilterSpanTagArgs Empty = new TraceMetricsRuleTraceFilterSpanTagArgs();

    @Import(name="key")
    private @Nullable Output<String> key;

    public Optional<Output<String>> key() {
        return Optional.ofNullable(this.key);
    }

    @Import(name="numericValue")
    private @Nullable Output<TraceMetricsRuleTraceFilterSpanTagNumericValueArgs> numericValue;

    public Optional<Output<TraceMetricsRuleTraceFilterSpanTagNumericValueArgs>> numericValue() {
        return Optional.ofNullable(this.numericValue);
    }

    @Import(name="value")
    private @Nullable Output<TraceMetricsRuleTraceFilterSpanTagValueArgs> value;

    public Optional<Output<TraceMetricsRuleTraceFilterSpanTagValueArgs>> value() {
        return Optional.ofNullable(this.value);
    }

    private TraceMetricsRuleTraceFilterSpanTagArgs() {}

    private TraceMetricsRuleTraceFilterSpanTagArgs(TraceMetricsRuleTraceFilterSpanTagArgs $) {
        this.key = $.key;
        this.numericValue = $.numericValue;
        this.value = $.value;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(TraceMetricsRuleTraceFilterSpanTagArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private TraceMetricsRuleTraceFilterSpanTagArgs $;

        public Builder() {
            $ = new TraceMetricsRuleTraceFilterSpanTagArgs();
        }

        public Builder(TraceMetricsRuleTraceFilterSpanTagArgs defaults) {
            $ = new TraceMetricsRuleTraceFilterSpanTagArgs(Objects.requireNonNull(defaults));
        }

        public Builder key(@Nullable Output<String> key) {
            $.key = key;
            return this;
        }

        public Builder key(String key) {
            return key(Output.of(key));
        }

        public Builder numericValue(@Nullable Output<TraceMetricsRuleTraceFilterSpanTagNumericValueArgs> numericValue) {
            $.numericValue = numericValue;
            return this;
        }

        public Builder numericValue(TraceMetricsRuleTraceFilterSpanTagNumericValueArgs numericValue) {
            return numericValue(Output.of(numericValue));
        }

        public Builder value(@Nullable Output<TraceMetricsRuleTraceFilterSpanTagValueArgs> value) {
            $.value = value;
            return this;
        }

        public Builder value(TraceMetricsRuleTraceFilterSpanTagValueArgs value) {
            return value(Output.of(value));
        }

        public TraceMetricsRuleTraceFilterSpanTagArgs build() {
            return $;
        }
    }

}
