<template>
    <div>
        <page-title :heading=heading
                    :subheading=subheading
                    :icon=icon
                    v-if="heading"
                    :orderButton="false"/>
        <SearcherComponent
                companyType="categories/group"
                :searchMapMarkers="false"
        />
        <BoxComponent/>
    </div>
</template>

<script>
    import PageTitle from "../../components/partials/PageTitle";
    import SearcherComponent from "~/components/technology/SearcherComponent";
    import BoxComponent from "~/components/technology/BoxComponent";

    export default {
        name: "seznam-technologii",
        components: {PageTitle, SearcherComponent, BoxComponent},
        data: () => ({
            f2: {gradient: ["#4ec4c3"]},
            f3: {gradient: ["#793aff"]},
            heading: $nuxt.$t('menu.search_technologies'),
            subheading: $nuxt.$t('help_text.technologies_list'),
            icon: 'pe-7s-search icon-gradient bg-blue-icon',
        }),
    }
</script>

<style scoped>

</style>