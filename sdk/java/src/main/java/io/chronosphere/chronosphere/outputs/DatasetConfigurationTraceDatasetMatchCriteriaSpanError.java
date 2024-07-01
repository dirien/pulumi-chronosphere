// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package io.chronosphere.chronosphere.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.Boolean;
import java.util.Objects;

@CustomType
public final class DatasetConfigurationTraceDatasetMatchCriteriaSpanError {
    private Boolean value;

    private DatasetConfigurationTraceDatasetMatchCriteriaSpanError() {}
    public Boolean value() {
        return this.value;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(DatasetConfigurationTraceDatasetMatchCriteriaSpanError defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private Boolean value;
        public Builder() {}
        public Builder(DatasetConfigurationTraceDatasetMatchCriteriaSpanError defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.value = defaults.value;
        }

        @CustomType.Setter
        public Builder value(Boolean value) {
            this.value = Objects.requireNonNull(value);
            return this;
        }
        public DatasetConfigurationTraceDatasetMatchCriteriaSpanError build() {
            final var o = new DatasetConfigurationTraceDatasetMatchCriteriaSpanError();
            o.value = value;
            return o;
        }
    }
}
