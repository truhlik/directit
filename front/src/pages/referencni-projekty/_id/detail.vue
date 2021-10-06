<template>
    <div id="user-add-ref-project">
        <PageTitle :heading=heading
                   :icon=icon
                   v-if="heading"/>
        <ProjectDetail></ProjectDetail>
    </div>
</template>

<script>
import PageTitle from "../../../components/partials/PageTitle";
import ProjectDetail from "../../../components/referential-projects/ProjectDetail";

export default {
    name: "detail",
    components: {ProjectDetail, PageTitle},
    async fetch({store, params, redirect}) {
        if (params.id) {
            await store.dispatch('projects/getRefProjectDetail', params.id);
        } else {
            redirect('/subjekty/referencni-projekty/');
        }
    },
    data: () => ({
        heading: $nuxt.$t('menu.ref_project_detail'),
        icon: 'pe-7s-note2 icon-gradient bg-blue-icon',
    }),
}
</script>

<style scoped>

</style>