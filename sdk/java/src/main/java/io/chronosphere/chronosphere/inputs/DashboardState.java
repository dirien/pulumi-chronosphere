// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package io.chronosphere.chronosphere.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class DashboardState extends com.pulumi.resources.ResourceArgs {

    public static final DashboardState Empty = new DashboardState();

    @Import(name="collectionId")
    private @Nullable Output<String> collectionId;

    public Optional<Output<String>> collectionId() {
        return Optional.ofNullable(this.collectionId);
    }

    @Import(name="dashboardJson")
    private @Nullable Output<String> dashboardJson;

    public Optional<Output<String>> dashboardJson() {
        return Optional.ofNullable(this.dashboardJson);
    }

    @Import(name="name")
    private @Nullable Output<String> name;

    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    @Import(name="slug")
    private @Nullable Output<String> slug;

    public Optional<Output<String>> slug() {
        return Optional.ofNullable(this.slug);
    }

    private DashboardState() {}

    private DashboardState(DashboardState $) {
        this.collectionId = $.collectionId;
        this.dashboardJson = $.dashboardJson;
        this.name = $.name;
        this.slug = $.slug;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(DashboardState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private DashboardState $;

        public Builder() {
            $ = new DashboardState();
        }

        public Builder(DashboardState defaults) {
            $ = new DashboardState(Objects.requireNonNull(defaults));
        }

        public Builder collectionId(@Nullable Output<String> collectionId) {
            $.collectionId = collectionId;
            return this;
        }

        public Builder collectionId(String collectionId) {
            return collectionId(Output.of(collectionId));
        }

        public Builder dashboardJson(@Nullable Output<String> dashboardJson) {
            $.dashboardJson = dashboardJson;
            return this;
        }

        public Builder dashboardJson(String dashboardJson) {
            return dashboardJson(Output.of(dashboardJson));
        }

        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        public Builder name(String name) {
            return name(Output.of(name));
        }

        public Builder slug(@Nullable Output<String> slug) {
            $.slug = slug;
            return this;
        }

        public Builder slug(String slug) {
            return slug(Output.of(slug));
        }

        public DashboardState build() {
            return $;
        }
    }

}
