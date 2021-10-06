<template>
    <div>
        <page-title :heading=heading
                    :icon=icon
                    v-if="heading"
                    :delButton="true"
                    :model="software"
                    :modelName="modelName">
        </page-title>
        <SoftwareForm :update="true"></SoftwareForm>
    </div>
</template>

<script>
    import {mapState} from 'vuex'
    import PageTitle from "~/components/partials/PageTitle";
    import SoftwareForm from "~/components/software/SoftwareForm";

    export default {
        name: 'software-update',
        async fetch({store, params, redirect}) {
            if (params.id) {
                await store.dispatch('software/getSoftwareDetail', params.id);
            } else {
                redirect('/technologie/seznam/');
            }
        },
        components: {
            PageTitle,
            SoftwareForm
        },
        data: () => ({
            heading: $nuxt.$t('software.update_title'),
            icon: 'pe-7s-note',
            modelName: 'software'
        }),
        computed: {
            ...mapState({
                software: state => state.software.software
            })
        }

    }
</script>