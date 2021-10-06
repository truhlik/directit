<template>
    <div>
        <page-title :heading=heading
                    :subheading="subheading"
                    :icon=icon
                    v-if="heading"
                    :pathUrl="pathUrl"
                    :pathName="$t('menu.software_list')"
                    :pathIcon="pathIcon">
        </page-title>
        <SoftwareForm></SoftwareForm>
        <div class="custom-container bg-transparent">
            <page-disclaimer :text="$t('disclaimer.technology_info')"></page-disclaimer>
        </div>
    </div>
</template>

<script>
import SoftwareForm from "~/components/software/SoftwareForm";
import PageTitle from "~/components/partials/PageTitle";
import PageDisclaimer from "../../components/partials/PageDisclaimer";

export default {
    name: 'create-software',
    async fetch({store}) {
        store.dispatch('software/clearSoftwareAction');
    },
    components: {
        PageDisclaimer,
        SoftwareForm,
        PageTitle
    },
    data: () => ({
        heading: $nuxt.$t('software.create_title'),
        icon: 'pe-7s-notebook',
        pathUrl: '/technologie/seznam/',
        pathIcon: 'list',
        subheading: $nuxt.$t('subheadings.software_create')
    })
}
</script>