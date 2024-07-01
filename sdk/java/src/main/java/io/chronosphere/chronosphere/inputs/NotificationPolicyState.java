// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package io.chronosphere.chronosphere.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import io.chronosphere.chronosphere.inputs.NotificationPolicyOverrideArgs;
import io.chronosphere.chronosphere.inputs.NotificationPolicyRouteArgs;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class NotificationPolicyState extends com.pulumi.resources.ResourceArgs {

    public static final NotificationPolicyState Empty = new NotificationPolicyState();

    @Import(name="isIndependent")
    private @Nullable Output<Boolean> isIndependent;

    public Optional<Output<Boolean>> isIndependent() {
        return Optional.ofNullable(this.isIndependent);
    }

    @Import(name="name")
    private @Nullable Output<String> name;

    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    @Import(name="notificationPolicyData")
    private @Nullable Output<String> notificationPolicyData;

    public Optional<Output<String>> notificationPolicyData() {
        return Optional.ofNullable(this.notificationPolicyData);
    }

    @Import(name="overrides")
    private @Nullable Output<List<NotificationPolicyOverrideArgs>> overrides;

    public Optional<Output<List<NotificationPolicyOverrideArgs>>> overrides() {
        return Optional.ofNullable(this.overrides);
    }

    @Import(name="routes")
    private @Nullable Output<List<NotificationPolicyRouteArgs>> routes;

    public Optional<Output<List<NotificationPolicyRouteArgs>>> routes() {
        return Optional.ofNullable(this.routes);
    }

    @Import(name="slug")
    private @Nullable Output<String> slug;

    public Optional<Output<String>> slug() {
        return Optional.ofNullable(this.slug);
    }

    @Import(name="teamId")
    private @Nullable Output<String> teamId;

    public Optional<Output<String>> teamId() {
        return Optional.ofNullable(this.teamId);
    }

    private NotificationPolicyState() {}

    private NotificationPolicyState(NotificationPolicyState $) {
        this.isIndependent = $.isIndependent;
        this.name = $.name;
        this.notificationPolicyData = $.notificationPolicyData;
        this.overrides = $.overrides;
        this.routes = $.routes;
        this.slug = $.slug;
        this.teamId = $.teamId;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(NotificationPolicyState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private NotificationPolicyState $;

        public Builder() {
            $ = new NotificationPolicyState();
        }

        public Builder(NotificationPolicyState defaults) {
            $ = new NotificationPolicyState(Objects.requireNonNull(defaults));
        }

        public Builder isIndependent(@Nullable Output<Boolean> isIndependent) {
            $.isIndependent = isIndependent;
            return this;
        }

        public Builder isIndependent(Boolean isIndependent) {
            return isIndependent(Output.of(isIndependent));
        }

        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        public Builder name(String name) {
            return name(Output.of(name));
        }

        public Builder notificationPolicyData(@Nullable Output<String> notificationPolicyData) {
            $.notificationPolicyData = notificationPolicyData;
            return this;
        }

        public Builder notificationPolicyData(String notificationPolicyData) {
            return notificationPolicyData(Output.of(notificationPolicyData));
        }

        public Builder overrides(@Nullable Output<List<NotificationPolicyOverrideArgs>> overrides) {
            $.overrides = overrides;
            return this;
        }

        public Builder overrides(List<NotificationPolicyOverrideArgs> overrides) {
            return overrides(Output.of(overrides));
        }

        public Builder overrides(NotificationPolicyOverrideArgs... overrides) {
            return overrides(List.of(overrides));
        }

        public Builder routes(@Nullable Output<List<NotificationPolicyRouteArgs>> routes) {
            $.routes = routes;
            return this;
        }

        public Builder routes(List<NotificationPolicyRouteArgs> routes) {
            return routes(Output.of(routes));
        }

        public Builder routes(NotificationPolicyRouteArgs... routes) {
            return routes(List.of(routes));
        }

        public Builder slug(@Nullable Output<String> slug) {
            $.slug = slug;
            return this;
        }

        public Builder slug(String slug) {
            return slug(Output.of(slug));
        }

        public Builder teamId(@Nullable Output<String> teamId) {
            $.teamId = teamId;
            return this;
        }

        public Builder teamId(String teamId) {
            return teamId(Output.of(teamId));
        }

        public NotificationPolicyState build() {
            return $;
        }
    }

}
