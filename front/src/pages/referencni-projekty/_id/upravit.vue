<template>
    <div id="user-add-ref-project">
        <PageTitle :heading=heading
                   :subheading=subheading
                   :icon=icon
                   v-if="heading"/>
        <ProjectForm
            :update="true"></ProjectForm>
    </div>
</template>

<script>
import PageTitle from "~/components/partials/PageTitle";
import ProjectForm from "~/components/referential-projects/ProjectForm.vue";

export default {
    name: "upravit",
    components: {ProjectForm, PageTitle},
    async fetch({store, params, redirect}) {
        if (params.id) {
            await store.dispatch('projects/getRefProjectDetail', params.id);
        } else {
            redirect('/subjekty/referencni-projekty/');
        }
    },
    data: () => ({
        heading: $nuxt.$t('menu.ref_project_create'),
        icon: 'pe-7s-note2 icon-gradient bg-blue-icon',
        subheading: $nuxt.$t('help_text.reference_project'),
    }),
}
</script>

<style scoped>

</style>