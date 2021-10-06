<template>
    <div class="mt-5" v-if="id">
        <!--<pre>{{messagesTree}}</pre>-->
        <div class="w-100">
            <ProjectMessageForm :parent="null" :thread="id"></ProjectMessageForm>
        </div>
        <ProjectMessagesThread parent="root" :thread="id"></ProjectMessagesThread>
    </div>
</template>

<script>
    import ProjectMessagesThread from "./ProjectMessagesThread";
    import ProjectMessageForm from "./ProjectMessageForm";


    export default {
        name: "ProjectMessages",
        components: {ProjectMessagesThread, ProjectMessageForm},
        props: {
            id: String | Number,
        },
    }
</script>

<style scoped>

</style>