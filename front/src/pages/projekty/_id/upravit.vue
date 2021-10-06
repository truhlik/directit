<template>
    <div>
        <page-title
                :heading=heading
                :icon=icon
                v-if="heading"
                :delButton="true"
                :model="project"
                :modelName="modelName">
        </page-title>

        <ProjectForm
                :update="true"></ProjectForm>
    </div>
</template>

<script>
    import {mapState} from 'vuex'
    import PageTitle from "~/components/partials/PageTitle";
    import ProjectForm from "~/components/projects/ProjectForm";

    export default {
        name: 'project-list',
        async fetch({store, params, redirect}) {
            if (params.id) {
                await store.dispatch('projects/getProjectDetail', params.id);
            } else {
                redirect('/projekty/seznam/');
            }
        },
        components: {
            PageTitle,
            ProjectForm
        },
        data: () => ({
            heading: $nuxt.$t('projects.title_update'),
            icon: 'pe-7s-vector',
            modelName: 'projects'
        }),
        computed: {
            ...mapState({
                project: state => state.projects.project
            })
        }
    }
</script>