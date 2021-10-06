<template>
    <div class="ares-box">
        <b-spinner class="map-spinner" variant="primary" label="Spinning" v-if="loadingAres"></b-spinner>
        <div class="card-shadow-primary card-border text-white mb-3 mt-3 card bg-primary" v-if="aresData">
            <div class="dropdown-menu-header">
                <div class="dropdown-menu-header-inner bg-primary">
                    <div class="menu-header-content">
                        <div>
                            <h5 class="menu-header-title">{{ aresData.first_name }} {{ aresData.last_name }}</h5>
                            <h6 class="menu-header-subtitle">{{ aresData.name }} ({{ aresData.vat_number }})</h6>
                        </div>
                        <div class="menu-header-btn-pane pt-1">
                        </div>
                    </div>
                </div>
            </div>
            <div class="text-center d-block card-footer">
                <p>
                    {{ aresData.street }} {{ aresData.street_number }},
                    {{ aresData.city }} {{ aresData.zip }}
                </p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "AresBox",
    props: {
        aresData: Object,
        loadingAres: Boolean,
    },
}
</script>

<style scoped lang="scss">
.card {
    border-radius: 0;

    h5 {
        margin: 0;
        text-align: center;
    }
}
</style>