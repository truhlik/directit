<template>
    <div>
        <page-title :heading=heading
                    :subheading=subheading
                    :icon=icon
                    v-if="heading"
                    :orderButton="false"/>
        <SearcherComponent
        ></SearcherComponent>
        <BoxComponent/>
    </div>
</template>

<script>
    import PageTitle from "../../components/partials/PageTitle";
    import SearcherComponent from "~/components/referential-projects/SearcherComponent";
    import BoxComponent from "~/components/referential-projects/BoxComponent";
    export default {
        name: "referencni-projekty",
        components: {
            PageTitle,
            SearcherComponent,
            BoxComponent,
        },
        data: () => ({
            f2: {gradient: ["#c8a470"]},
            f3: {gradient: ["#783eff"]},
            heading: $nuxt.$t('menu.reference_projects'),
            subheading: $nuxt.$t('help_text.reference_projects'),
            icon: 'pe-7s-search icon-gradient bg-blue-icon',
        }),
    }
</script>

<style scoped>

</style>