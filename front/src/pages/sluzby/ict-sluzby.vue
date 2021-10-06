<template>
    <div>
        <page-title :heading=heading
                    :subheading=subheading
                    :icon=icon
                    v-if="heading">
        </page-title>
        <ict-services :highlight-id="id"></ict-services>
    </div>
</template>

<script>
    import PageTitle from "~/components/partials/PageTitle";
    import IctServices from "../../components/services/IctServices";

    export default {
        name: "ict-sluzby",
        components: {
            IctServices,
            PageTitle
        },
        data: () => ({
            icon: 'pe-7s-server',
            heading: $nuxt.$t('menu.ict_services'),
            subheading: $nuxt.$t('services.ict_services.info_text'),
            id: null,
        }),
        created() {
            this.id = this.$route?.query?.id
        },
    }
</script>

<style scoped>
</style>